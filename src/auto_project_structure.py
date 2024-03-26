import os
import subprocess


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
        contents = [
            "from .base import *\n\n",
            "DEBUG = False\n",
            "ALLOWED_HOSTS = []\n",
            "INTERNAL_IPS = [\"127.0.0.1\"]"
        ]
        
        os.chdir("config")
        os.mkdir("settings")
        os.rename("settings.py", "settings/base.py")
        os.chdir("settings")
        self.create_structure("__init__.py")
        self.create_structure("production.py", contents[:3])
        contents[1] = "DEBUG = True\n"
        self.create_structure("local.py", contents)
        
        with open("base.py", "r") as file:
            lines = file.readlines()
            file.close()
        
        lines = lines[:23] + lines[29:39] + ["\t\'rest_framework\',\n", "\t\'api\',\n"]  + lines[39:]

        with open("base.py", "w") as file:
            file.writelines(lines)
            file.close()
        
        os.chdir("..")
        
        for file_name in ["asgi.py", "wsgi.py", "manage.py"]:
            if file_name == "manage.py": 
                os.chdir("..")
                
            with open(file_name, "r") as file:
                lines = file.readlines()
                file.close()
                
            index = 13 if file_name != "manage.py" else 8
            lines[index] = lines[index][:-3] + ".local')\n"
            
            with open(file_name, "w") as file:
                file.writelines(lines)
                file.close()
                
        os.system("python manage.py migrate")
    
    
    def setup_version_control(self, github_repository):
        commands = [
            "git init",
            "git add .",
            "git commit -m \"Initial commit\"",
            "git branch -M main"
        ]

        if github_repository:
            commands.append(f"git remote add origin {github_repository}")
            commands.append("git push -u origin main")

        commands.append("git checkout -b develop")

        for command in commands:
            os.system(command)
            
    
    def create_structure(self, file_name, contents = None): 
        if contents is None: 
            open(file_name, "w+").close()
        
        else:
            with open(file_name, "w") as file:
                file.writelines(contents)
                file.close()