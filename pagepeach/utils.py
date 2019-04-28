import sys


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


def generate_primary_color_light(hex_color, brightness_offset=30):
    rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int]  # make sure new values are between 0 and 255
    return "#" + "".join([hex(i)[2:] for i in new_rgb_int])


def print_error(value, exit=True):
    print(f"\033[91mError: {value}\033[00m")
    if exit:
        sys.exit(1)
