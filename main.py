import os
import requests
from pathlib import Path
                
    
def verify_github_repository(link):
    response = requests.get(link)
    return response.status_code == 200


def main():
    project = AutoProjectStructure()    
    github_repository = ""
    
    while True:
        print("""
              -------------------------
                AutoProjectStructure 
                  by @WannaCry081
              -------------------------
              
              - Monolithic Architecture
              - Public Repository only           
              """)
        
        project_name = input("Enter Project Name: ").strip()
        project_name = project_name.replace(" ", "-")
        project_dir = os.getcwd() + rf"\\{project_name}"
        
        try:
            Path.mkdir(project_name, exist_ok=False)
            os.chdir(project_name)
            
            while True:
                is_ok = input("Would you like to add a Repository [y/n]: ").lower()
                
                if is_ok == "n": 
                    break
                
                if is_ok == "y":
                    
                    while True:
                        github_repository = input("Enter GitHub Repository Link: ").strip()
                        
                        if not verify_github_repository(github_repository) and github_repository.endswith(".git"):
                            print(f"{github_repository} does not exists.")
                        else: 
                            break
                        
                    break
                
            os.chdir(project_dir)
            print(f"\nCreating '{project_name}' directory...")
            
            project.setup_environment(project_name)
            project.setup_project()
            project.setup_version_control(github_repository)
            
            print(f"""
                  -----------------------------------------------
                  Successfully created '{project_name}' directory. 
                        Happy Hacking! by @WannaCry081
                  -----------------------------------------------
                  """)
            break
                
        except FileExistsError as e:
            print(f"Directory already exists.")
        
        except FileNotFoundError as e:
            is_exit = input("Press 'q' to exit: ").lower()
            if is_exit == 'q':
                break
            
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
    input()