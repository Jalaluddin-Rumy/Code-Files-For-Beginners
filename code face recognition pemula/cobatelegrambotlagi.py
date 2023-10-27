import telebot

api = '5946148456:AAHPuoGQxv3Pulqf4eJgE0_73g1IPF7NAFo'
bot = telebot.TeleBot(api)

user = ' Jalaluddin 32601700004 '
@bot.message_handler(commands=['start'])
def action_start(message):
    no_id = str(message.from_user.id)
    if no_id in user:
        bot.reply_to(message, 'User terdeteksi')
    else:
        bot.reply_to(message,'''
        Anda tidak punya hakk..!!
        Hanya user tertentu saja yang masuk ruangan''')
    
print ('Telegram start running')
bot.polling()


