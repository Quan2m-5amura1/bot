import telebot
import random
import os
bot = telebot.TeleBot('Token')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

#@bot.message_handler(commands=['text'])
@bot.message_handler(content_types=["text"])
def create_file(message):
    path = 'C:\\'
    Folder_Name = [random.randrange(10) for i in range(5)]
    for i in range(5):
        Folder_Name[i] = str(Folder_Name[i])
    Folder_Name_1 = ''.join(Folder_Name)
    fullpath = os.path.join(path, Folder_Name_1)
    os.mkdir(fullpath)
    fullpath_1 = os.path.join(fullpath, "myfile.txt")
    myfile = open(fullpath_1, "w")
    myfile.write(message.text)
    myfile.close()
    bot.send_message(message.chat.id, Folder_Name_1)

bot.polling()