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


def choose_perfect_skills(update: Update, context: CallbackContext):
    kbd_layout = [['Python'], ['SQL'], ['Web'], ['Перейти к выбору навыков, которые хочется подтянуть']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    if update.message.text in ('Python', 'SQL', 'Web'):
        context.bot.sendMessage(
            chat_id=update.message.chat_id,
            text=f'Отличный выбор! Есть ли еще навыки, в которых ты уверен?',
            reply_markup=kbd,
        )
    else:
        update.message.reply_text(text="Выбери навыки, в которых ты уверен", reply_markup=kbd)


def choose_middle_skills(update: Update, context: CallbackContext):
    kbd_layout = [['CI/CD'], ['Golang'], ['Tests'], ['Перейти к выбору навыков, которые хочется изучить']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    if update.message.text in ('CI/CD', 'Golang', 'Tests'):
        context.bot.sendMessage(
            chat_id=update.message.chat_id,
            text=f'Отличный выбор! Есть ли еще навыки, которые хочется подтянуть?',
            reply_markup=kbd,
        )
    else:
        update.message.reply_text(text="Выбери навыки, которые хочется подтянуть", reply_markup=kbd)


def choose_weak_skills(update: Update, context: CallbackContext):
    kbd_layout = [['Teamwork'], ['Docker'], ['Asyncio'], ['Перейти к рекомендациям']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    if update.message.text in ('Teamwork', 'Docker', 'Asyncio'):
        context.bot.sendMessage(
            chat_id=update.message.chat_id,
            text='Отличный выбор! Есть ли еще навыки, которые хочется изучить?',
            reply_markup=kbd,
        )
    else:
        update.message.reply_text(text="Выбери навыки, которые хочется изучить", reply_markup=kbd)


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
    Filters.regex('^(Python разработчик|Таргетолог|UI/UX designer|Python|SQL|Web)$'),
    choose_perfect_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Перейти к выбору навыков, которые хочется подтянуть|CI/CD|Golang|Tests)$'),
    choose_middle_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Перейти к выбору навыков, которые хочется изучить|Teamwork|Docker|Asyncio)$'),
    choose_weak_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^Перейти к рекомендациям$'),
    make_recommendation,
))
dispatcher.add_handler(MessageHandler(None, start))
updater.start_polling()
