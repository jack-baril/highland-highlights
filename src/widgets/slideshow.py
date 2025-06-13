import fitz
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from settings import DOCUMENT_DIRECTORY, SLIDE_CYCLE_INTERVAL, SLIDESHOW_DPI
from utils.directory_watcher import DirectoryWatcher
from utils.scaling import get_screen_height, get_screen_width, scale_pixmap
from utils.timer import start_timer


class Slideshow(QWidget):
    def __init__(self):
        super().__init__()
        self.pdf_file_watcher = DirectoryWatcher(
            DOCUMENT_DIRECTORY, "*.pdf", self.reload_pages
        )
        self.current_pdf = None
        self.current_slide = 0
        self.total_slides = 0
        self.pixmap_cache = {}
        self.label = QLabel()
        self.create_layout()
        self.reload_pages()
        start_timer(self, SLIDE_CYCLE_INTERVAL, self.cycle_slides)

    def create_layout(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)

    def reload_pages(self):
        latest_pdf = self.pdf_file_watcher.get_latest_file()
        if latest_pdf is not None and latest_pdf != self.current_pdf:
            self.current_slide = 0
            self.current_pdf = latest_pdf
            self.load_pages(latest_pdf)
        self.update_slide()

    def load_pages(self, pdf_path):
        with fitz.open(pdf_path) as pdf:
            self.pixmap_cache = {}
            self.total_slides = len(pdf)
            for slide in range(self.total_slides):
                page = pdf.load_page(slide)
                pixmap = Slideshow.convert_page_to_pixmap(page)
                screen_width = get_screen_width()
                screen_height = get_screen_height()
                scaled_slide = scale_pixmap(
                    pixmap, screen_width, screen_height
                )
                self.pixmap_cache[slide] = scaled_slide

    def update_slide(self):
        if self.pixmap_cache:
            current_pixmap = self.pixmap_cache[self.current_slide]
            self.label.setPixmap(current_pixmap)

    def cycle_slides(self):
        if self.total_slides > 1:
            self.current_slide = (self.current_slide + 1) % self.total_slides
            self.update_slide()

    @staticmethod
    def convert_page_to_pixmap(page):
        pixmap = page.get_pixmap(dpi=SLIDESHOW_DPI, alpha=False)
        image = QImage(
            pixmap.samples,
            pixmap.width,
            pixmap.height,
            pixmap.stride,
            QImage.Format_RGB888,
        )
        pixmap = QPixmap.fromImage(image)
        return pixmap
