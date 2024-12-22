from aiogram import F, Bot, Dispatcher, types
from aiogram.filters import Command
from conf import token
from button import keyboard_main, MENU, genrate_menu_keybord
import asyncio
bot = Bot(token=token)
dp = Dispatcher()
@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет, я бот! Выберите то что вас интересует.",
reply_markup=keyboard_main)
@dp.message(Command("help"))
async def help(message:types.Message):

    await message.reply(" вот доступные команды: \n 1) /help - описание команд \n 2) /about - краткая информация \n 3) /menu - меню")
@dp.message(Command("about"))

async def ab(message:types.Message):

    await message.reply("Этот бот создан для добычи информации.")
@dp.message(Command("menu"))

async def help(message:types.Message):
    await message.answer("Привет, я бот! Выберите то что вас интересует.",
reply_markup=keyboard_main)

@dp.message(F.text =='Выбрать.')
async def choose_topic(message:types.Message):
    keyboard = genrate_menu_keybord()
    await message.reply("Вот, выбирайте", reply_markup=keyboard)
@dp.message(F.text == "курсы валют")
async def ans(message:types.Message):
    await message.answer("Вот нынешние курсы валют: \n Доллар = 80.00 \n Рубль = 0.80 \n Евро = 92.00")
@dp.message(F.text =="новости")
async def news(message:types.Message):
    await message.answer("Война между государствами продолжается. \n Россия угрожает ядерным оружием \n Экономика растет в среднеазиятских странах.")
@dp.message(F.text == "контактная информация")
async def con(message:types.Message):
    await message.answer("Наша почта: info@example.com. Телефон: +123456789.")
@dp.message(F.text == 'Часто Задаваемые Вопросы')
async def ask(message:types.Message):
    await message.answer("1) Для чего нужен этот бот? \n он нужен для добычи информации. \n 2) Опасен ли он? \n совсем нет.")


















async def main():
    print("Запукс Бота")
    await dp.start_polling(bot)

asyncio.run(main())
