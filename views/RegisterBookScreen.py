"""Module that manage Register book Screen"""
from PySide6.QtWidgets import QMainWindow, QLabel, QListWidgetItem

from custom_widgets.BookCustomWidget import BookCustomWidget
from models.BookApi import BookApi
from uis.RegisterBookUi import Ui_register_book_window


class RegisterBookScreen(QMainWindow, Ui_register_book_window):
    """Register Book Screen class"""
    def __init__(self):
        """Register Book Screen's constructor"""
        super().__init__()
        self.setupUi(self)
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        """Connect all signals to slots"""
        self.run_search_button.clicked.connect(self.on_run_search_button_clicked)
        self.register_book_in_library_button.clicked.connect(self.on_register_book_in_library_button_clicked)

    def on_run_search_button_clicked(self):
        """Method that manage the search button click"""
        self.books_find_in_api_list_view.clear()
        book_api: BookApi = BookApi()
        book_api.construct_list_books(book_api.get_json_data_from_url(self.search_a_book_line_edit.text()))
        for book in book_api.books_get_with_api:
            new_book_custom_widget: BookCustomWidget = BookCustomWidget(book)
            list_widget_item: QListWidgetItem = QListWidgetItem(self.books_find_in_api_list_view)
            list_widget_item.setSizeHint(new_book_custom_widget.sizeHint())
            self.books_find_in_api_list_view.addItem(list_widget_item)
            self.books_find_in_api_list_view.setItemWidget(list_widget_item, new_book_custom_widget)

    def on_register_book_in_library_button_clicked(self):
        """Method that manage the register book click"""
        current_list_widget_item_selected: QListWidgetItem = self.books_find_in_api_list_view.currentItem()
        book_custom_widget_selected: BookCustomWidget = self.books_find_in_api_list_view.itemWidget(current_list_widget_item_selected)
        book_custom_widget_selected.book_model.insert_a_book_into_database()