# SingularityAnacondaTensorflow

A simple Singularity recipe to build an image containing Anaconda3-5.2.0 (Python 3) and most recent tensorflow with GPU support on an Ubuntu 14.04 (trusty).
Uses the graphics card driver installed on the system (using Singularitys native GPU support by `--nv`)

How to use:

* download `singularity.recipe` from this repository
* install singularity (e.g. by: `sudo apt-get install singularity-container` under ubuntu)
* build container by `sudo singularity build singularity.img singularity.recipe`, this will generate a ~4.2GB singularity image
* execute container `sudo singularity shell -B /path:/path --nv singularity.img` runs the singularity image binding the folder `/path` (`-B /path:/path`) using GPU support (`--nv`)
