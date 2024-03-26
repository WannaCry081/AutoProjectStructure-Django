import os
import requests
import subprocess
from pathlib import Path


class AutoProjectStructure:
    
    def setup_environment(self, project_name):
        pass
    
    
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