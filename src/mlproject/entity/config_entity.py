from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True) #A @dataclass(frozen=True) makes a class immutable. Once an instance is created, its attributes cannot be changed.
class DataIngestionConfig:
    root_dir:Path
    source_URL:str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True) #A @dataclass(frozen=True) makes a class immutable. Once an instance is created, its attributes cannot be changed.
class DataValidationConfig:
    root_dir:Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir:Path
    train_data_path:Path
    test_data_path:Path
    model_name:str
    alpha: float # this is the parameters.
    l1_ratio: float # this is the parameters.
    target_column: str # this comes from the schema 

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str