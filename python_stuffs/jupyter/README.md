# Jupyter notebook
Jupyter debug
## when jupyter kernel running wrong python
check which python jupyter kernel is using
```python
import sys
print(sys.executable)
from jupyter_core.paths. import jupyter_data_dir
print(jupyter_data_dir())
```

fix: install `nb_conda_kernels`
```
conda install -c conda-forge nb_conda_kernels
```