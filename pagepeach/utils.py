def get_url(filename, config):
    if config.general.base_url == "":
        return f"/{filename}"

    return f"/{config.general.base_url}/{filename}"


def get_footer_html(config):
    html = config.theme.copyright

    if not config.theme.hide_created_using:
        if html != "":
            html += " | "
        html += 'Created using <a href="" target="_blank">Pagepeach</a>'

    return html
