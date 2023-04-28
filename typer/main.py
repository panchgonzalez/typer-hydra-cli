import client

import typer

cli = typer.Typer()

@cli.command()
def submit_job(job_name: str, job_id: str):
    client.submit_job(job_name, job_id)

@cli.command()
def job_status(job_id: str):
    client.get_job_status(job_id)


if __name__ == "__main__":
    cli()