# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashScreenUi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QLabel, QProgressBar,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(336, 406)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(110, 240, 131, 21))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.title_label.setFont(font)
        self.loading_progressBar = QProgressBar(self.centralwidget)
        self.loading_progressBar.setObjectName(u"loading_progressBar")
        self.loading_progressBar.setGeometry(QRect(20, 320, 291, 20))
        self.loading_progressBar.setValue(24)
        self.loading_label = QLabel(self.centralwidget)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setGeometry(QRect(120, 350, 111, 17))
        self.icon_label = QLabel(self.centralwidget)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setGeometry(QRect(50, 10, 241, 241))
        self.icon_label.setPixmap(QPixmap(u":/pic/pictures/icon_splash_screen.png"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"BiblioNotion", None))
        self.loading_label.setText(QCoreApplication.translate("MainWindow", u"Chargement ...", None))
        self.icon_label.setText("")
    # retranslateUi

