#!/bin/bash
#SBATCH --array=0-383%10
#SBATCH -t 1-00:00:00
#SBATCH -n 1
#SBATCH -c 1
#SBATCH --gres=gpu:1
#SBATCH --constraint=12GB
#SBATCH --constraint=high-capacity
#SBATCH --mem=8G
#SBATCH -p gablab
#SBATCH -o run_kwyk-%A-%3a.out

set -e

source ~/.bashrc
conda activate nobrainer
#conda activate datalad_env

python3 run_kwyk.py $SLURM_ARRAY_TASK_ID


#python3 download_data.py
#python3 get_T1_list.py
#python3 run_kwyk.py
#python3 collect_T1.py 
