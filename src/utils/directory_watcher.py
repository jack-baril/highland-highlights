from pathlib import Path

from PySide6.QtCore import QFileSystemWatcher


class DirectoryWatcher:
    def __init__(
        self,
        watch_directory,
        file_extension_filter,
        on_directory_update,
        on_new_file_detected=None,
    ):
        self.watch_directory = Path(watch_directory)
        self.file_extension_filter = file_extension_filter
        self.on_directory_update = on_directory_update
        self.on_new_file_detected = on_new_file_detected
        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(str(self.watch_directory))
        self.watcher.directoryChanged.connect(on_directory_update)

    def get_latest_file(self):
        files = list(self.watch_directory.glob(self.file_extension_filter))
        if not files:
            return None
        latest_file = max(files, key=lambda file: file.stat().st_mtime)
        if self.on_new_file_detected:
            return self.on_new_file_detected(latest_file)
        return latest_file
