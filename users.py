from collections import defaultdict
from copy import deepcopy

from descriptions import default_skills, PersonDescription


users = defaultdict()

# TODO: унести информацию о сессии в БД
# диалоги разработчиков для отладки бота
users[242282672] = PersonDescription(salary=80000, skills=deepcopy(default_skills), ratings=[], vector=[])
users[428336217] = PersonDescription(salary=80000, skills=deepcopy(default_skills), ratings=[], vector=[])
