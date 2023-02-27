"""
Module that manage the LibraryScreen of the application
author: amolixs
"""
from PySide6.QtWidgets import QWidget
from uis.LibraryScreenUi import Ui_library_screen
from views.RegisterBookScreen import RegisterBookScreen


class LibraryScreen(QWidget, Ui_library_screen):
    """Library Screen"""
    def __init__(self):
        """Library Screen's constructor"""
        super().__init__()
        self.register_book_screen: RegisterBookScreen = RegisterBookScreen()
        self.setWindowTitle("Bibliothèque")
        self.setupUi(self)
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Method that connect all signals to slots"""
        self.register_a_new_book_button.clicked.connect(self.on_register_a_new_book_button_clicked)

    def on_register_a_new_book_button_clicked(self):
        """Method that manage register a new book button click"""
        if not self.register_book_screen.isVisible():
            self.register_book_screen.show()