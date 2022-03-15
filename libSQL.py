from email import message
import telebot
from config import TOKEN
from lib_sql.userSQL import UserSQL
from lib_sql.authorsSQL import AuthorsSQL
from lib_sql.genereSQL import GenreSQL
from lib_sql.bookSQL import BooksSQL
from telebot import types
import mysql.connector
bot = telebot.TeleBot(token=TOKEN)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="271711hasan",
    db="chat",
    autocommit = True
)

cursor = db.cursor()

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    text = """
    Добро пожаловать в бота нашей библиотеки
    имени Ч.Айтматова.
    """
    bot.send_message(message.chat.id , text=text)
    markup = types.InlineKeyboardMarkup()
    my_cart = types.InlineKeyboardButton("Моя карточка", callback_data="my_cart")
    genres = types.InlineKeyboardButton("Жанры", callback_data="genre")
    search = types.InlineKeyboardButton("Поиск", callback_data="search")
    my_books = types.InlineKeyboardButton("Мои Книги",callback_data="my_books")
    markup.row_width = 1
    markup.add(my_cart, genres, search,my_books)

    bot.send_message(message.chat.id, text=text , reply_markup=markup)


@bot.callback_query_handler(func= lambda call: call.data=='genre')
def sand_all_genres(call):
    message = call.message
    genre_manger = GenreSQL(cursor)
    genres = genre_manger.get_all_genres()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    for (id,name) in genres:
        button = types.InlineKeyboardButton(name, callback_data=f"genre_{id}")
        markup.add(button)
    bot.edit_message_text(
        chat_id=message.chat.id, 
        text="Выберите жанр",
        message_id=message.id,
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: call.data=="my_books")
def send_user_books(call):
    message=call.message
    books_manager=BooksSQL(cursor)
    books = books_manager.get_books_info()
    markup = types.InlineKeyboardMarkup()
    for book in books:
        name = book[1]
        book_id = book[0]
        button = types.InlineKeyboardButton(
            name, 
        callback_data=f"book_{book_id}"
        )
        markup.add(button)
    markup.row_width = 2
    bot.edit_message_text(
        chat_id=message.chat.id,
        text="Выберите книгу:",
        message_id=message.id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: str(call.data).startswith('book_'))
def send_book_info(call):
    message = call.message
    book_maneger = BooksSQL(cursor)
    book = call.data.split("_")
    book_id = book[1]
    book_data = book_maneger.get_book_info(id=book_id)
    text = f"""
    Book's name: {book_data[1]}
    Author : {book_data[2]}"""

bot.infinity_polling()