from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Услуги"))
main_menu.add(KeyboardButton("Задать вопрос"))
main_menu.add(KeyboardButton("Отправить заявку"))
main_menu.add(KeyboardButton("На главную")) 
