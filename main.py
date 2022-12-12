from email import message
from random import random
from time import sleep
from matplotlib.pyplot import text
import telebot
from telebot import types
bot = telebot.TeleBot("5278735722:AAFr2vv8Wo_bMViUTntyGACRSgo-nWdU1AM")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
# Homework1 = open('liquid.txt')
# Homework = (Homework1)
# global Homework
# bot.send_message(call.message.chat.id, Homework)
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Меню')
    keyboard.row('Пока')
    keyboard.row('Текст')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'меню':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='1', callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='2', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='Беседа',url='https://t.me/', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='Отзывы',url='https://t.me/', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='Написать продавцу', callback_data=5))
        switch = types.InlineKeyboardButton(text='выбрать чат', switch_inline_query='/start')
        markup.add(switch)
        bot.send_message(message.chat.id, text="Выберите ==>> Нажмите : ", reply_markup=markup)
        
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Ну пока!')
    elif message.text.lower() == 'текст':
        def welcome(pm):
            sent = bot.send_message(pm.chat.id, "Введите пароль")
            bot.register_next_step_handler(sent, welcome2) #Next message will call the name_handler function
        def welcome2(pm):
            name = pm.text
            if name == '123456':
                def welcome1(pm):
                    sent_msg = bot.send_message(pm.chat.id, "Напишите текст для изменения 1")
                    bot.register_next_step_handler(sent_msg, name_handler) #Next message will call the name_handler function
                def name_handler(pm):
                    nike = pm.text
                    with open('liquid.txt', 'w') as FILE:
                        FILE.write(nike)
                        # FILE.close()
                    sent_msg = bot.send_message(pm.chat.id, "Введите текст для 2")
                    bot.register_next_step_handler(sent_msg, age_handler, nike) #Next message will call the age_handler function
                def age_handler(pm, nike):
                    age = pm.text
                    with open('evaporators.txt', 'w') as FILE:
                        FILE.write(age)
                        FILE.close()
                        print(f'{nike}')
                    bot.send_message(message.chat.id, 'готово')
                welcome1(message)
            else:
                bot.send_message(message.chat.id, 'нету доступа')
        welcome(message)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    # bot.answer_callback_query(callback_query_id=call.id, text='дк')
    if call.data == '1':
        with open('liquid.txt', 'r') as FILE:
            doc = FILE.read()
            bot.send_message(call.message.chat.id, doc)
    elif call.data == '2':
        with open('evaporators.txt', 'r') as FILE:
            doc = FILE.read()
            bot.send_message(call.message.chat.id, doc)
    elif call.data == '5':
        bot.send_message(call.message.chat.id, '@777')
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling()



