import os

from telegram.ext import Filters
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater

from handlers.courses import get_courses
from handlers.recommendation import make_recommendation
from handlers.rules import rules
from handlers.salary import ask_salary
from handlers.skills import (
    choose_middle_skills,
    choose_perfect_skills,
    choose_weak_skills,
)
from handlers.start import start


updater = Updater(os.environ['TOKEN'], use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', rules))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Python разработчик|Data Scientist)$'),
    ask_salary
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(0-50|50-100|100-130|130-160|Больше 160|Ничего вам не скажу|Git|SQL|Python|Data Analysis)$'),
    choose_perfect_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Перейти к выбору навыков, которые хочется подтянуть|Web|Algorithms|ML|Docker|)$'),
    choose_middle_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Перейти к выбору навыков, которые хочется изучить|CI/CD|Testing|Golang|Asyncio)$'),
    choose_weak_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^Перейти к рекомендациям$'),
    make_recommendation,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^А как мне его подтянуть$'),
    get_courses,
))
dispatcher.add_handler(MessageHandler(None, start))
updater.start_polling()
