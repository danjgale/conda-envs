# ----------------------------------------------------------------------------
# Dockerfile for fMRI projects on the HPC
# Dan Gale 2017
# 
# Uses the nipype image (https://github.com/nipy/nipype/tree/master/docker)
# with some additional python libraries and a nano text editor
# ----------------------------------------------------------------------------
FROM nipype/nipype:latest

RUN conda install ipython pytest scikit-image
RUN apt-get update && apt-get install -y nano