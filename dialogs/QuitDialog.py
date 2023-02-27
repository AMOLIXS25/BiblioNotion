"""
Module that manage QuitDialog for confirm to quit the app
author: amolixs
"""
import sys

from PySide6.QtWidgets import QDialog
from uis.QuitDialogUi import Ui_quit_dialog


class QuitDialog(QDialog, Ui_quit_dialog):
    """Quit Dialog class"""
    def __init__(self, parent=None):
        """QuitDialog's constructor"""
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Confirmation quitter")
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Method that connect signals to slots"""
        self.yes_button.clicked.connect(self.on_yes_button_clicked)
        self.no_button.clicked.connect(self.on_no_button_clicked)

    def on_yes_button_clicked(self):
        """Manage click on yes button"""
        # Je ferme le widget parent qui à ouvert initialement la QDialog
        sys.exit()

    def on_no_button_clicked(self):
        """Manage click on no button"""
        # Je ferme la QDialog elle même
        self.close()
