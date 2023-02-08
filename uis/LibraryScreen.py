# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LibraryScreenUi.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListView,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_library_screen(object):
    def setupUi(self, library_screen):
        if not library_screen.objectName():
            library_screen.setObjectName(u"library_screen")
        library_screen.resize(707, 343)
        self.verticalLayout_2 = QVBoxLayout(library_screen)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(library_screen)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.list_books_list_view = QListView(library_screen)
        self.list_books_list_view.setObjectName(u"list_books_list_view")

        self.verticalLayout.addWidget(self.list_books_list_view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.update_book_button = QPushButton(library_screen)
        self.update_book_button.setObjectName(u"update_book_button")

        self.horizontalLayout.addWidget(self.update_book_button)

        self.delete_book_button = QPushButton(library_screen)
        self.delete_book_button.setObjectName(u"delete_book_button")

        self.horizontalLayout.addWidget(self.delete_book_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.register_a_new_book_button = QPushButton(library_screen)
        self.register_a_new_book_button.setObjectName(u"register_a_new_book_button")

        self.verticalLayout.addWidget(self.register_a_new_book_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(library_screen)

        QMetaObject.connectSlotsByName(library_screen)
    # setupUi

    def retranslateUi(self, library_screen):
        library_screen.setWindowTitle(QCoreApplication.translate("library_screen", u"Form", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("library_screen", u"Rechercher un livre...", None))
        self.update_book_button.setText(QCoreApplication.translate("library_screen", u"Modifier", None))
        self.delete_book_button.setText(QCoreApplication.translate("library_screen", u"Supprimer", None))
        self.register_a_new_book_button.setText(QCoreApplication.translate("library_screen", u"Enregistrer un nouveau livre", None))
    # retranslateUi

