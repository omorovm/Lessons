import telebot
from telebot import types

bot = telebot.TeleBot("6790757803:AAGHcC5pAQDMR0SDnGEpOcrdRuT5c0Z-bJQ")

keyboard = types.ReplyKeyboardMarkup()

button = types.KeyboardButton("Game")

keyboard.add(button)

@bot.message_handler(commands=["start", "hi"])
def start_message(message):
    bot.send_message(message.chat.id, "good techer!!!", reply_markup=keyboard)
    bot.register_next_step_handler(message, func)

def func(message):
    if message.text == "Game":
        bot.send_message(message.chat.id, "Now we Go again")
    else:
        bot.send_message(message.chat.id, "Nooooooooooooo")

@bot.message_handler(content_types=['sticker'])
def echo_all(message):
    bot.reply_to(message, message.sticker_file_id)
    bot.send_message(message.chat.id, message.text)
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEKqmJlQ6Ff55ubmGdAvfnd09EjWU4smAACfBIAAvGYMUunL614YVTCCDME")


bot.polling()