import os

from telegram.ext import Filters
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.update import Update

from perfect_vacancy import (
    all_vacancies_descriptions,
    get_skill_difference,
    get_perfect_vacancy,
    person_description,
)


updater = Updater(os.environ['TOKEN'], use_context=True)
dispatcher = updater.dispatcher

professions = []


def start(update: Update, context: CallbackContext):
    kbd_layout = [['Python разработчик'], ['Таргетолог'], ['UI/UX designer']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text="Выбери профессию, в которой ты хочешь развиваться", reply_markup=kbd)


def rules(update: Update, context: CallbackContext):
    answer = f'Привет, я бот'
    update.message.reply_text(answer)


def make_recommendation(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardRemove()
    perfect_vacancy = get_perfect_vacancy(person_description, all_vacancies_descriptions)
    worst_skill, skill_difference = get_skill_difference(person_description, perfect_vacancy)
    answer = f'Вакансия для тебя: {perfect_vacancy.name} {perfect_vacancy.link}\n' \
             f'Прирост в зарплате составит: {perfect_vacancy.salary - person_description.salary}\n' \
             f'Скилл, который нужно подтянуть в первую очередь: {worst_skill}. ' \
             f'Разница с идеалом составляет {skill_difference}'
    update.message.reply_text(text=answer, reply_markup=reply_markup)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Python разработчик|Таргетолог|UI/UX designer)$'),
    make_recommendation,
))
dispatcher.add_handler(MessageHandler(None, rules))
updater.start_polling()
