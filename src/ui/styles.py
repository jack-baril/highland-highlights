BACKGROUND_COLOR = "background-color: #101010"
CLOCK_COLOR = "color: #007c70"
SEPARATOR_COLOR = "background-color: #eb8d18"
TEXT_BODY_COLOR = "color: #cfcfcf"
TEXT_HEADER_COLOR = "color: #007c70"
FONT_FAMILY = "font-family: Nunito"
FONT_WEIGHT = "font-weight: bold"
CLOCK_FONT_SIZE = 214
DATE_FONT_SIZE = 58
SCROLLING_TEXT_FONT_SIZE = 30
TEMPERATURE_FONT_SIZE = 58
CLOCK_HEIGHT = 176
SEPARATOR_HEIGHT = 12
WEATHER_ICON_HEIGHT = 80
WEATHER_ICON_WIDTH = 80


def combine_styles(*styles):
    return "; ".join(styles)
