# Managing the end-to-end machine learning lifecycle with MLFlow

This Repository contains the resources for my tutorial **"Managing the end-to-end machine learning lifecycle with MLFlow"** at pyData/pyCon Berlin 2019.

# Basic setup

## Setup the environment
- clone this repository
- **with virtualenv (recommended)**
  - install virtualenv: `pip install virtualenv`
  - create a new environment: `virtualenv mlflow_tutorial`
  - activate the environment: `source /mlflow_tutorial/bin/activate`
  - run `pip install -r requirements.txt`
  
- **with pipenv** 
  - install pipenv: `pip install pipenv`
  - run `pipenv install` in the directory of the Pipfile
  - activate the environment by `pipenv shell`

## The notebook
- Get the `hands_on_example.ipynb`
- run `jupyter notebook`

# Advanced setup

## Setup the environment
- install postgresql: `sudo apt-get install postgresql postgresql-contrib postgresql-server-dev-all`

# Notes
## Run Tracking Server
```bash
mlflow server --backend-store-uri mlruns/ --default-artifact-root mlruns/ --host 0.0.0.0 --port 8000
```

## Running MLFlow project

Specify the entrypoint for this project by creating a MLproject file and adding an conda environment with a conda.yaml. You can copy the yaml file from the experiment logs.

To run this project, invoke mlflow run . -P alpha=0.42. After running this command, MLflow runs your training code in a new Conda environment with the dependencies specified in conda.yaml.
```bash
mlflow run . -P alpha=0.42
```

## Deply