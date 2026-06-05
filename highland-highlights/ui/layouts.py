from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout

from config import DATE_WEATHER_LAYOUT_CONTENT_SPACING
from ui.widgets import (
    create_clock_widget,
    create_date_widget,
    create_scrolling_text_widget,
    create_separator_widget,
    create_slideshow_widget,
    create_weather_widget,
)


class Layouts:
    @classmethod
    def create_widgets(cls):
        cls.clock_widget = create_clock_widget()
        cls.date_widget = create_date_widget()
        cls._scrolling_text_widget = create_scrolling_text_widget()
        cls._separator_widget = create_separator_widget()
        cls._slideshow_widget = create_slideshow_widget()
        cls._weather_widget = create_weather_widget()

    @classmethod
    def create_layouts(cls):
        cls._slideshow_layout = cls._create_slideshow_layout()
        cls._date_weather_layout = cls._create_date_weather_layout()
        cls._clock_date_weather_layout = cls._create_clock_date_weather_layout()
        cls._top_layout = cls._create_top_layout()
        cls.main_layout = cls._create_main_layout()

    @classmethod
    def _create_main_layout(cls):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(cls._top_layout)
        main_layout.addWidget(cls._separator_widget)
        main_layout.addLayout(cls._slideshow_layout)
        return main_layout

    @classmethod
    def _create_top_layout(cls):
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0, 0, 0, 0)
        top_layout.setSpacing(0)
        top_layout.addLayout(cls._clock_date_weather_layout, 1)
        top_layout.addWidget(cls._scrolling_text_widget, 1)
        return top_layout

    @classmethod
    def _create_clock_date_weather_layout(cls):
        clock_date_weather_layout = QVBoxLayout()
        clock_date_weather_layout.setContentsMargins(0, 0, 0, 0)
        clock_date_weather_layout.setSpacing(0)
        clock_date_weather_layout.setAlignment(Qt.AlignCenter)
        clock_date_weather_layout.addWidget(cls.clock_widget)
        clock_date_weather_layout.addLayout(cls._date_weather_layout)
        return clock_date_weather_layout

    @classmethod
    def _create_date_weather_layout(cls):
        date_weather_layout = QHBoxLayout()
        date_weather_layout.setContentsMargins(0, 0, 0, 0)
        date_weather_layout.setSpacing(DATE_WEATHER_LAYOUT_CONTENT_SPACING)
        date_weather_layout.setAlignment(Qt.AlignCenter)
        date_weather_layout.addWidget(cls.date_widget)
        date_weather_layout.addWidget(cls._weather_widget)
        return date_weather_layout

    @classmethod
    def _create_slideshow_layout(cls):
        slideshow_layout = QVBoxLayout()
        slideshow_layout.setContentsMargins(0, 0, 0, 0)
        slideshow_layout.addWidget(cls._slideshow_widget)
        return slideshow_layout
