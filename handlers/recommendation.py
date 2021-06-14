from telegram.ext.callbackcontext import CallbackContext
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.update import Update

from algorithm.optimization import get_skill_difference, scalar_optimize
from algorithm.transformer import Transformer
from users import users
from vacancies import real_vacancies


def make_recommendation(update: Update, context: CallbackContext):
    transformer = Transformer()

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