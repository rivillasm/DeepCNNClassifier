import os
from pathlib import Path  # takes care of path issues like the backware and forwared slash
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__py",
    "tests/intergration/__init__.py",
    "configs/config.yaml",
    "dvs.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory : {filedir} for file: {filename}")

    # if file does not exist or empty - then creates it
    # it makes sure to not overwrite the file if it is > 0 size
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  
        with open(filepath,"w") as f:
            pass  # creates an empty file
            logging.info(f"Creating empty file : {filepath} ")

    else:
        logging.info(f"{filename} already exists")