"""
Module that manage the HomeScreen of the application
author: amolixs
"""

from PySide6.QtWidgets import QMainWindow, QPushButton

from Custom_Widgets.Widgets import loadJsonStyle
from dialogs.QuitDialog import QuitDialog
from uis.HomeScreenUi import Ui_MainWindow


class HomeScreen(QMainWindow, Ui_MainWindow):
    """Home Screen"""
    def __init__(self):
        QMainWindow.__init__(self)
        self.active_button_style: str = """
            border-top-left-radius: 10px;
            border-bottom-left-radius: 10px;
            border-left: 2px solid rgb(254, 206, 47);
            background-color: #292929;
        """
        # Je met en place mon ui
        self.setupUi(self)
        self.slide_menu_buttons: list[QPushButton] = [
            self.library_button,
            self.notes_button,
            self.settings_button,
            self.quit_button
        ]
        self.library_button.setStyleSheet(self.active_button_style)
        # Je charge le style json à la racine de mon projet
        loadJsonStyle(self, self)
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Method that connects all the signals to the slots"""
        self.library_button.clicked.connect(self.on_library_button_clicked)
        self.settings_button.clicked.connect(self.on_settings_button_clicked)
        self.notes_button.clicked.connect(self.on_notes_button_clicked)
        self.quit_button.clicked.connect(self.on_quit_button_clicked)

    def set_active_style_on_slide_menu_button_clicked(self, button_clicked: QPushButton):
        """Set the active style on button clicked in the slide menu"""
        for button in self.slide_menu_buttons:
            if button.objectName() == button_clicked.objectName():
                button.setStyleSheet(self.active_button_style)
            else:
                button.setStyleSheet("")

    ##################
    # MES SLOTS
    ##################

    def on_library_button_clicked(self):
        """Method that manage library button click"""
        self.set_active_style_on_slide_menu_button_clicked(self.library_button)

    def on_notes_button_clicked(self):
        """Method that manage library button click"""
        self.set_active_style_on_slide_menu_button_clicked(self.notes_button)

    def on_settings_button_clicked(self):
        """Method that manage settings button click"""
        self.set_active_style_on_slide_menu_button_clicked(self.settings_button)

    def on_quit_button_clicked(self):
        """Method that manage library button click"""
        self.set_active_style_on_slide_menu_button_clicked(self.quit_button)
        quit_dialog = QuitDialog(self)
        quit_dialog.exec()
