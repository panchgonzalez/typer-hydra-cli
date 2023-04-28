from setuptools import find_packages, setup

setup(
    name="hydra-app",
    packages=find_packages(include=["app"]),
    entry_points={
        "console_scripts": [
            "submit-job = app.main:submit_job",
            "job-status = app.main:job_status"
        ]
    },
    install_requires=["hydra-core"]
)