#!/bin/bash
#SBATCH --qos=regular
#SBATCH --constraint=haswell
#SBATCH --nodes=5
#SBATCH --time=12:00:00
#SBATCH --error=bs_mask.err 

module load python/3.7-anaconda-2019.07
module unload desimodules
source /project/projectdirs/desi/software/desi_environment.sh 18.7

srun python bs_mask.py --n 1.2 & 
srun python bs_mask.py --n 1.4 & 
srun python bs_mask.py --n 1.6 &
srun python bs_mask.py --n 1.8 & 
srun python bs_mask.py --n 2.0 & 
wait