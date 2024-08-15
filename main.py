from email import utils
import os
from pathlib import Path
import yaml
from src.manager_facade import FacadeManager
from src.config import Config
from src.resume import Resume
from src.style_manager import StyleManager
from src.resume_generator import ResumeGenerator

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

def main():
    folder = "log"
    if not os.path.exists(folder):
        os.makedirs(folder)

    api_key = validate_secrets(Path("secrets.yaml"))
    config = Config(
        STRINGS_MODULE_RESUME_PATH=Path("resume_prompt/strings_feder-cr.py").resolve(),
        STRINGS_MODULE_RESUME_JOB_DESCRIPTION_PATH=Path("resume_job_description_prompt/strings_feder-cr.py").resolve(),
        STRINGS_MODULE_NAME="strings_feder_cr",
        STYLES_DIRECTORY=Path("resume_style").resolve(),
        RESUME_TEMPLATE_PATH=Path("plain_text_resume.yaml").resolve(),
        OUTPUT_FILE_PATH=Path("resume.html").resolve(),
        API_KEY=api_key
    )
    with open(config.RESUME_TEMPLATE_PATH, "r") as file:
        plain_text_resume = file.read()
        resume_object = Resume(plain_text_resume)
    style_manager = StyleManager()
    resume_generator = ResumeGenerator()
    manager = FacadeManager(config, style_manager, resume_generator, resume_object)
    manager.run()    

if __name__ == "__main__":
    main()