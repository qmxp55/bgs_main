#!/bin/bash

module load python/3.7-anaconda-2019.07
module unload desimodules
source /project/projectdirs/desi/software/desi_environment.sh 18.7

python select_targets_bgs.py