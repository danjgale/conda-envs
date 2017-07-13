# project-envs
This repository contains files to setup virtualized environments for behavioural and/or fMRI projects. Namely, it includes conda `environment.yml` files for my typical python environments and a Dockerfile to setup a containerized fMRI environment (either via Docker or Singularity). 

## Repository Structure

`behav/`:
- conda environment for behavioural projects

`fmri/`:
- conda environment and `Dockerfile` for fMRI projects. 

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
`fmri` includes several additional libraries from the [nipy ecosystem](http://nipy.org/) (`nipy`, `nipype`, `nilearn`, `nibabel`, `nitime`) and `scikit-image` for working with fMRI data.

## Containers

A `Dockerfile` is included under `fmri/` and the image it creates can be found on DockerHub https://hub.docker.com/r/danjgale/fmri/. This bundles the conda `fmri` environment with the [Nipype image](https://hub.docker.com/r/nipype/nipype/), an install of `dcm2niix`, and adds `nano` for convenience.

Note that if you wish to convert this image to a Singularity container to run on an HPC, you cannot directly pull the image into a `Singularity` file yet (due to a [known issue with Singularity](https://github.com/singularityware/singularity/issues/719)). The current workaround requires you to run [docker2singularity](https://github.com/singularityware/docker2singularity).
