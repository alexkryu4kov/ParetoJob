from copy import deepcopy

from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update

from users import users
from descriptions import default_skills, PersonDescription


def rules(update: Update, context: CallbackContext):
    if update.message.chat_id not in users:
        users[update.message.chat_id] = PersonDescription(skills=deepcopy(default_skills))
    answer = f'Привет, меня зовут Парето! Я помогу тебе получить работу твоей мечты, приложив минимум усилий!\n' \
             f'Для начала тебе надо будет немного рассказать о своих навыках\n' \
             f'Потом искусственный интеллект подберет тебе идеальную вакансию, и расскажет какие курсы надо пройти для ее получения'
    update.message.reply_text(answer)
