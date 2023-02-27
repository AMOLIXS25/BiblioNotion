"""
Module that contains the book model
author: amolixs
"""

import sqlite3


class BookModel:
    """Book class"""

    def __init__(self, title: str, cover: str, author_names: str, number_of_pages: int,
                 isbn: str, published_date: str, types: str = "", status: str = "pas commencé", evaluation: int = -1):
        """Book's constructor"""
        self.cover: str = cover
        self.title: str = title
        self.published_date: str = published_date
        self.author_names: str = author_names
        self.status: str = status
        self.types: str = types
        self.isbn: str = isbn
        self.number_of_pages: int = number_of_pages
        self.eval: int = evaluation
        self.con = sqlite3.connect("biblio.db")

    def insert_a_book_into_database(self):
        """Method that insert a new book into the database"""
        new_book = (self.title, self.cover, self.author_names, self.status, self.types, self.number_of_pages, self.isbn)
        with self.con:
            self.con.execute(
                "INSERT INTO Books(title, cover, author, status, types, pages, ISBN) VALUES (?, ?, ?, ?, ?, ?, ?)",
                new_book)
            self.con.commit()
        self.con.close()
