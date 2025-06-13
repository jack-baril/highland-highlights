from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QWidget

from settings import APP_ICON_PATH, APP_NAME, BACKGROUND_COLOR
from ui.layouts import Layouts


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        Layouts.create_widgets()
        Layouts.clock_widget.date_changed.connect(
            Layouts.date_widget.update_date
        )
        Layouts.create_layouts()
        self.create_central_widget()
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(APP_ICON_PATH))
        self.setCursor(Qt.BlankCursor)

    def create_central_widget(self):
        central_widget = QWidget(self)
        central_widget.setLayout(Layouts.main_layout)
        self.setCentralWidget(central_widget)
        self.setStyleSheet(BACKGROUND_COLOR)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape and self.isFullScreen():
            self.setWindowState(self.windowState() & ~Qt.WindowFullScreen)
        if event.key() == Qt.Key_F11:
            self.setWindowState(self.windowState() ^ Qt.WindowFullScreen)
