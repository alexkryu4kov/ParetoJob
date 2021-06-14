from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update


def rules(update: Update, context: CallbackContext):
    answer = f'Привет, меня зовут Парето! Я помогу тебе получить работу твоей мечты, приложив минимум усилий!\n' \
             f'Для начала тебе надо будет немного рассказать о своих навыках\n' \
             f'Потом искусственный интеллект подберет тебе идеальную вакансию, и расскажет какие курсы надо пройти для ее получения'
    update.message.reply_text(answer)
