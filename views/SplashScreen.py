"""Module that manage the SplashScreen"""
from PySide6.QtCore import QRect, QTimer
from PySide6.QtGui import Qt, QScreen
from PySide6.QtWidgets import QMainWindow, QApplication

from uis.SplashScreenUi import Ui_MainWindow


class SplashScreen(QMainWindow, Ui_MainWindow):
    """SplashScreen of the application"""

    def __init__(self):
        """SplashScreen's constructor"""
        super().__init__()  # Je fais appel au constructor de la classe parent
        self.setupUi(self)
        self.counter_loading: int = 40
        self.timer: QTimer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)
        self.counter_loading_max: int = 100
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.center_splash_screen()
        
    def center_splash_screen(self):
        """Method that center the SplashScreen on the Screen"""
        available_screen_size: QRect = QScreen.availableGeometry(QApplication.primaryScreen())
        pos_center_x: int = (available_screen_size.width() - self.width()) / 2
        pos_center_y: int = (available_screen_size.height() - self.height()) / 2
        self.move(pos_center_x, pos_center_y)

    def loading(self):
        """Method that create the loading of the progressBar"""
        self.loading_progressBar.setValue(self.counter_loading)
        if self.counter_loading >= 100:
            self.timer.stop()
            self.close()
        self.counter_loading += 1
