"""Main module of my application"""
import sys

from PySide6.QtWidgets import QApplication

from views.HomeScreen import HomeScreen


def load_qss_style(qss_name_file: str, app: QApplication):
    """
    Method that load qss style from a qss stylesheet file
    :param qss_name_file: Qss File Name
    :param app: App where Qss style will load
    """
    with open(qss_name_file, "r") as f:
        style: str = f.read()
        app.setStyleSheet(style)


if __name__ == '__main__':
    # Je lance ma boucle d'événement en passant les paramètres de la console
    app: QApplication = QApplication(sys.argv)
    load_qss_style("res/qss/styles.qss", app)
    test_ui = HomeScreen()
    test_ui.show()
    app.exec()
