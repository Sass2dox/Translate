import telebot #библиотека для создания и работы с ботами
import googletrans
from googletrans import Translator #библиотека, помогающая переводить тексты
from telebot import types


print(googletrans.LANGUAGES)

token = '6494875450:AAEqWXdoPpoLXpfVZ8Ls9oCraSsaKjKNyFA'
bot = telebot.TeleBot(token) #соединяем код питона с нашим ботом в телеграме

@bot.message_handler(commands=['start']) #обработчик, помогает боту среагировать на /старт
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Русский - Английский',
                                                           'Английский - Русский',
                                                           'Русский - Китайский',
                                                           'Китайский - Русский',
                                                           'Русский - Немецкий',
                                                           'Немецкий - Русский',
                                                           'Русский - Казахский',
                                                           'Казахский - Русский']])
    bot.send_message(message.chat.id, 'Выбери языковую пару для переводов', reply_markup=keyboard)

l = ''

@bot.message_handler(content_types=['text'])
def language(message):
    global l
    if message.text == 'Русский - Английский':
        m = bot.send_message(message.chat.id, 'Введите текст на русском языке')
        l = 'en'
        bot.register_next_step_handler(m, translate)
    elif message.text == 'Английский - Русский':
        m = bot.send_message(message.chat.id, 'Введите текст на английском языке')
        l = 'ru'
        bot.register_next_step_handler(m, translate)
        
    elif message.text == 'Русский - Китайский':
        m = bot.send_message(message.chat.id, 'Введите текст на русском языке')
        l = 'zh-cn'
        bot.register_next_step_handler(m, translate)
        
    elif message.text == 'Китайский - Русский':
        m = bot.send_message(message.chat.id, 'Введите текст на китайском языке')
        l = 'ru'
        bot.register_next_step_handler(m, translate)
        
    elif message.text == 'Русский - Немецкий':
        m = bot.send_message(message.chat.id, 'Введите текст на русском языке')
        l = 'de'
        bot.register_next_step_handler(m, translate)
        
    elif message.text == 'Немецкий - Русский':
        m = bot.send_message(message.chat.id, 'Введите текст на немецком языке')
        l = 'ru'
        bot.register_next_step_handler(m, translate)
        
    elif message.text == 'Русский - Казахский':
        m = bot.send_message(message.chat.id, 'Введите текст на русском языке')
        l = 'kk'
        bot.register_next_step_handler(m, translate)
        
    elif message.text == 'Казахский - Русский':
        m = bot.send_message(message.chat.id, 'Введите текст на казахском языке')
        l = 'ru'
        bot.register_next_step_handler(m, translate)

def translate(message):
    global l
    print(l)
    text = message.text #текст, который отправляет нам пользователь
    translator = Translator() #запускаем переводчик
    trans = translator.translate(text, dest=l) #переводим текст на английский
    bot.send_message(message.chat.id, trans.text) #отправляем пользователю переведенный текст
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Выбрать другую языковую пару']])
    m = bot.send_message(message.chat.id, 'Выберите опцию', reply_markup=keyboard)
    bot.register_next_step_handler(m, next)
    

def next(msg):
    if msg.text == "Выбрать другую языковую пару":
        start(msg)
    


  
bot.polling(none_stop=True) #запускаем цикл
