#!/bin/bash
#SBATCH -c 8  # Number of Cores per Task
#SBATCH --mem=8192  # Requested Memory
#SBATCH -p gypsum-titanx  # Partition
#SBATCH -t 02:00:00  # Job time limit
#SBATCH -o slurm/setup_conda_%j.out  # %j = job ID

conda create --name 696ds -y
conda install -n 696ds pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia -y
conda install -n 696ds -c huggingface transformers -y
conda install -n 696ds ipykernel -y
python -m ipykernel install --user --name 696ds --display-name="696ds"