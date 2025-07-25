# Jupyter notebook
Jupyter debug
USEFUL LINK: https://stackoverflow.com/questions/58068818/how-to-use-jupyter-notebooks-in-a-conda-environment

```bash
# use conda to install instead of pip 
conda install jupyter
```

## Useful Commands
```bash
which jupyter
which jupyter notebook
jupyter-troubleshoot
```
Running jupyter notebook on a remote server
```bash
# remote server
jupyter notebook --ip='*' --NotebookApp.token='' --NotebookApp.password='' --no-browser --port <your_port>

# local client
ssh -N -f -L localhost:<your_port>:localhost:<your_port> <username>@<ip_address>
```

## when jupyter kernel running wrong python
check which python jupyter kernel is using
```python
import sys
print(sys.executable)
from jupyter_core.paths import jupyter_data_dir
print(jupyter_data_dir())
```

fix: install `nb_conda_kernels`
```
conda install -c conda-forge nb_conda_kernels
```

