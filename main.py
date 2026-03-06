# from email.mime import message
import os

# Підключаємо модуль випадкових чисел
import random
import telebot
from telebot import types
from dotenv import load_dotenv
from data.goroscope import FIRST, SECOND, SECOND_ADD, THIRD
# from pathlib import types

# =======================
# Load keys from .env
# =======================
load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# FIRST = os.getenv("FIRST")
# SECOND = os.getenv("SECOND")
# SECOND_ADD = os.getenv("SECOND_ADD")
# THIRD = os.getenv("THIRD")

bot = telebot.TeleBot(str(TELEGRAM_BOT_TOKEN))

# Обробник натискання на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
  # якщо натиснута кнопка з даними "zodiac"
  if call.data == "zodiac": 
    # Формуємо гороскоп
    msg = random.choice(FIRST) + ' ' + random.choice(SECOND) + ' ' + random.choice(SECOND_ADD) + ' ' + random.choice(THIRD)
    # Відправляємо текст в Телеграм
    bot.send_message(call.message.chat.id, msg)


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "Привіт":
        bot.send_message(
            message.from_user.id, "Привіт, зараз я розкажу тобі гороскоп на сьогодні."
        )
        # Створюємо клавіатуру для вибору знака зодіаку
        keyboard = types.InlineKeyboardMarkup()
        # По черзі створюємо кнопки для кожного знака зодіаку і додаємо їх на екран
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        # Додаємо кнопку на екран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телець', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнюки', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Діва', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Ваги', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпіон', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрілець', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козоріг', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолій', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Риби', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показуємо клавіатуру користувачу
        bot.send_message(message.from_user.id, text='Оберіть свій знак зодіаку', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привіт")
    else:
        bot.send_message(message.from_user.id, "Я тебе не розумію. Напиши /help.")


bot.polling(none_stop=True, interval=0)





# # Виводимо знаки зодіаку
# print("1 - Овен")
# print("2 - Телець")
# print("3 - Близнюки")
# print("4 - Рак")
# print("5 - Лев")
# print("6 - Діва")
# print("7 - Ваги")
# print("8 - Скорпіон")
# print("9 - Стрілець")
# print("10 - Козоріг")
# print("11 - Водолій")
# print("12 - Риби")

# # Запитуємо у користувача про його знак
# zodiac = int(
#     input(
#         "{blue}Введіть число з номером знака зодіаку: {endcolor}".format(
#             blue="\033[96m", endcolor="\033[0m"
#         )
#     )
# )
# # Якщо число введено правильно — видаємо гороскоп
# if 0 < zodiac < 13:
#     print(
#         random.choice(first),
#         random.choice(second),
#         random.choice(second_add),
#         random.choice(third),
#     )
# else:
#     print("Ви помилилися з числом, запустіть програму ще раз")
