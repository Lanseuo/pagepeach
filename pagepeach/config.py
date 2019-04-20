import yaml


class Config:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def parse_yaml(filepath):
        with open(filepath, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return Config(
            name=data["general"]["name"]
        )
