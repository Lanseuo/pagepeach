import os
import shutil
from pathlib import Path

from template import Page


class Build:
    def __init__(self, config):
        self.config = config

    def build(self, docs_path):
        dist_path = Path("dist")
        self.prepare_dist(dist_path)

        for root, dirs, files in os.walk(docs_path):
            for name in files:
                filepath = Path(root, name)
                if filepath.suffix != ".md":
                    continue

                file = File(filepath)
                file_content = file.content()

                filename = name.replace(".md", ".html")
                page = Page(self.config, file_content)
                html = page.generate_html()
                self.save_html(filename, html, dist_path)

    def prepare_dist(self, dist_path):
        template_path = Path(os.path.realpath(__file__)).parent / "template"

        shutil.rmtree(dist_path)
        dist_path.mkdir(parents=True, exist_ok=True)

        shutil.copyfile(template_path / "style.css", dist_path / "style.css")

    def save_html(self, name, html, dist_path):
        with open(dist_path / name, "w") as f:
            f.write(html)


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def content(self):
        with open(self.filepath, "r") as f:
            return f.read()
