# Debug your Cuda errors without having to install Cuda and Cudnn in your host machine
The general rule of thumb is avoid installing cuda and cudnn binaries into your host machine but install them in your docker or conda environment. 

The host machine should only have the latest nvidia driver, as they are known to be backwards compatitble to a certain extend, installed without any cuda or cudnn binaries.

This would allow the host machine to support multiple requirements. e.g. running a project with different cuda version requirements


##  Some cuda or cudnn binaries not found.
Ideally, installing your cuda or cudnn binaries in your docker or conda environment would lead to python packages, such as pytorch or tensorflow to automatically search for them in your installed directories.
This however is not the case for paddle paddle (pull request maybe?). A simple fix is to export the paths as such

```bash
export LD_LIBRARY_PATH=<directory of your cuda installation>:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=<directory of your cudatoolkit installation>:$LD_LIBRARY_PATH
# e.g.
export LD_LIBRARY_PATH=/home/common/miniconda3/pkgs/cudnn-7.6.5-cuda10.2_0/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/common/miniconda3/pkgs/cudatoolkit-10.2.89-hfd86e86_1/lib:$LD_LIBRARY_PATH
```
