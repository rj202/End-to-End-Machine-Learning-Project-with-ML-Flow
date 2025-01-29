import os # operation system
from pathlib import Path
import logging

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s]: %(message)s'  # Formato del mensaje de logging
)

project_name ='mlproject'

# creating an folder inside of the github repository.
list_of_files=[
    '.github/workflow/.gitkeep', #.github workflow is used for cicd deployment, and the gitkeep is used for commit the folder
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
   


]
# Suponemos que list_of_files es una lista de rutas de archivos
for filepath in list_of_files:
    filepath = Path(filepath)  # Convirtiendo el archivo a un objeto Path
    filedir, filename = os.path.split(filepath)  # Separando la carpeta y el nombre del archivo

    # Crear directorio si no existe
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)  # Creando la carpeta
        logging.info(f'Creating directory: {filedir} for the file: {filename}')

    # Comprobamos si el archivo no existe o tiene tamaño 0
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass  # Crear archivo vacío
        logging.info(f'Creating empty file: {filepath}')  # Creando el archivo vacío

    else:
        logging.info(f'{filename} already exists')  # El archivo ya existe