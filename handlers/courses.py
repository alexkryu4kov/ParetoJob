from copy import deepcopy

from telegram.ext.callbackcontext import CallbackContext
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.update import Update

from courses import courses
from descriptions import default_skills, PersonDescription
from users import users


def get_courses(update: Update, context: CallbackContext):
    if update.message.chat_id not in users:
        users[update.message.chat_id] = PersonDescription(skills=deepcopy(default_skills))
    reply_markup = ReplyKeyboardRemove()
    answer = f'Обрати внимание на эти ресурсы:\n' \
             f'{courses.get(users[update.message.chat_id].needed_skill)}'
    update.message.reply_text(text=answer, reply_markup=reply_markup)
