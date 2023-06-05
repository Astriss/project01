'''Эхо - бот'''
import telebot
bot = telebot.TeleBot('6260812558:AAESxWW0ZkhWTa6lbvngRW7AV0H5jiUBJ4s')
@bot.message_handler(commands=['start'])
def start(message):
 bot.send_message(message.chat.id, "Привет! Поболтай со мной!")

@bot.message_handler(content_types=['text'])
def handle_text(message):
 bot.send_message(message.chat.id, "Ты написал: "  + message.text)

bot.polling(none_stop=True, interval=0)

