from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QScrollArea, QVBoxLayout, QWidget

from settings import DOCUMENT_DIRECTORY, TEXT_SCROLL_INTERVAL
from utils.directory_watcher import DirectoryWatcher
from utils.docx_to_html_converter import convert_docx_to_html
from utils.timer import start_timer


class ScrollingText(QWidget):
    def __init__(self):
        super().__init__()
        self.docx_file_watcher = DirectoryWatcher(
            DOCUMENT_DIRECTORY,
            "*.docx",
            self.update_text,
            convert_docx_to_html,
        )
        self.current_docx = None
        self.labels = ScrollingText.create_labels(self.current_docx)
        self.create_scroll_area()
        self.create_layout()
        self.update_text()
        start_timer(self, TEXT_SCROLL_INTERVAL, self.scroll_labels)

    def create_scroll_area(self):
        self.scroll_area = QScrollArea()
        self.scroll_area_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setEnabled(False)
        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.scroll_area.setStyleSheet("border: none")

    def create_layout(self):
        layout = QVBoxLayout(self)
        scroll_area_layout = QVBoxLayout(self.scroll_area_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        for label in self.labels:
            scroll_area_layout.addWidget(label)
        layout.addWidget(self.scroll_area)

    def update_text(self):
        latest_docx = self.docx_file_watcher.get_latest_file()
        if latest_docx is not None and latest_docx != self.current_docx:
            self.current_docx = latest_docx
            for label in self.labels:
                label.setText(self.current_docx)

    def scroll_labels(self):
        for i, label in enumerate(self.labels):
            label.move(0, label.y() - 1)
            other_label = self.labels[1 - i]
            if label.y() + label.height() <= 0:
                label.move(0, other_label.y() + other_label.height())

    @staticmethod
    def create_labels(text):
        labels = []
        for _ in range(2):
            label = ScrollingText.create_label(text)
            labels.append(label)
        return labels

    @staticmethod
    def create_label(text):
        label = QLabel()
        label.setText(text)
        label.setWordWrap(True)
        return label
