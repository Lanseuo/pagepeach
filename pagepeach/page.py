import os
from jinja2 import Template
from pathlib import Path


class Page:
    def __init__(self, config, markdown_path):
        self.config = config
        self.markdown_path = markdown_path
        self.nav = Nav(config)

    def read(self):
        with open(self.markdown_path, "r") as f:
            return f.read()

    def generate_html(self):
        template_path = Path(os.path.realpath(__file__)).parent / "template"
        with open(template_path / "index.html", "r") as f:
            template = Template(f.read())

        return template.render(nav=self.nav, title=self.title())

    def title(self):
        return "Title"

    def get_path(self):
        return str(self.markdown_path).replace("docs/", "").replace(".md", "")

    def save_html(self, dist_path):
        html_path = Path(dist_path / (self.get_path() + ".html"))

        if "/" in self.get_path():
            folder = html_path.parent
            folder.mkdir(exist_ok=True)

        with open(html_path, "w") as f:
            f.write(self.generate_html())

    def to_dict(self):
        return {
            "type": "page",
            "title": self.title(),
            "path": self.get_path(),
            "content": self.generate_html(),
        }


class Section:
    def __init__(self, config, folder_path):
        self.config = config
        self.folder_path = folder_path
        self.children = self.get_children()

    def get_children(self):
        children = []

        for child in self.folder_path.iterdir():
            if child.suffix != ".md":
                continue
            page = Page(self.config, child)
            children.append(page)

        return children

    def title(self):
        return self.folder_path.name \
            .replace("-", " ") \
            .upper()

    def save_html(self, dist_path):
        for child in self.children:
            child.save_html(dist_path)

    def to_dict(self):
        return {
            "type": "section",
            "title": self.title(),
            "content": [p.to_dict() for p in self.children]
        }


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
