# Conda useful commands
```bash
conda create --name project1 python=3.5 packages
```
```bash
conda info --envs # to see all the environments
```
```bash
source active project1 # activate project1
source deactive project1 
```
```bash
conda env remove --name project1 # remove conda environment
```
```bash
conda env create -f environment.yml # create the environment from the environment.yml file
```
```bash
conda env export > environment.yml # exporting active environment to a new file
```
```bash
conda env export --no-builds > environment.yml # export active environment to a new file w/o builds
```