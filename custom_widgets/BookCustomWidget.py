from PySide6 import QtCore

import requests
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap, QImage

from models.BookModel import BookModel

from res import res


class BookCustomWidget(QWidget):
    def __init__(self, book_model: BookModel, parent=None):
        """
        Book Custom Widget's constructor
        :param text_up: Text up to inject
        :param text_down: Text down to inject
        :param url_cover: Cover url to create my cover
        :param parent: Parent of my custom Widget
        """
        self.book_model = book_model
        super(BookCustomWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.text_up_label = QLabel(self.book_model.title)
        self.text_down_label = QLabel(f"{self.book_model.published_date} - {self.book_model.author_names}")
        self.textQVBoxLayout.addWidget(self.text_up_label)
        self.textQVBoxLayout.addWidget(self.text_down_label)
        self.main_layout = QHBoxLayout()
        self.thumbnail_label = QLabel()
        self.main_layout.addWidget(self.thumbnail_label, 0)
        self.main_layout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.main_layout)
        self.set_cover()

    def set_cover(self):
        """Method load the image url into the image label"""
        pixmap: QPixmap
        if self.book_model.cover is None:
            pixmap = QPixmap(u":/pic/pictures/no-cover.jpg")
        else:
            thumbnail_image = QImage()
            # Je construis mon image à partir des données de l'image récupérer via l'url internet.
            thumbnail_image.loadFromData(requests.get(self.book_model.cover).content)
            pixmap = QPixmap(thumbnail_image)
            # Je redimensionne mon image tous en gardant le ratio de mon image.
        pixmap = pixmap.scaled(40, 40, QtCore.Qt.KeepAspectRatio)
        self.thumbnail_label.setPixmap(pixmap)
