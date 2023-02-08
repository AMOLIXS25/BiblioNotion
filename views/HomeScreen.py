"""
Module that manage the HomeScreen of the application
author: amolixs
"""

from PySide6.QtWidgets import QMainWindow

from Custom_Widgets.Widgets import loadJsonStyle
from dialogs.QuitDialog import QuitDialog
from uis.HomeScreenUi import Ui_MainWindow


class HomeScreen(QMainWindow, Ui_MainWindow):
    """Home Screen"""
    def __init__(self):
        QMainWindow.__init__(self)
        # Je met en place mon ui
        self.setupUi(self)
        # Je charge le style json à la racine de mon projet
        loadJsonStyle(self, self)
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Method that connects all the signals to the slots"""
        self.quit_button.clicked.connect(self.on_quit_button_clicked)

    def on_quit_button_clicked(self):
        """Method that manage quit button click"""
        quit_dialog = QuitDialog(self)
        quit_dialog.exec()
