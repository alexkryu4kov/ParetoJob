from random import choice

from telegram.ext.callbackcontext import CallbackContext
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.update import Update

from consts import (
    salaries,
    MIDDLE_KBD_LAYOUT,
    PERFECT_KBD_LAYOUT,
    WEAK_KBD_LAYOUT,
)
from copy import deepcopy
from descriptions import default_skills, PersonDescription
from users import users


def random_greeting():
    return choice(['Отличный выбор.', 'Спасибо что поделился!', 'Записал в свой блокнот.'])


def choose_perfect_skills(update: Update, context: CallbackContext):
    if update.message.chat_id not in users:
        users[update.message.chat_id] = PersonDescription(skills=deepcopy(default_skills))
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
    if update.message.chat_id not in users:
        users[update.message.chat_id] = PersonDescription(skills=deepcopy(default_skills))

    kbd = ReplyKeyboardMarkup(MIDDLE_KBD_LAYOUT, resize_keyboard=True)
    if update.message.text in ('Web', 'Algorithms', 'Machine Learning', 'Docker'):
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
    if update.message.chat_id not in users:
        users[update.message.chat_id] = PersonDescription(skills=deepcopy(default_skills))
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
