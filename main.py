import telebot
import random

#API ключ бота
bot = telebot.TeleBot('5284328035:AAHvyuNsUgqF6VQHVFI4zXQRwR5CAtsbZ_I')

#загрузка фотографий
photo1 = open("1.jpg", "rb")
photo2 = open("2.jpg", "rb")
photo3 = open("3.jpg", "rb")
photo4 = open("4.jpg", "rb")
photo5 = open("5.jpg", "rb")


#photos_first = [telebot.types.InputMediaPhoto(photo1), telebot.types.InputMediaPhoto(photo2), telebot.types.InputMediaPhoto(photo3), telebot.types.InputMediaPhoto(photo4), telebot.types.InputMediaPhoto(photo5)]
#photos_second = [telebot.types.InputMediaPhoto(photo1), telebot.types.InputMediaPhoto(photo2), telebot.types.InputMediaPhoto(photo3), telebot.types.InputMediaPhoto(photo4), telebot.types.InputMediaPhoto(photo5)]

#Начало использования бота
@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, <b><u>{message.from_user.first_name} {message.from_user.last_name}</u></b>, рады Вас видеть! \n Если Вам будет что-то не понятно, пожалуйста, обратитесь к администратору, Вам ответят так быстро, как только смогут."
    marcup = telebot.types.ReplyKeyboardMarkup()
    website = telebot.types.KeyboardButton('сайт')
    price = telebot.types.KeyboardButton('цены')
    registration = telebot.types.KeyboardButton('регистрация')
    examples = telebot.types.KeyboardButton("примеры работ")
    admin = telebot.types.InlineKeyboardButton("администатор")
    marcup.add(website, price, registration, examples, admin)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=marcup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, f"Привет, <b><u>{message.from_user.first_name}</u></b>, рад тебя видеть!", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Вот твой id: <u>{message.from_user.id}</u>", parse_mode='html')
    else:
        bot.delete_message(message.chat.id, message.id)
        if message.text == "Анекдот" or message.text == "Анек":
            #a = random(1,2)
            #if a == 1:
                bot.send_message(message.chat.id, "Как озадачить панка? \nПредложить ему принять грязевую ванну.", parse_mode='html')
            #elif a == 2:
             #   bot.send_message(message.chat.id, f"Вот твой id: <u>{message.from_user.id}</u>", parse_mode='html')
        elif message.text == "сайт":
            marcup = telebot.types.InlineKeyboardMarkup()
            marcup.add(telebot.types.InlineKeyboardButton("посетить веб сайт", url="site.skal-tur-bez.h1n.ru"))
            #main = types.InlineKeyboardButton("меню")
            bot.send_message(message.chat.id, "Что бы перейти на сайт нажмите на кнопку", reply_markup=marcup)
        elif message.text == "цены":
            marcup = telebot.types.InlineKeyboardMarkup()
            marcup.add(telebot.types.InlineKeyboardButton("цены", url="https://docs.google.com/document/d/1dRmjRQQCAZoeQogxQhUIoxf96l-4lTSN/edit?usp=sharing&ouid=102902808486600263780&rtpof=true&sd=true"))
            #main = types.InlineKeyboardButton("меню")
            bot.send_message(message.chat.id, "Нажмите на кнопку, что бы посмотреть цены.", reply_markup=marcup)
        elif message.text == "регистрация":
            marcup = telebot.types.ReplyKeyboardMarkup()
            time = telebot.types.InlineKeyboardButton("время", url="https://docs.google.com/spreadsheets/d/1k-HcnYFm-cuXTLAGWcMQ8t0SBVgAIHSn/edit?usp=sharing&ouid=102902808486600263780&rtpof=true&sd=true")
            admin = telebot.types.InlineKeyboardButton("админ", url="https://t.me/Vrevetka")
            price = telebot.types.InlineKeyboardButton("цены", url="https://docs.google.com/document/d/1dRmjRQQCAZoeQogxQhUIoxf96l-4lTSN/edit?usp=sharing&ouid=102902808486600263780&rtpof=true&sd=true")
            main = telebot.types.InlineKeyboardButton("меню")
            marcup.add(time, price, admin, main)
            bot.send_message(message.chat.id, "Что бы определиться с временем нажмите на кнопку \"Время\" \nОпределились с временем? \nТогда посмотрите цены, а после напишите Администратору, он Вас зарегистрирует. \nСпасибо за обращение!", reply_markup=marcup)
        elif message.text == "время":
            marcup = telebot.types.InlineKeyboardMarkup()
            time = telebot.types.InlineKeyboardButton("время", url="https://docs.google.com/spreadsheets/d/1k-HcnYFm-cuXTLAGWcMQ8t0SBVgAIHSn/edit?usp=sharing&ouid=102902808486600263780&rtpof=true&sd=true")
            marcup.add(time)
            bot.send_message(message.chat.id, "Что бы посмотреть время нажмите на кнопку.", reply_markup=marcup)
        elif message.text == "админ" or message.text == "администатор":
            marcup = telebot.types.InlineKeyboardMarkup()
            admin = telebot.types.InlineKeyboardButton("админ", url="https://t.me/Vrevetka")
            marcup.add(admin)
            bot.send_message(message.chat.id, "Для обращения к администатору нажмите на кнопку.", reply_markup=marcup)
        elif message.text == "примеры работ":
            bot.send_message(message.chat.id, "<a href=\"http://firephoto.ru/index.php/photo\"><b>Примеры моих работ с поседних фотосессий</b></a>", parse_mode='html')
        elif message.text == "меню":
            marcup = telebot.types.ReplyKeyboardMarkup()
            website = telebot.types.KeyboardButton('сайт')
            price = telebot.types.KeyboardButton('цены')
            registration = telebot.types.KeyboardButton('регистрация')
            examples = telebot.types.KeyboardButton("примеры работ")
            admin = telebot.types.InlineKeyboardButton("администатор")
            marcup.add(website, price, registration, examples, admin)
            bot.send_message(message.chat.id, "<b>Вы в главном меню</b>", parse_mode='html', reply_markup=marcup)
        else:
            bot.send_message(message.chat.id, f"Я тебя не понимаю(", parse_mode='html')

bot.polling(none_stop=True)
