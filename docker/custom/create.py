"""Neurodocker script to create DockerFile"""

from neurodocker import Dockerfile
import sys

sys.path.append('../../envs/fmri')

def set_specs():
    specs = {
        'pkg_manager': 'apt',
        'check_urls': True,
        'instructions': [
            ('base', 'ubuntu:17.04'),
            ('install', ['git gcc']),
            ('miniconda', {
                'env_name': 'fmri',
                'conda_install': 
                    'python=3.6 numpy scipy pandas jupyter scikit-learn matplotlib pytest scikit-image',
                    'pip_install': 'nipype nibabel nilearn nitime nipy'
                    }
            ),
            ('afni', {'version': 'latest'}),
            ('ants', {'version': '2.2.0'}),
            ('freesurfer', {
                'version': '6.0.0',
                'license_path': 'rel/path/license.txt',
                'min': True
                }
            ),
            ('fsl', {'version': '5.0.10', 'use_binaries': True}),
            ('mrtrix3', {'use_binaries': False}),
            ('neurodebian', {
                'os_codename': 'zesty', 
                'download_server': 'usa-nh',
                'pkgs': ['afni', 'dcm2niix']
                }
            ),
            ('spm', {'version': '12', 'matlab_version': 'R2017a'})
        ]
    }
    return specs

if __name__ == '__main__':

    df = Dockerfile(set_specs())
    df.save('Dockerfile')
    print(df)