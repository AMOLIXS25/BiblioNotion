"""
Module that manage the LibraryScreen of the application
author: amolixs
"""
from PySide6.QtWidgets import QWidget

from Custom_Widgets.Widgets import loadJsonStyle
from uis.LibraryScreenUi import Ui_library_screen


class LibraryScreen(QWidget, Ui_library_screen):
    """Library Screen"""
    def __init__(self):
        """Library Screen's constructor"""
        super().__init__()
        self.setWindowTitle("Bibliothèque")
        self.setupUi(self)