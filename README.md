# project-envs
This repository contains environment.yml files to setup common conda environments for behavioural and/or fMRI projects. While I tend to prefer a separate environment for each and every project, I found that having several related projects always on the go resulted in multiple identical environments -- a little overkill. More so, I'm not as concerned with dependency hell for my own internal research projects, as I'm typically the sole author and the dependencies are extremely straightforward. Hence, the environments created from this repository act to streamline conda environments and prevent over-engineering.

## Environments
There are currently two environments: `behav` and `fmri`, which are for behavioural and fMRI projects, respectively. Both environments include your typical PyData stack:
  - `numpy`
  - `scipy`
  - `pandas`
  - `matplotlib`
  - `sklearn`
  - `jupyter`
As well, `pytest` is included with both environments. 

### Behav
In addition, `behav` contains some more specific libraries for statistical analysis typically required when analyzing human behavioural data collected from our experiments (namely, `statsmodels`, `seaborn`). 

### fMRI
`fmri` includes several additional libraries from the [nipy ecosystem](http://nipy.org/) (`nipy`, `nipype`, `nilearn`, `nibabel`, `nitime`). As well, there are libraries for working with Docker (`docker`, `neurodocker`) when running analyses on HPCs or the cloud.      

## Use

These environments may either be used as complete standalone environments, or as a parent for child environments. 

First, clone this repository. Then, `cd` to the directory with the desired `environment.yml` file (e.g., `cd path/to/project-envs/fmri/`). Following this, run `conda env create` to create the environment. 




