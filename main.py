import base64
import os
from pathlib import Path
import warnings
import subprocess
import sys
from typing import Type

# Define custom deprecation warnings
class CustomDeprecationWarning(DeprecationWarning):
    """Custom warning for deprecated features."""
    pass

class CustomPendingDeprecationWarning(PendingDeprecationWarning):
    """Custom pending deprecation warning."""
    pass

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)


REPO_OWNER = 'feder-cr'
REPO_NAME = 'lib_resume_builder_AIHawk'
BRANCH_NAME = 'main'
HIDDEN_DIR = os.path.expanduser('~/.my_repo_cache')
COMMIT_FILE = os.path.join(HIDDEN_DIR, 'last_commit_id.txt')

def ensure_hidden_dir_exists():
    if not os.path.exists(HIDDEN_DIR):
        os.makedirs(HIDDEN_DIR)

def get_latest_commit_id():
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/branches/{BRANCH_NAME}'
    response = requests.get(url)
    response.raise_for_status()
    branch_info = response.json()
    return branch_info['commit']['sha']

def get_saved_commit_id():
    if os.path.exists(COMMIT_FILE):
        with open(COMMIT_FILE, 'r') as f:
            return f.read().strip()
    return None

def save_commit_id(commit_id):
    ensure_hidden_dir_exists()
    with open(COMMIT_FILE, 'w') as f:
        f.write(commit_id)

def install_library():
    subprocess.check_call([sys.executable, "-m", "pip", "install", f"git+https://github.com/{REPO_OWNER}/{REPO_NAME}.git"])

def check_for_changes_and_install():
    latest_commit_id = get_latest_commit_id()
    saved_commit_id = get_saved_commit_id()

    if saved_commit_id is None:
        printred("Need lib_resume_builder_AIHawk. Auto-installing the library for the first time.")
        printred("installing...")
        install_library()
        save_commit_id(latest_commit_id)
    elif saved_commit_id != latest_commit_id:
        printred("New version of lib_resume_builder_AIHawk. Reinstalling the library.")
        install_library()
        save_commit_id(latest_commit_id)

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
    check_for_changes_and_install()
    
    from lib_resume_builder_AIHawk import Resume, StyleManager, ResumeGenerator, FacadeManager
    
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
    manager = FacadeManager(api_key, style_manager, resume_generator, resume_object, log_path)
    
    if os.path.exists("resume.pdf"):
        os.remove("resume.pdf")
    
    with open("resume.pdf", "xb") as f:
        f.write(base64.b64decode(manager.pdf_base64()))

if __name__ == "__main__":
    main()
