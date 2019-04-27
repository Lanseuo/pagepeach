import os
import shutil
from pathlib import Path

from page import Page, Section
from api_reference import ApiReferencePage


class Build:
    def __init__(self, config):
        self.config = config

    def build(self, docs_path):
        dist_path = Path("dist")
        self.prepare_dist(dist_path)

        pages = []
        for child in docs_path.iterdir():
            if child.is_dir():
                item = Section(self.config, child)
            else:
                if child.suffix != ".md":
                    continue
                item = Page(self.config, child)

            pages.append(item)

        if self.config.general.enable_api_reference:
            pages.append(ApiReferencePage(self.config))

        sitemap = [p.to_nav_dict() for p in pages]
        for page in pages:
            page.save_html(dist_path, sitemap)

    def prepare_dist(self, dist_path):
        template_path = Path(os.path.realpath(__file__)).parent / "template"

        shutil.rmtree(dist_path)
        dist_path.mkdir(parents=True, exist_ok=True)

        shutil.copyfile(template_path / "style.css", dist_path / "style.css")
