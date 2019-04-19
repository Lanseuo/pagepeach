import os
from jinja2 import Template
from pathlib import Path


class Page:
    def __init__(self, config, content):
        self.config = config
        self.content = content
        self.nav = Nav(config)

    def generate_html(self):
        template_path = Path(os.path.realpath(__file__)).parent / "template"
        with open(template_path / "index.html", "r") as f:
            template = Template(f.read())
        return template.render(nav=self.nav, title=self.title())

    def title(self):
        return "Title"


class Nav:
    def __init__(self, config):
        self.config = config
        self.title = "Title"
        self.link_sections = [
            {
                "title": "First",
                "links": [
                    {"title": "A", "href": "/a"},
                    {"title": "A", "href": "/a"},
                    {"title": "A", "href": "/a"}
                ]
            },
            {
                "title": "Second",
                "links": [
                    {"title": "A", "href": "/a"},
                    {"title": "A", "href": "/a"},
                    {"title": "A", "href": "/a"}
                ]
            }
        ]
