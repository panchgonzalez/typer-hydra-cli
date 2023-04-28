from setuptools import find_packages, setup

setup(
    name="typer-hydra-app",
    packages=find_packages(include=["app"]),
    entry_points={
        "console_scripts": [
            "my_app = app.main:entrypoint",
        ]
    },
    install_requires=["hydra-core"]
)