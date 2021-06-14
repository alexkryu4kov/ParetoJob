import os
import random
from collections import defaultdict
from copy import deepcopy

from telegram.ext import Filters
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.updater import Updater
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.update import Update

from descriptions import courses, default_skills, PersonDescription
from optimization import get_skill_difference, scalar_optimize
from transformer import Transformer
from vacancies import real_vacancies

salaries = {
    '0-50': random.randint(0, 50) * 1000,
    '50-100': random.randint(50, 100) * 1000,
    '100-130': random.randint(100, 130) * 1000,
    '130-160': random.randint(130, 160) * 1000,
    'Больше 160': random.randint(160, 200) * 1000,
    'Ничего вам не скажу': 100000,
}


users = defaultdict()
transformer = Transformer()

# диалоги разработчиков для отладки бота
users[242282672] = PersonDescription(salary=80000, skills=deepcopy(default_skills), ratings=[], vector=[])
users[428336217] = PersonDescription(salary=80000, skills=deepcopy(default_skills), ratings=[], vector=[])


PERFECT_KBD_LAYOUT = [['Git'], ['SQL'], ['Python'], ['Data Analysis'], ['Перейти к выбору навыков, которые хочется подтянуть']]
MIDDLE_KBD_LAYOUT = [['Web'], ['Algorithms'], ['ML'], ['Docker'], ['Перейти к выбору навыков, которые хочется изучить']]
WEAK_KBD_LAYOUT = [['CI/CD'], ['Testing'], ['Golang'], ['Asyncio'], ['Перейти к рекомендациям']]


def random_greeting():
    return random.choice(['Отличный выбор.', 'Спасибо что поделился!', 'Записал в свой блокнот.'])


updater = Updater(os.environ['TOKEN'], use_context=True)
dispatcher = updater.dispatcher

professions = []


def start(update: Update, context: CallbackContext):
    users[update.message.chat_id] = PersonDescription(skills=deepcopy(default_skills))
    kbd_layout = [['Python разработчик'], ['Data Scientist']]
    kbd = ReplyKeyboardMarkup(kbd_layout, resize_keyboard=True)
    update.message.reply_text(text='Выбери профессию, в которой ты хочешь развиваться', reply_markup=kbd)


def rules(update: Update, context: CallbackContext):
    answer = f'Привет, меня зовут Парето! Я помогу тебе получить работу твоей мечты, приложив минимум усилий!\n' \
             f'Для начала тебе надо будет немного рассказать о своих навыках\n' \
             f'Потом искусственный интеллект подберет тебе идеальную вакансию, и расскажет какие курсы надо пройти для ее получения'
    update.message.reply_text(answer)


def ask_salary(update: Update, context: CallbackContext):
    users[update.message.chat_id].name = update.message.text
    kbd_layout = [['0-50'], ['50-100'], ['100-130'], ['130-160'], ['Больше 160'], ['Ничего вам не скажу']]
    kbd = ReplyKeyboardMarkup(kbd_layout, resize_keyboard=True)
    update.message.reply_text(
        text='Какая интересная профессия!\n'
             'Укажи диапазон в котором находится твоя зарплата (об этом конечно же никто не узнает)',
        reply_markup=kbd,
    )


def choose_perfect_skills(update: Update, context: CallbackContext):
    kbd = ReplyKeyboardMarkup(PERFECT_KBD_LAYOUT, resize_keyboard=True)
    if update.message.text in ('Git', 'SQL', 'Python', 'Data Analysis'):
        users[update.message.chat_id].skills[update.message.text] = 5
        PERFECT_KBD_LAYOUT.remove([update.message.text])
        kbd = ReplyKeyboardMarkup(PERFECT_KBD_LAYOUT, resize_keyboard=True)
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
    kbd = ReplyKeyboardMarkup(MIDDLE_KBD_LAYOUT, resize_keyboard=True)
    if update.message.text in ('Web', 'Algorithms', 'ML', 'Docker'):
        users[update.message.chat_id].skills[update.message.text] = 3
        MIDDLE_KBD_LAYOUT.remove([update.message.text])
        kbd = ReplyKeyboardMarkup(MIDDLE_KBD_LAYOUT, resize_keyboard=True)
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
    kbd = ReplyKeyboardMarkup(WEAK_KBD_LAYOUT, resize_keyboard=True)
    if update.message.text in ('CI/CD', 'Testing', 'Golang', 'Asyncio'):
        users[update.message.chat_id].skills[update.message.text] = 1
        WEAK_KBD_LAYOUT.remove([update.message.text])
        kbd = ReplyKeyboardMarkup(WEAK_KBD_LAYOUT, resize_keyboard=True)
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
    vacancies_vectors = transformer.vacancy_to_vector(real_vacancies)
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
