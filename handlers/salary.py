from telegram.ext.callbackcontext import CallbackContext
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.update import Update

from users import users


def ask_salary(update: Update, context: CallbackContext):
    users[update.message.chat_id].name = update.message.text
    kbd_layout = [['0-50'], ['50-100'], ['100-130'], ['130-160'], ['Больше 160'], ['Ничего вам не скажу']]
    kbd = ReplyKeyboardMarkup(kbd_layout, resize_keyboard=True)
    update.message.reply_text(
        text='Какая интересная профессия!\n'
             'Укажи диапазон в котором находится твоя зарплата (об этом конечно же никто не узнает)',
        reply_markup=kbd,
    )
