import telebot
from telebot import types
import time
import test
from random import shuffle



bot = telebot.TeleBot("1862921660:AAHQe6cciebdhvu6zbj44OHMHrd-gfOd5mw")
bot_info = bot.get_me()


def buttons(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    b1 = types.KeyboardButton("Все шикарно!")
    b2 = types.KeyboardButton("Нормально.")
    b3 = types.KeyboardButton("Не очень хорошо.")
    b4 = types.KeyboardButton("Полное говно. Переделывай.")
    b5 = types.KeyboardButton("exit")
    markup.row(b1, b2)
    markup.row(b3, b4)
    markup.add(b5)
    act = bot.send_message(message.chat.id, "Оцените моего бота:", reply_markup=markup)
    bot.register_next_step_handler(act, answer)
def answer(message):
    if message.text == "Все шикарно!":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIH72DFo0J0KbGStFQsX09S874Xjb0lAAK5AgACNnYgDu106wVn0luFHwQ')
    if message.text == "Нормально.":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIH82DFo1CuhToQtsL2H9VwFQABjdUhuQACuwIAAjZ2IA7ZoDLhm2E9jx8E')
    if message.text == "Не очень хорошо.":
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIH9WDFo1KTWMluQ87DcsS-ZvmHaqLFAAKxAgACNnYgDstvp_Zy2sn9HwQ')
    if message.text == "Полное говно. Переделывай.":
        bot.send_audio(message.chat.id, 'BQACAgIAAxkBAAIHxWDFokVPtG23ey0CfDJiNTTxQQJ5AAIYDAAC_pIwSpSBk5kpU_9GHwQ')
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Нажмите на /start, чтобы снова сыграть.", reply_markup=markup)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Добро пожаловать, {}.".format(message.from_user.first_name))
    bot.send_message(message.chat.id, "Комманды для бота: /send_photo, /send_music, /send_sticker")
    bot.send_message(message.chat.id, "Также можно сыграть в игру 'Jojo's Theme': ")
    start_markup = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    start_markup_btn1 = types.KeyboardButton('/game')
    start_markup.add(start_markup_btn1)
    bot.send_message(message.chat.id, "Lets Go!", reply_markup=start_markup)
@bot.message_handler(commands=['send_photo', 'send_sticker', 'send_music'])
def emil(message):
    if message.text == '/send_photo':
        bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAIHgmDFmmdmn4VKVe3M3nJ6P3yM1zq5AALxsjEb_pIwSs9YPgh9K8vvfoBRpC4AAwEAAwIAA3MAAyBHAgABHwQ')
    if message.text == '/send_sticker':
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAIHhGDFmqJ01Fo0t_1oLL8COJ9eyt4uAAIDAAOjhWYE2fJDXrbHO-EfBA')
    if message.text == '/send_music':
        bot.reply_to(message, "Wait, it will take a while...")
        bot.send_audio(message.chat.id, 'CQACAgIAAxkBAAIIDmDFpNR1IY_e2TLTfhuR_BRHHFeqAAItDAAC_pIwSlr6Dyq_Rg_nHwQ')


########################################################################################################

@bot.message_handler(commands=['game'])
def jojo(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    global tries
    tries = 7
    global names
    names = ['Jonathan', 'Joseph', 'Jotaro', 'Josuke', 'Giorno', 'Jolyne', 'Johnny', 'Josuke(Jojolion)']
    b1 = types.KeyboardButton(names[0])
    b2 = types.KeyboardButton(names[1])
    b3 = types.KeyboardButton(names[2])
    b4 = types.KeyboardButton(names[3])
    b5 = types.KeyboardButton(names[4])
    b6 = types.KeyboardButton(names[5])
    b7 = types.KeyboardButton(names[6])
    b8 = types.KeyboardButton(names[7])
    ex = types.KeyboardButton("EXIT")
    markup.row(b1, b2, b3)
    markup.row(b4, b5, b6)
    markup.row(b7, b8)
    markup.add(ex)
    global act
    act = bot.send_message(message.chat.id, "Guess Jojo's Theme: ", reply_markup=markup)
    shuffle(names)
    bot.send_audio(message.chat.id, test.data[names[0]])
    bot.register_next_step_handler(act, reply)
def reply(message):
    if message.text == names[0]:
        bot.send_animation(message.chat.id, 'CgACAgQAAxkBAAIMxGDHh54qUHzCSsS1Zmvhx1DntZ5uAAIaAgACEvWkUo6Njf0RS4xFHwQ')
        jojo(message)
    elif message.text != names[0] and message.text !="EXIT":
        bot.send_animation(message.chat.id, 'CgACAgQAAxkBAAIMwmDHh3P2LBvN6onyIyEOAud52t3_AAJhAgACD4jdUtZ7SSKeWzmLHwQ')
        bot.register_next_step_handler(act, reply)

    if message.text == "EXIT":
        bot.send_voice(message.chat.id, "AwACAgQAAxkBAAIMVmDHgyZPYd8dYPuilKKiEezVEDPYAAK6IQACOYpAUuvQGevCvy_eHwQ")
        markup = types.ReplyKeyboardRemove()
        asking = bot.send_message(message.chat.id, "Игра окончена. Оцените бота по комманде: /estimate", reply_markup=markup)
        bot.register_next_step_handler(asking, buttons)




bot.polling(none_stop=True)
