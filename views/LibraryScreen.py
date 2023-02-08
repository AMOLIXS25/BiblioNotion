"""
Module that manage the LibraryScreen of the application
author: amolixs
"""
from PySide6.QtWidgets import QWidget

from uis.LibraryScreen import Ui_library_screen


class LibraryScreen(QWidget, Ui_library_screen):
    """Library Screen"""
    def __init__(self):
        """Library Screen's constructor"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bibliothèque")
