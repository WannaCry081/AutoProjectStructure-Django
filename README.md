# AutoProjectStructure - Django

AutoProjectStructure is a Python script designed to automate the tedious environment setup in Django projects. It provides a user-friendly approach to setting up a Django project, including the creation of necessary files, directories, and environment variables. Additionally, it includes an executable file generated using PyInstaller for easy execution across different platforms.

## Features

- Automates Django environment setup
- User-friendly interface
- Monolithic Architecture for building APIs

## Packages Used

- pyinstaller
- os
- requests
- pathlib
- subprocess

## Project Structure

The structure below provides a clear visual representation of the directory hierarchy of the Django project, making it easy for users to understand the organization of files and directories.

   ```plaintext
   project_name
   │
   ├── app_name
   │   ├── authentications       # Custom authentication classes
   │   │   ├── __init__.py
   │   │   ├── ...
   │   ├── permissions           # Custom permission classes
   │   │   ├── ...
   │   ├── viewsets              # Controllers or viewsets classes
   │   │   ├── ...
   │   ├── models
   │   │   ├── ...
   │   ├── serializers
   │   │   ├── ...
   │   ├── utils
   │   │   ├── ...
   │   ├── migrations
   │   │   ├── ...
   │   ├── __init__.py
   │   ├── admin.py
   │   ├── apps.py
   │   └── urls.py
   │
   ├── config
   │   ├── settings
   │   │   ├── __init__.py
   │   │   ├── base.py
   │   │   ├── production.py
   │   │   └── local.py
   │   ├── __init__.py
   │   ├── wsgi.py
   │   └── asgi.py
   │
   ├── .dockerignore
   ├── .gitignore
   ├── manage.py
   ├── README.md
   └── Dockerfile
   ```

## Installation

To use AutoProjectStructure, follow these steps:

1. Clone the repository:

   ```bash
   $ git clone https://github.com/WannaCry081/AutoProjectStructure-Django.git
   ```

2. Navigate to the project directory:

   ```bash
   $ cd AutoProjectStructure-Django
   ```

3. Install the required packages:

   ```bash
   $ pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   $ python main.py
   ```

   or

   ```bash
   $ ./main.exe
   ```

## Usage

1. Run the script and follow the prompts to enter the project name and optional GitHub repository link.
2. The script will set up the Django environment, including creating directories, files, and environment variables.
3. Once completed, the project directory will be ready for development.

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.