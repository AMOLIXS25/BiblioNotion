# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeScreenUi.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(869, 528)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_container_frame = QFrame(self.centralwidget)
        self.left_container_frame.setObjectName(u"left_container_frame")
        self.left_container_frame.setMinimumSize(QSize(270, 0))
        self.left_container_frame.setMaximumSize(QSize(270, 16777215))
        self.left_container_frame.setFrameShape(QFrame.StyledPanel)
        self.left_container_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container_frame)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.left_container_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 90))
        self.frame_3.setMaximumSize(QSize(16777215, 90))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.slide_menu_container = QFrame(self.left_container_frame)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu_container.sizePolicy().hasHeightForWidth())
        self.slide_menu_container.setSizePolicy(sizePolicy)
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setGeometry(QRect(10, 10, 251, 411))
        sizePolicy.setHeightForWidth(self.slide_menu.sizePolicy().hasHeightForWidth())
        self.slide_menu.setSizePolicy(sizePolicy)
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.slide_menu_content = QFrame(self.slide_menu)
        self.slide_menu_content.setObjectName(u"slide_menu_content")
        self.slide_menu_content.setGeometry(QRect(10, 10, 231, 391))
        sizePolicy.setHeightForWidth(self.slide_menu_content.sizePolicy().hasHeightForWidth())
        self.slide_menu_content.setSizePolicy(sizePolicy)
        self.slide_menu_content.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slide_menu_content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.pushButton = QPushButton(self.slide_menu_content)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/pictures/icon_book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 32))

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.slide_menu_content)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/icons/pictures/icon_note.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(25, 32))
        self.pushButton_2.setFlat(False)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.slide_menu_content)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/icons/pictures/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(25, 32))

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.slide_menu_content)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/icons/pictures/icon_logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(25, 32))

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_2.addWidget(self.slide_menu_container)


        self.horizontalLayout.addWidget(self.left_container_frame, 0, Qt.AlignLeft)

        self.right_container_frame = QFrame(self.centralwidget)
        self.right_container_frame.setObjectName(u"right_container_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.right_container_frame.sizePolicy().hasHeightForWidth())
        self.right_container_frame.setSizePolicy(sizePolicy1)
        self.right_container_frame.setFrameShape(QFrame.StyledPanel)
        self.right_container_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.right_container_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_bar_color_frame = QFrame(self.right_container_frame)
        self.header_bar_color_frame.setObjectName(u"header_bar_color_frame")
        self.header_bar_color_frame.setMinimumSize(QSize(0, 15))
        self.header_bar_color_frame.setMaximumSize(QSize(16777215, 15))
        self.header_bar_color_frame.setFrameShape(QFrame.StyledPanel)
        self.header_bar_color_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.header_bar_color_frame, 0, Qt.AlignTop)

        self.main_content_frame = QFrame(self.right_container_frame)
        self.main_content_frame.setObjectName(u"main_content_frame")
        sizePolicy.setHeightForWidth(self.main_content_frame.sizePolicy().hasHeightForWidth())
        self.main_content_frame.setSizePolicy(sizePolicy)
        self.main_content_frame.setFrameShape(QFrame.StyledPanel)
        self.main_content_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_content_frame)


        self.horizontalLayout.addWidget(self.right_container_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Biblioth\u00e8que", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Param\u00e8tres", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
    # retranslateUi

