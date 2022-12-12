import telebot
from telebot import types
token='5278735722:AAFr2vv8Wo_bMViUTntyGACRSgo-nWdU1AM'
import telebot

bot = telebot.TeleBot("5278735722:AAFr2vv8Wo_bMViUTntyGACRSgo-nWdU1AM") 

@bot.message_handler(content_types=['text'])
def welcome(pm):
    sent = bot.send_message(pm.chat.id, "Введите пароль")
    bot.register_next_step_handler(sent, welcome2) #Next message will call the name_handler function
def welcome2(pm):
    name = pm.text
    if name == '123456':
        def welcome1(pm):
            sent_msg = bot.send_message(pm.chat.id, "Welcome to bot. what's your name?")
            bot.register_next_step_handler(sent_msg, name_handler) #Next message will call the name_handler function
        def name_handler(pm):
            nam = pm.text
            sent_msg = bot.send_message(pm.chat.id, f"Your name is. how old are you?")
            bot.register_next_step_handler(sent_msg, age_handler, nam) #Next message will call the age_handler functio
        def age_handler(pm, nam):
            age = pm.text
            bot.send_message(pm.chat.id, f"Your name is {nam}, and your age is {age}.")
        welcome1(pm)
    else:
        bot.send_message(pm.chat.id, 'нету доступа')
bot.polling()