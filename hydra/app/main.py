import client

import hydra
from omegaconf import DictConfig


@hydra.main(config_path="conf", config_name="config")
def submit_job(cfg: DictConfig):
    client.submit_job(cfg.job_name, cfg.job_id)


@hydra.main(config_path="conf", config_name="config")
def job_status(cfg: DictConfig):
    client.get_job_status(cfg.job_id)