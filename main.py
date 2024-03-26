import os
import requests
import subprocess
from pathlib import Path


class AutoProjectStructure:
    
    def setup_environment(self, project_name):
        python_libs = [
            "django\n",
            "djangorestframework\n",
            "djangorestframework-simplejwt\n",
            "djangorestframework-xml\n",
            "django-cors-headers\n",
            "djoser\n",
            "drf-yasg\n",
            "python-dotenv\n"
        ]
        
        environment_vars = [
            "DJANGO_ENV=\n",
            "DJANGO_SECRET_KEY=\n",
        ] 
        
        ignore_contents = [
            "**/__pycache__\n",
            "/venv\n",
            ".env\n"
        ]
        
        to_remove = [
            "models.py",
            "tests.py",
            "views.py"
        ]
        
        to_add = [
            "authentications\\__init__.py",
            "permissions\\__init__.py",
            "models\\__init__.py",
            "tests\\__init__.py",
            "serializers\\__init__.py",
            "viewsets\\__init__.py",
            "urls.py"
        ]
        
        os.system("virtualenv venv")
        self.create_structure("requirements.txt", python_libs)
        self.create_structure(".env", environment_vars)
        self.create_structure(".gitignore", ignore_contents)
        self.create_structure(".dockerignore", ignore_contents)
        self.create_structure("Dockerfile")
        self.create_structure("README.md", [f"# {project_name}"])
        
        subprocess.run(["venv\\Scripts\\activate.bat", "&&", "pip", "install", "-r", "requirements.txt"])
        subprocess.run(["django-admin", "startproject", "config", "."])
        
        os.mkdir("api")
        os.chdir("api")
        subprocess.run(["django-admin", "startapp", "v1"])
        os.chdir("v1")
        
        for file in to_remove:
            os.remove(file)
            
        for file in to_add:
            
            directory = os.path.dirname(file)
            if directory:
                os.makedirs(directory, exist_ok=True)
            
            with open(file, "a") as file:
                file.close()
    
        os.chdir("../..")
    
    
    def setup_project(self):
        pass
    
    
    def setup_version_control(self, github_repository):
        pass
    
    
def verify_github_repository(link):
    response = requests.get(link)
    return response.status_code == 200


def main():
    pass


if __name__ == "__main__":
    main()
    input()