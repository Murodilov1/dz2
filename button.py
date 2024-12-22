from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
MENU = ['новости', 'курсы валют', 'контактная информация', 'Часто Задаваемые Вопросы']
keyboard_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Выбрать.")],
    ],
    resize_keyboard=True

) 

def genrate_menu_keybord():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=menu)] for menu in MENU ],
        resize_keyboard=True
    )