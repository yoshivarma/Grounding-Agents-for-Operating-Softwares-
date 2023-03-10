# Grounding-Agents-for-Operating-Softwares

## Environment

### Install environment
Currently I'm using a conda environment for this project. In the main directory, you can find the file `environment.yml` which contains all the packages that are needed for this project. To create the environment, you can run the following command:

```bash
conda env create -n 696ds -f environment.yml 
```
This will create a conda environment called `696ds`.
It will take a while to install all the packages (took me over 20 mins).

### Activate environment

To activate the conda environment use
```bash
conda activate 696ds
```

### Add environment to jupyter notebook

To add the environment to jupyter notebook, you can run the following command (Requires the environment to be activated):

```bash
python -m ipykernel install --user --name 696ds --display-name "696ds"
```

## Running Models

The following setup was sufficient for running the xl model:
- Partition: TitanX
- CPU Threads: 4
- Memory: 40(GB)
- GPU: 1
