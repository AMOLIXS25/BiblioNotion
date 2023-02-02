from PySide6.QtWidgets import QMainWindow

from Custom_Widgets.Widgets import loadJsonStyle
from uis.TestUi2 import Ui_MainWindow


class HomeScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)