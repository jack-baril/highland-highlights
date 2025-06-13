from dotenv import load_dotenv
import os


load_dotenv()

APP_ICON_PATH = "assets/images/highland-hawk-logo.png"
APP_NAME = "Highland Highlights"
DOCUMENT_DIRECTORY = "assets/documents"
DOCX_XML_NAMESPACE = (
    "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
)
DOCX_BODY_COLOR_FILTER = "#222222"
DOCX_HEADER_COLOR_FILTER = "#006666"
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
REFERENCE_SCREEN_WIDTH = 1920
REFERENCE_SCREEN_HEIGHT = 1080
SLIDESHOW_DPI = 300
SLIDE_CYCLE_INTERVAL = 15000
TEXT_SCROLL_INTERVAL = 20
WEATHER_UPDATE_INTERVAL = 900000
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=gilbert"
