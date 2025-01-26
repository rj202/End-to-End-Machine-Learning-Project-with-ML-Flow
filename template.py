import os # operation system
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name ='mlproject'

list_of_files=[
    '.github/workflow/.gitkeep', # creating an folder inside of the github repository.
    f'src({project_name}/__init__.py)',
    f'src({project_name}/components/__init__.py)',
    f'src({project_name}/utils/__init__.py)',
    f'src({project_name}/utils/__init__.py)',
    f'src({project_name}/config/__init__.py)',
    f'src({project_name}/pipeline/__init__.py)',
    f'src({project_name}/entity/__init__.py)',
    f'src({project_name}/entity/config_entity.py)',
    f'src({project_name}/constants/__init__.py)',
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
    'test.py'


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # separating the folder and the function

    if filedir !='':
        os.makedirs(filedir,exist_ok=True) # creating the folder
        logging.info(f'Creating directory; {filedir} for the file: {filename}')

    if(not os.path.exists(filepath) or (os.path.getsize(filepath)== 0)):
        with open (filepath, 'w') as f:
            pass
            logging.info(f'creating empty file: {filepath}') # creating the file


    else:
        logging.info(f'{filename} is already exists')
