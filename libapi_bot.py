import teleport
import pprint
import time


token = '7192308389:AAEAYs4PUbuzLwvtYl0KpH2NSzCWSa8fjU0'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=('start','help'))
def send_welcome(message):
    bot.reply_to(message,text='Как твои дела?Чем я могу помочь?')
@bot.message_handler(content_types={'sticker'})
def send_sticker(message):
    file_in = ''





@bot.message_handler(content_types='text')
def revence_text(message):
    text = message.text
    bot.reply_to(message, text)
@bot.message_handler(commands=('timer'))
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.cjat.id,i+1)

@bot.message_handler(commands={'say'})
def say(message):
    text = ' '-join(message.text.split(' ')[1:])
    bot.reply_to(message,text=f'***{text.upper()}***')


@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message,bot='Текст содержит слово плохой')
        return
    text = message.text[::1]
    bot.reply_to(message,text)
bot.polling()


