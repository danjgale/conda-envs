# project-envs
This repository contains files to setup virtualized environments for behavioural and/or fMRI projects. Namely, it includes conda `environment.yml` files for my typical python environments and files to setup a containerized fMRI environment (either via Docker or Singularity). 

## Repository Structure

`behav/`:
- conda environment for behavioural projects

`fmri/`:
- conda environments and container files for fMRI projects. 

## Conda Environments

While I tend to prefer a separate environment for each and every project, I found that having several related projects always on the go resulted in multiple identical environments -- a little overkill. More so, I'm not as concerned with dependency hell for my own internal research projects, as I'm typically the sole author and the dependencies are extremely straightforward. Hence, the environments created from this repository act to streamline conda environments and prevent over-engineering.

There are currently two environments: `behav` and `fmri`, which are for behavioural and fMRI projects, respectively. Both environments include your typical PyData stack:
  - `numpy`
  - `scipy`
  - `pandas`
  - `jupyter`
  - `scikit-learn`
  - `matplotlib`

As well, `pytest` is included with both environments. 

These environments may either be used as complete standalone environments, or as a parent for child environments. First, clone this repository. Then, `cd` to the directory with the desired `environment.yml` file (e.g., `cd path/to/project-envs/fmri/`). Following this, run `conda env create` to create the environment. 

### behav
In addition, `behav` contains some more specific libraries for statistical analysis typically required when analyzing human behavioural data collected from our experiments (namely, `statsmodels`, `seaborn`). 

### fmri
`fmri` includes several additional libraries from the [nipy ecosystem](http://nipy.org/) (`nipy`, `nipype`, `nilearn`, `nibabel`, `nitime`) and `scikit-image` for working with fMRI data. As well, there are libraries for working with Docker (`docker`, `neurodocker`) when running analyses on HPCs or the cloud.

## Containers

A `Dockerfile` and `Singularity` file are included under `fmri/` to make portable, containerized environments in either the cloud or on an HPC, respectively. Both images import the [nipype image](https://github.com/nipy/nipype/tree/master/docker) and add some additional tools on top. 
