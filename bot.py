import telebot

bot = telebot.TeleBot("2003887609:AAElRCk9cM0RhvVEsXfV4LlVM7b8vQmFTF4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()