# CLIs with Typer and Hydra

[Blog post](https://blog.panch.io/building-robust-clis-with-typer-and-hydra-a51a5b68969e)

### Usage

**Typer CLI Example**

```
cd typer

python main.py my_job_name my_job_id
```

**Hydra App Example**

```
cd hydra

pip install -e .

submit-job job_name=my_job_name job_id=my_job_id
```

**Typer + Hydra App Example**

```
cd typer_hydra_cli

pip install -e .

my_app submit-job job_name=my_job_name job_id=my_job_id
```