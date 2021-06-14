from copy import deepcopy

from telegram.ext.callbackcontext import CallbackContext
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.update import Update

from users import users
from descriptions import default_skills, PersonDescription


def start(update: Update, context: CallbackContext):
    if update.message.chat_id not in users:
        users[update.message.chat_id] = PersonDescription(skills=deepcopy(default_skills))
    kbd_layout = [['Python разработчик'], ['Data Scientist']]
    kbd = ReplyKeyboardMarkup(kbd_layout, resize_keyboard=True)
    update.message.reply_text(text='Выбери профессию, в которой ты хочешь развиваться', reply_markup=kbd)
