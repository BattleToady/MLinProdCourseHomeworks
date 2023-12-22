import wandb
import sklearn
import time

def hyperparams_tuning(model, sweep_configuration, project_name):
	sweep_id = wandb.sweep(sweep = sweep_configuration, project = project_name)
	wandb.agent(sweep_id, function=main)