import telebot
import xlrd
import random
import requests
import codecs
from telebot import types
import sqlite3
from telebot import apihelper
apihelper.proxy = {'http':'http://192.168.0.1:3128',
                   'https':'http://192.168.0.1:3128'}
loc = ("D:\PYTHON\dcu-location\Geo-10242.xls")
bot = telebot.TeleBot('5097552028:AAE6KEZRgvBCVNlMnn-x9f1mj18VshMaFHA')
print ('ishga tushdi')



@bot.message_handler(commands=['start'])

def start (message):
    bot.reply_to(message,"Salom , {0.first_name}\nASKUE bo'limining LOKATSIYA botiga XUSH kelibsiz😉\nSiz bu bot orqali Konsentratorlarning \njoylashgan joyini aniqlashingiz mumkin\nBuning uchun konsentrator raqamini kiriting👇".format(message.from_user),parse_mode='html')
    
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#@bot.message_handler(commands=['command1'])
#def start(message):
    #message = "."
    #chats =[1489327500]
    #for chat in chats:
    #chats= analytics
    #bot.send_message(text= chats)
        


@bot.message_handler(commands=['now'])
def stat(message):
    # Opening a file
    test = open("test.txt","r",encoding='latin-1')    
    Counter = 0
    # Reading from file
    Content = test.read()
    CoList = Content.split("\n")
    for i in CoList:
        if i:
            Counter +=1
            #word = (len(CoList))
    
    test.close()
    print(Counter)
    messageStat = '👤 BOT FOYDALANUVCHILARI SONI: '+str(Counter)+' 🔝 '+'\nIshonchingiz uchun rahmat'
    bot.send_message(message.chat.id, messageStat, parse_mode='HTML')    
@bot.message_handler(content_types=["text"])

def get_text_messages(message):
    test=open('test.txt', 'a' ,encoding='UTF-8')
    test.write(str(message.chat.id)+ " " + (message.chat.first_name) +" " + (message.text)+"\n")
    meter = message.text
    rowa = 1
    cola = 4
    for row in range(sheet.nrows): 
        if meter == sheet.cell_value(row,0):
            for col in range(sheet.row_len(row)):
                print (str(sheet.cell_value(row,col)))
                rowa = row
                cola = col    
    messageText = '🏢 Hudud nomi : '+sheet.cell_value(rowa,5)+'\n🏭 Podstansiya : '+sheet.cell_value(rowa,3)+'\n🗼 Fider : '+sheet.cell_value(rowa,4)+'\n📌 TP raqami : '+sheet.cell_value(rowa,6)+'\n🟡 Balans raqami : '+sheet.cell_value(rowa,7)+'\n🔋 Quvvati : '+str(sheet.cell_value(rowa,8))+'\nLokatsiya 📍'
    bot.send_message(message.chat.id, messageText, parse_mode='HTML')
    bot.send_location(message.chat.id, latitude=sheet.cell_value(rowa,1) , longitude=sheet.cell_value(rowa,2))
        
bot.polling(none_stop=True)
