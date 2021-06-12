import os

from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.update import Update

updater = Updater(os.environ['TOKEN'], use_context=True)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    kbd_layout = [['Python', 'C++'], ['Java', 'Golang'],
                  ['Haskell']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text="Выбери область, в которой ты хочешь развиваться", reply_markup=kbd)


def remove(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardRemove()
    update.message.reply_text(text="I'm back.", reply_markup=reply_markup)


def echo(update: Update, context: CallbackContext):
    answer = 'Вакансия для тебя: https://hh.ru/vacancy/44856473\nПройди курс: https://netology.ru/'
    update.message.reply_text(answer)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('remove', remove))
dispatcher.add_handler(MessageHandler(None, echo))
updater.start_polling()
