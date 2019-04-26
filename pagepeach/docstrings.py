import ast
from pathlib import Path

FILENAME = Path("script.py")


def get_docstrings():
    with open(FILENAME, "r") as f:
        file_content = f.read()

    module = ast.parse(file_content)
    functions = [node for node in module.body if isinstance(node, ast.FunctionDef)]

    for function in functions:
        print("---")
        print(str(FILENAME) + "::" + function.name)
        print(ast.get_docstring(function))

    print("---")


get_docstrings()
