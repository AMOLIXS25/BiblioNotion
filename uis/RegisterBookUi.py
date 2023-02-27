# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterBookUi.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_register_book_window(object):
    def setupUi(self, register_book_window):
        if not register_book_window.objectName():
            register_book_window.setObjectName(u"register_book_window")
        register_book_window.resize(598, 434)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(register_book_window.sizePolicy().hasHeightForWidth())
        register_book_window.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(register_book_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 581, 421))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.layoutWidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.title)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.search_a_book_line_edit = QLineEdit(self.layoutWidget)
        self.search_a_book_line_edit.setObjectName(u"search_a_book_line_edit")

        self.verticalLayout.addWidget(self.search_a_book_line_edit)

        self.run_search_button = QPushButton(self.layoutWidget)
        self.run_search_button.setObjectName(u"run_search_button")

        self.verticalLayout.addWidget(self.run_search_button)

        self.books_find_in_api_list_view = QListWidget(self.layoutWidget)
        self.books_find_in_api_list_view.setObjectName(u"books_find_in_api_list_view")

        self.verticalLayout.addWidget(self.books_find_in_api_list_view)

        self.register_book_in_library_button = QPushButton(self.layoutWidget)
        self.register_book_in_library_button.setObjectName(u"register_book_in_library_button")

        self.verticalLayout.addWidget(self.register_book_in_library_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        register_book_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(register_book_window)

        QMetaObject.connectSlotsByName(register_book_window)
    # setupUi

    def retranslateUi(self, register_book_window):
        register_book_window.setWindowTitle(QCoreApplication.translate("register_book_window", u"Enregistrer un nouveau livre", None))
        self.title.setText(QCoreApplication.translate("register_book_window", u"Enregistrer un livre", None))
        self.run_search_button.setText(QCoreApplication.translate("register_book_window", u"Lancer la recherche", None))
        self.register_book_in_library_button.setText(QCoreApplication.translate("register_book_window", u"Enregistrer le livre dans ma biblioth\u00e8que", None))
    # retranslateUi

