import os
import shutil
from pathlib import Path

from page import Page, Section


class Build:
    def __init__(self, config):
        self.config = config

    def build(self, docs_path):
        dist_path = Path("dist")
        self.prepare_dist(dist_path)

        pages = []
        for child in docs_path.iterdir():
            if child.is_dir():
                section = Section(self.config, child)
                pages.append(section)
            else:
                if child.suffix != ".md":
                    continue
                page = Page(self.config, child)
                pages.append(page)

        for page in pages:
            page.save_html(dist_path)
            print(page.to_dict())

    def prepare_dist(self, dist_path):
        template_path = Path(os.path.realpath(__file__)).parent / "template"

        shutil.rmtree(dist_path)
        dist_path.mkdir(parents=True, exist_ok=True)

        shutil.copyfile(template_path / "style.css", dist_path / "style.css")
