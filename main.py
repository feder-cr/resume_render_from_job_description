import base64
from email import utils
import os
from pathlib import Path
import yaml
from lib_resume_builder_AIHawk import Resume, StyleManager, ResumeGenerator, FacadeManager


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