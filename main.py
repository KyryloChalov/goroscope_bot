import os
import random

from dotenv import load_dotenv
from telebot import types, TeleBot

from include.horoscope import ZODIACS, FIRST, SECOND, SECOND_ADD, THIRD

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = TeleBot(str(TELEGRAM_BOT_TOKEN))


def rnd(text: list[str]) -> str:
    return random.choice(text)


def dialog(message) -> None:
    bot.send_message(
        message.from_user.id, "Привіт, я покажу тобі гороскоп на сьогодні."
    )
    # Створюємо клавіатуру для вибору знака зодіаку
    keyboard = types.InlineKeyboardMarkup()

    # Створюємо кнопки для кожного знака зодіаку
    for zodiac in ZODIACS:
        keyboard.add(types.InlineKeyboardButton(text=zodiac, callback_data="zodiac"))

    # Показуємо клавіатуру користувачу
    bot.send_message(
        message.from_user.id,
        text="Оберіть свій знак зодіаку",
        reply_markup=keyboard,
    )


# Обробник натискання на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call) -> None:
    # якщо натиснута кнопка з даними "zodiac"
    if call.data == "zodiac":
        # Формуємо гороскоп
        msg = f"{rnd(FIRST)} {rnd(SECOND)} {rnd(SECOND_ADD)} {rnd(THIRD)}"
        # Відправляємо текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


@bot.message_handler(content_types=["text"])
def get_text_messages(message) -> None:
    if message.text.lower() in ["привіт", "hello", "/start"]:
        dialog(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привіт'")
    else:
        bot.send_message(message.from_user.id, "Я тебе не розумію. Напиши /help.")


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
