import click
from pathlib import Path

from build import Build
from config import Config


@click.group()
def cli():
    pass


@cli.command()
def build():
    "Build your documentation"

    docs_path = Path("docs")
    config = Config.parse_yaml(docs_path / "pagepeach.yaml")

    build = Build(config)
    build.build(docs_path)
