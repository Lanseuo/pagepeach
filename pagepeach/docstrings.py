import ast
from pathlib import Path

FILENAME = Path("script.py")


class Function:
    def __init__(self, node):
        self.node = node


class Class:
    def __init__(self, node):
        self.node = node
        self.methods = self.get_methods()

    def get_methods(self):
        return [Function(subnode) for subnode in self.node.body if isinstance(subnode, ast.FunctionDef)]


def get_docstrings():
    with open(FILENAME, "r") as f:
        file_content = f.read()
    module = ast.parse(file_content)

    functions = [Function(node) for node in module.body if isinstance(node, ast.FunctionDef)]
    classes = [Class(node) for node in module.body if isinstance(node, ast.ClassDef)]


get_docstrings()
