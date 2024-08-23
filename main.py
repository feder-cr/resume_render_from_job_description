import base64
import os
from pathlib import Path
import warnings
import inquirer
import requests
import yaml
import subprocess
import sys
from typing import Type
from lib_resume_builder_AIHawk import Resume, StyleManager, ResumeGenerator, FacadeManager

# Define custom deprecation warnings
class CustomDeprecationWarning(DeprecationWarning):
    """Custom warning for deprecated features."""
    pass

class CustomPendingDeprecationWarning(PendingDeprecationWarning):
    """Custom pending deprecation warning."""
    pass

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)



@staticmethod
def validate_secrets(secrets_yaml_path: Path):
    try:
        with open(secrets_yaml_path, 'r') as stream:
            secrets = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        raise Exception(f"Error reading secrets file {secrets_yaml_path}: {exc}")
    except FileNotFoundError:
        raise Exception(f"Secrets file not found: {secrets_yaml_path}")
    mandatory_secrets = ['openai_api_key']
    for secret in mandatory_secrets:
        if secret not in secrets:
            raise Exception(f"Missing secret in file {secrets_yaml_path}: {secret}")
    if not secrets['openai_api_key']:
        raise Exception(f"OpenAI API key cannot be empty in secrets file {secrets_yaml_path}.")
    return secrets['openai_api_key']

def printred(text):
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED}{text}{RESET}")

def main():  
    folder = "log"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    log_path = Path(folder).resolve()
    api_key = validate_secrets(Path("secrets.yaml"))
    
    with open("plain_text_resume.yaml", "r") as file:
        plain_text_resume = file.read()
        resume_object = Resume(plain_text_resume)
    
    style_manager = StyleManager()
    resume_generator = ResumeGenerator()
    questions = [
        inquirer.List(
            'selection',  # Nome della variabile che conterrà la scelta dell'utente
            message="What would you like to do?",  # Messaggio mostrato all'utente
            choices=['Create Resume', 'Create Resume based on Job Description URL', 'Exit']  # Scelte disponibili
        ),
    ]

    answers = inquirer.prompt(questions)
    manager = FacadeManager(api_key, style_manager, resume_generator, resume_object, log_path, selection=answers['selection'])

    
    if os.path.exists("resume.pdf"):
        os.remove("resume.pdf")
    
    with open("resume.pdf", "xb") as f:
        f.write(base64.b64decode(manager.pdf_base64()))

if __name__ == "__main__":
    main()
