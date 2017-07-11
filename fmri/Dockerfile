# ----------------------------------------------------------------------------
# Dockerfile for fMRI projects on the HPC
# Dan Gale 2017
# 
# Uses the nipype image (https://github.com/nipy/nipype/tree/master/docker)
# with some additional python libraries and a nano text editor
# ----------------------------------------------------------------------------
FROM nipype/nipype:latest

# add nano for convenience
RUN apt-get update && apt-get install -y nano 

# ------------------------
# Setup python environment
# ------------------------ 

COPY environment.yml .
RUN conda env create