import os
import random
from collections import defaultdict

from telegram.ext import Filters
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.update import Update

from descriptions import courses, default_skills, PersonDescription
from optimization import scalar_optimize
from perfect_vacancy import (
    get_skill_difference,
)
from transformer import Transformer
from vacancies import all_vacancies_descriptions

salaries = {'0-50': 50000, '50-100': 100000, '100-130': 130000, '130-160': 160000, 'Больше 160': 200000}


users = defaultdict()
transformer = Transformer()
users[242282672] = PersonDescription(salary=80000, skills=default_skills, ratings=[], vector=[])
users[428336217] = PersonDescription(salary=80000, skills=default_skills, ratings=[], vector=[])


def random_greeting():
    return random.choice(['Отличный выбор.', 'Спасибо что поделился!', 'Записал в свой блокнот.'])


updater = Updater(os.environ['TOKEN'], use_context=True)
dispatcher = updater.dispatcher

professions = []


def start(update: Update, context: CallbackContext):
    users[update.message.chat_id] = PersonDescription(skills=default_skills)
    kbd_layout = [['Python разработчик'], ['Таргетолог'], ['UI/UX designer']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text='Выбери профессию, в которой ты хочешь развиваться', reply_markup=kbd)


def rules(update: Update, context: CallbackContext):
    answer = f'Привет, меня зовут Парето! Я помогу тебе получить работу твоей мечты, приложив минимум усилий!\n' \
             f'Для начала тебе надо будет немного рассказать о своих навыках\n' \
             f'Потом искусственный интеллект подберет тебе идеальную вакансию, и расскажет какие курсы надо пройти для ее получения'
    update.message.reply_text(answer)


def ask_salary(update: Update, context: CallbackContext):
    users[update.message.chat_id].name = update.message.text
    kbd_layout = [['0-50'], ['50-100'], ['100-130'], ['130-160'], ['Больше 160']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(
        text='Какая интересная профессия!\n'
             'Укажи диапазон в котором находится твоя зарплата (об этом конечно же никто не узнает)',
        reply_markup=kbd,
    )


def choose_perfect_skills(update: Update, context: CallbackContext):
    kbd_layout = [['Python'], ['SQL'], ['Web'], ['Перейти к выбору навыков, которые хочется подтянуть']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    if update.message.text in ('Python', 'SQL', 'Web'):
        users[update.message.chat_id].skills[update.message.text] = 5
        context.bot.sendMessage(
            chat_id=update.message.chat_id,
            text=f'{random_greeting()} Есть ли еще навыки, в которых ты уверен?',
            reply_markup=kbd,
        )
    else:
        users[update.message.chat_id].salary = salaries.get(update.message.text)
        update.message.reply_text(
            text='Благодарю за честность!\n'
                 'А теперь давай познакомимся поближе:)\n'
                 'Выбери навыки из списка ниже, в которых ты уверен',
            reply_markup=kbd,
        )


def choose_middle_skills(update: Update, context: CallbackContext):
    kbd_layout = [['CI/CD'], ['Golang'], ['Tests'], ['Перейти к выбору навыков, которые хочется изучить']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    if update.message.text in ('CI/CD', 'Golang', 'Tests'):
        users[update.message.chat_id].skills[update.message.text] = 3
        context.bot.sendMessage(
            chat_id=update.message.chat_id,
            text=f'{random_greeting()} Есть ли еще навыки, которые хочется подтянуть?',
            reply_markup=kbd,
        )
    else:
        update.message.reply_text(
            text='Отлично, переходим к следующему этапу!\n'
                 'Выбери навыки из спика ниже, которые хочется подтянуть',
            reply_markup=kbd,
        )


def choose_weak_skills(update: Update, context: CallbackContext):
    kbd_layout = [['Algorithms'], ['Docker'], ['Asyncio'], ['Перейти к рекомендациям']]
    kbd = ReplyKeyboardMarkup(kbd_layout)
    if update.message.text in ('Algorithms', 'Docker', 'Asyncio'):
        context.bot.sendMessage(
            chat_id=update.message.chat_id,
            text=f'{random_greeting()} Есть ли еще навыки, которые хочется изучить?',
            reply_markup=kbd,
        )
    else:
        update.message.reply_text(
            text='Осталось совсем чуть-чуть!\n'
                 'Выбери навыки из спика ниже, которые хочется изучить',
            reply_markup=kbd,
        )


def make_recommendation(update: Update, context: CallbackContext):
    kbd_layout = [['А как мне его подтянуть']]
    kbd = ReplyKeyboardMarkup(kbd_layout, resize_keyboard=True)
    person = users[update.message.chat_id]
    person_vector = transformer.person_to_vector(person).vector
    vacancies_vectors = transformer.vacancy_to_vector(all_vacancies_descriptions)
    best_vacancy = scalar_optimize(vacancies_vectors, person_vector)
    worst_skill, skill_difference = get_skill_difference(person, best_vacancy)
    users[update.message.chat_id].needed_skill = worst_skill
    try:
        salary_difference = round((best_vacancy.salary - person.salary)/person.salary, 2) * 100
    except ZeroDivisionError:
        salary_difference = 0
    answer = f'Моя рекомендация готова!\n\n' \
             f'Вакансия для тебя: {best_vacancy.name} {best_vacancy.link}\n' \
             f'Прирост в зарплате составит примерно {salary_difference}% от текущей зарплаты\n' \
             f'Скилл, который нужно подтянуть в первую очередь: {worst_skill}. ' \
             f'Разница с идеалом составляет {skill_difference} условных пункта'
    update.message.reply_text(text=answer, reply_markup=kbd)


def get_courses(update: Update, context: CallbackContext):
    reply_markup = ReplyKeyboardRemove()
    answer = f'Обрати внимание на эти ресурсы:\n' \
             f'{courses.get(users[update.message.chat_id].needed_skill)}'
    update.message.reply_text(text=answer, reply_markup=reply_markup)


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', rules))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Python разработчик|Таргетолог|UI/UX designer)$'),
    ask_salary
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(0-50|50-100|100-130|130-160|Больше 160|Python|SQL|Web)$'),
    choose_perfect_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Перейти к выбору навыков, которые хочется подтянуть|CI/CD|Golang|Tests)$'),
    choose_middle_skills,
))
dispatcher.add_handler(MessageHandler(
    Filters.regex('^(Перейти к выбору навыков, которые хочется изучить|Algorithms|Docker|Asyncio)$'),
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
