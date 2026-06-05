from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget

from config import DOCUMENT_DIRECTORY, TEXT_SCROLL_INTERVAL
from utils.directory_watcher import DirectoryWatcher
from utils.docx_to_html_converter import convert_docx_to_html
from utils.timer import start_timer


class ScrollingText(QWidget):
    def __init__(self):
        super().__init__()
        self._docx_file_watcher = DirectoryWatcher(
            DOCUMENT_DIRECTORY,
            "*.docx",
            self._update_text,
            convert_docx_to_html,
        )
        self._current_docx = None
        self._labels = ScrollingText._create_labels(self._current_docx)
        self._create_scroll_area()
        self._create_layout()
        self._update_text()
        start_timer(self, TEXT_SCROLL_INTERVAL, self._scroll_labels)

    def _create_scroll_area(self):
        self._scroll_area = QScrollArea()
        self._scroll_area_widget = QWidget()
        self._scroll_area.setWidget(self._scroll_area_widget)
        self._scroll_area.setWidgetResizable(True)
        self._scroll_area.setEnabled(False)
        self._scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self._scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self._scroll_area.setStyleSheet("border: none")

    def _create_layout(self):
        layout = QVBoxLayout(self)
        scroll_area_layout = QVBoxLayout(self._scroll_area_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        for label in self._labels:
            scroll_area_layout.addWidget(label)
        layout.addWidget(self._scroll_area)

    def _update_text(self):
        latest_docx = self._docx_file_watcher.get_latest_file()
        if latest_docx is not None:
            self._current_docx = latest_docx
            for label in self._labels:
                label.setText(self._current_docx)

    def _scroll_labels(self):
        for i, label in enumerate(self._labels):
            label.move(0, label.y() - 1)
            other_label = self._labels[1 - i]
            if label.y() + label.height() <= 0:
                label.move(0, other_label.y() + other_label.height())

    @staticmethod
    def _create_labels(text):
        return [ScrollingText._create_label(text) for _ in range(2)]

    @staticmethod
    def _create_label(text):
        label = QLabel()
        label.setText(text)
        label.setWordWrap(True)
        return label
