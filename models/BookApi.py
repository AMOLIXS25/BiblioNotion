"""
Module that manage the book api
author: amolixs
"""
from requests import Response

import requests
from models.BookModel import BookModel


class BookApi:
    """"""

    def __init__(self):
        super(BookApi, self).__init__()
        # Ma liste de livre que je vais créer grâce au livre réupérer depuis l'api
        self.books_get_with_api: list[BookModel] = []

    @staticmethod
    def get_json_data_from_url(search_text: str):
        """
        Method that get the json data thanks to google api books with a search text
        :param search_text: The text to search a specific book
        :return data_json: The json data get from url
        """
        url_api: str = f"https://www.googleapis.com/books/v1/volumes?q={search_text}&maxResults=20&key" \
                       f"=AIzaSyBZESW5evO0JkTqVTNS8xYzfWFwD8mNqpI"
        response: Response = requests.get(url_api)
        # Je transforme ma réponse en string au format objet(json)
        data_json = response.json()
        return data_json

    def construct_list_books(self, data_json):
        """
        Method that construct the list books with the json data
        :param data_json: Data Json
        """
        # Je vide la liste de livre à chaque construction d'une nouvelle liste c'est à dire une nouvelle recherche.
        self.books_get_with_api.clear()
        for item in data_json['items']:
            published_date: str = ""
            title: str = ""
            cover: str = ""
            number_of_pages: int = 0
            isbn: str = ""
            authors: str = ""
            try:
                title = item['volumeInfo']['title']
            except KeyError:
                print("[!] Erreur aucun titre trouvé !")
            try:
                cover = item['volumeInfo']['imageLinks']['smallThumbnail']
            except KeyError:
                print("[!] Erreur aucun couverture trouvé")
            try:
                number_of_pages = int(item['volumeInfo']['pageCount'])
            except:
                print("[!] Erreur aucun nombre de pages trouvées !")
            try:
                isbn = item['volumeInfo']["industryIdentifiers"][0]['identifier']
            except:
                print("[!] Erreur aucun isbn trouvé !")
            try:
                published_date = item['volumeInfo']['publishedDate']
            except KeyError:
                print("[!] Erreur aucune date de publication trouvé !")
            try:
                for author in item['volumeInfo']['authors']:
                    if len(item['volumeInfo']['authors']) != 1:
                        authors += f"{author}, "
                    else:
                        authors += f"{author}"
            except KeyError:
                print("[!] Erreur aucun auteur trouvé !")
            new_book: BookModel = BookModel(title=title, cover=cover, author_names=authors,
                                            number_of_pages=number_of_pages, isbn=isbn, published_date=published_date)
            self.books_get_with_api.append(new_book)
