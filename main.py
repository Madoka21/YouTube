import telebot
import random
import flask
import os
from telebot import types
from pytube import YouTube

# py -m pip install pytube

token = '5466706932:AAF_Ua9V0AAPUNuZ2rRyxIHZqY9XdeEc2bs'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, 'Отправьте ссылку на видео youtube')

@bot.message_handler(content_types=['text'])
def get_video(msg):
    link = msg.text
    video = YouTube(link)
    filename = video.streams.filter(res='720p').first().default_filename
    video.streams.filter(res='720p').first().download()
    file = open(filename, 'rb')
    bot.send_video(msg.chat.id, file)
    bot.send_message(msg.chat.id, 'Приятного просмотра')

bot.polling()


# py -m pip install pytelegrambotapi
