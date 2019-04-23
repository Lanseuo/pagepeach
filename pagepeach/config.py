import yaml


class Config:
    def __init__(self, general, theme):
        self.general = general
        self.theme = theme

    @staticmethod
    def parse_yaml(filepath):
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


class ThemeConfig:
    def __init__(self, data):
        self.copyright = data.get("copyright", "")
        self.hide_created_using = data.get("hide_created_using")
        self.primary_color = data.get("primary_color", "#ffb977")
        self.header_links = data.get("header_links", [])
