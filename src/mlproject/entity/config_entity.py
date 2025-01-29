from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) #A @dataclass(frozen=True) makes a class immutable. Once an instance is created, its attributes cannot be changed.
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file: Path
    unzip_dir: Path
