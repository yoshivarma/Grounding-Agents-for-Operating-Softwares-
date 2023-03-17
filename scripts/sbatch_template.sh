#!/bin/bash
#SBATCH -c 8  # Number of Cores per Task
#SBATCH --mem=40GB  # Requested Memory
#SBATCH -p gypsum-titanx  # Partition
#SBATCH -t 02:00:00  # Job time limit
#SBATCH -G 1  # Number of GPUs per Task
#SBATCH -o slurm/setup_conda_%j.out  # %j = job ID

python test.py

# srun --mem=50GB -G 1 --time=02:00:00 --partition=gypsum-titanx -c 8 --pty bash