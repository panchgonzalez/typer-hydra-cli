from typing import Optional, List

import typer
from hydra import compose, initialize
from hydra.utils import to_absolute_path, get_original_cwd
from hydra.core.utils import configure_log
from hydra.core.hydra_config import HydraConfig
from omegaconf import DictConfig

from . import client

cli = typer.Typer()

# def _compose(config_name: str, overrides: Optional[List[str]]) -> DictConfig:
#     original_cwd, cwd = set_workdir()
#     with initialize(version_base=None, config_path="conf"):
#         cfg = compose(
#             config_name=config_name, overrides=overrides, return_hydra_config=True
#         )
#         cfg.cwd = cwd
#         cfg.original_cwd = original_cwd
#         cfg.hydra.runtime.output_dir = cwd  # Used for logging
#         # Makes cfg interpolation usable outside context
#         # https://github.com/facebookresearch/hydra/issues/2017#issuecomment-1254220345
#         HydraConfig.instance().set_config(cfg)
#         configure_log(cfg.hydra.job_logging)
#         return cfg

def _compose(config_name: str, overrides: Optional[List[str]]) -> DictConfig:
    with initialize(config_path="conf"):
        cfg = compose(
            config_name=config_name, overrides=overrides, return_hydra_config=True
        )
        # # Makes cfg interpolation usable outside context
        # # https://github.com/facebookresearch/hydra/issues/2017#issuecomment-1254220345
        # HydraConfig.instance().set_config(cfg)
        # configure_log(cfg.hydra.job_logging)
        return cfg

@cli.command()
def submit_job(overrides: Optional[List[str]] = typer.Argument(None)):
    cfg = _compose(config_name="config", overrides=overrides)
    client.submit_job(cfg.job_name, cfg.job_id)


@cli.command()
def job_status(overrides: Optional[List[str]] = typer.Argument(None)):
    cfg = _compose(config_name="config", overrides=overrides)
    client.get_job_status(cfg.job_id)

def entrypoint():
    cli()