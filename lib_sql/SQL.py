from ast import While

from bookSQL import BooksSQL
from genereSQL import GenreSQL
from authorsSQL import AuthorsSQL

import mysql.connector
from userSQL import UserSQL
from datetime import datetime


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="271711hasan",
    db="chat",
    autocommit = True
)

cursor = db.cursor()


user_maneger = UserSQL(cursor=cursor)
genere_maneger = GenreSQL(cursor=cursor)
authors_maneger = AuthorsSQL(cursor=cursor)
book_manager = BooksSQL(cursor=cursor)
# print(book_maneger.get_books_info())

for (book_id, book_name, author_id, author_name, genre_id, genre) in book_manager.get_books_info():
    print("book_id:", book_id)
    print("book_name:", book_name)
    print("author_id:", author_id)
    print("author_name:", author_name)
    print("genre_id:", genre_id)
    print("genre:", genre)
    print("-------------------------------------------")

# print(genere_maneger.get_genre(3))
# # genere_maneger.add_new_genre("Фантастика")
# genere_maneger.delete_genre(id=5)
# print(genere_maneger.get_all_genres())
# bday = datetime(1920,1,2)
# # bday_text = bday.strftime("%Y-%m-%d")
# print(authors_maneger.get_all_authors())
# # authors_maneger.add_new_author("Рей","Бредбери",birthday=bday_text)
# print(authors_maneger.get_author(2))    

cursor.close()




