import yaml
from pathlib import Path

import utils


class Config:
    def __init__(self, general, theme):
        self.general = general
        self.theme = theme

    @staticmethod
    def parse_yaml(filepath):
        if not filepath.exists():
            utils.print_error(
                "Unable to find the config file. Pagepeach needs a config file called 'docs/pagepeach.yaml' to proceed."
            )
            raise FileNotFoundError("Unable to find the config file")
        with open(filepath, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return Config(
            general=GeneralConfig(data.get("general", {}) or {}),
            theme=ThemeConfig(data.get("theme", {}) or {})
        )


class GeneralConfig:
    def __init__(self, data):
        self.name = data.get("name")
        self.base_url = data.get("base_url", "").strip("/")
        self.enable_api_reference = data.get("enable_api_reference", False)
        self.dist_path = Path(data.get("dist_path", "docs/dist"))


class ThemeConfig:
    def __init__(self, data):
        self.copyright = data.get("copyright", "")
        self.hide_created_using = data.get("hide_created_using")
        self.primary_color = data.get("primary_color", "#ffb977")
        self.header_links = data.get("header_links", [])
