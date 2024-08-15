from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass(frozen=True)
class Config:
    STRINGS_MODULE_RESUME_PATH: Path
    STRINGS_MODULE_RESUME_JOB_DESCRIPTION_PATH: Path
    STRINGS_MODULE_NAME: str
    STYLES_DIRECTORY: Path
    RESUME_TEMPLATE_PATH: Path
    OUTPUT_FILE_PATH: Path
    API_KEY: str