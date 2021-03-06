import telebot
import random
import flask
import os
from telebot import types
from pytube import YouTube

# py -m pip install pytube

server = flask.Flask(__name__)

app_name = "youtubebot1234"
token = '5315904167:AAGRl-txzHs9lKvWcZ4en-57ld3heO82O-o'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Дароу, введи существующую ссылку YouTube')

@bot.message_handler(content_types=['text'])
def get_video(msg):
    bot.send_message(msg.chat.id, "Секунду, обрабатываю ваш запрос. Видео будет доступно в течении пару секунд или минут в зависимости от продолжительности видео")
    link = msg.text
    video = YouTube(link)
    filename = video.streams.filter(res='720p').first().default_filename
    video.streams.filter(res='720p').first().download()
    file = open(filename, 'rb')
    bot.send_video(msg.chat.id, file)
    bot.send_message(msg.chat.id, 'Держи! Я молодец, а ты никто!')

@server.route('/' + token, methods=['POST'])

def get_message():
      bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
      return "!", 200

@server.route('/', methods=["GET"])

def index():
    print("hello webhook!")
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{app_name}.herokuapp.com/{token}")
    return "Hello from Heroku!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

# py -m pip install pytelegrambotapi
