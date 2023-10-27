import telebot
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dosen')

#cek akses database
print(mydb)
#akses ke database
sql = mydb.cursor()
api = '5946148456:AAHPuoGQxv3Pulqf4eJgE0_73g1IPF7NAFo'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['pengunjung'])
def pengunjung(message):
    #2 input text yg akan di pisahkan mnggunakan split message
    texts = message.text.split(' ')
    print(texts)
    

print ('Telegram start running')
bot.polling()


