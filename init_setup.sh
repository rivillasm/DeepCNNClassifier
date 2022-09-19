echo [$(date)]: "START"
echo [$(date)]: "Creating Env with Python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activating Env"
source activate ./env
echo [$(date)]: "Installing Requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "end"