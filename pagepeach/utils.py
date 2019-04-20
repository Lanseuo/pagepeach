def get_url(filename, config):
    if config.general.base_url == "":
        return f"/{filename}"

    return f"/{config.general.base_url}/{filename}"
