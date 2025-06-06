from functools import partial
import json

from PySide6.QtCore import QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWidgets import QHBoxLayout, QLabel, QWidget

from config import WEATHER_API_URL, WEATHER_UPDATE_INTERVAL
from ui.styles import WEATHER_ICON_HEIGHT, WEATHER_ICON_WIDTH
from utils.scaling import scale_dimension, scale_pixmap
from utils.timer import start_timer


class Weather(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = QNetworkAccessManager()
        self.weather_icon_label = QLabel()
        self.temperature_label = QLabel()
        self.create_layout()
        self.get_weather_data()
        start_timer(self, WEATHER_UPDATE_INTERVAL, self.get_weather_data)

    def create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.weather_icon_label)
        layout.addWidget(self.temperature_label)
        self.setLayout(layout)

    def get_weather_data(self):
        self.make_request(WEATHER_API_URL, self.process_weather_data)

    def process_weather_data(self, reply):
        weather_data = json.loads(reply.readAll().data().decode("utf-8"))
        reply.deleteLater()
        current_weather = weather_data["current"]
        self.get_weather_icon(current_weather)

    def get_weather_icon(self, current_weather):
        weather_icon_url = f"https:{current_weather['condition']['icon']}"
        self.make_request(
            weather_icon_url,
            partial(self.process_weather_icon, current_weather),
        )

    def process_weather_icon(self, current_weather, reply):
        weather_icon = reply.readAll()
        reply.deleteLater()
        pixmap = self.convert_weather_icon_to_pixmap(weather_icon)
        scaled_weather_icon = scale_pixmap(
            pixmap,
            scale_dimension(WEATHER_ICON_WIDTH),
            scale_dimension(WEATHER_ICON_HEIGHT),
        )
        self.update_weather(current_weather, scaled_weather_icon)

    def update_weather(self, current_weather, scaled_weather_icon):
        self.temperature_label.setText(f"{current_weather['temp_f']:.0f}°")
        self.weather_icon_label.setPixmap(scaled_weather_icon)

    def make_request(self, url, callback):
        request = QNetworkRequest(QUrl(url))
        reply = self.manager.get(request)
        reply.finished.connect(partial(callback, reply))

    @staticmethod
    def convert_weather_icon_to_pixmap(weather_icon):
        pixmap = QPixmap()
        pixmap.loadFromData(weather_icon)
        return pixmap
