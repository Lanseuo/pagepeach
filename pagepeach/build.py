import os
from pathlib import Path


class Build:
    def __init__(self, config):
        self.config = config

    def build(self, docs_path):
        for root, dirs, files in os.walk(docs_path):
            for name in files:
                filepath = Path(root, name)
                if filepath.suffix == ".md":
                    file = File(filepath)
                    file_content = file.content()
                    print(file_content)


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def content(self):
        with open(self.filepath, "r") as f:
            return f.read()
