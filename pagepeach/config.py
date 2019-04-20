import yaml


class Config:
    def __init__(self, general):
        self.general = general

    @staticmethod
    def parse_yaml(filepath):
        with open(filepath, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return Config(
            general=GeneralConfig(data.get("general", {}))
        )


class GeneralConfig:
    def __init__(self, data):
        self.name = data.get("name")
        self.base_url = data.get("base_url", "").strip("/")
