from dataclasses import dataclass
from typing import List


@dataclass
class Description:
    salary: int
    skills: dict


def get_perfect_vacancy(person: Description, all_vacancies: List[Description]) -> Description:
    """Возвращает оптимальную вакансию.

    Вакансия выбирается из списка all_vacations, и должна соответствовать двум критериям:
    * максимальная разница в salary с person
    * минимальная разница в скиллах с person
    """


person_description = Description(
    salary=60_000,
    skills={
        'python': 3,
        'sql': 2,
        'tests': 3,
        'web': 3,
        'teamwork': 3,
    }
)

all_vacancies_descriptions = [
    Description(
        salary=80_000,
        skills={
            'python': 3,
            'sql': 2,
            'tests': 3,
            'web': 3,
            'teamwork': 4,
        }
    ),
    Description(
        salary=100_000,
        skills={
            'python': 4,
            'sql': 2,
            'tests': 3,
            'web': 3,
            'teamwork': 5,
        }
    ),
    Description(
        salary=110_000,
        skills={
            'python': 5,
            'sql': 5,
            'tests': 5,
            'web': 5,
            'teamwork': 4,
        }
    ),
]


perfect_vacancy = get_perfect_vacancy(
    person=person_description,
    all_vacancies=all_vacancies_descriptions,
)

# в переменной vacancy должна содержаться вакансия, которая будет предложена пользователю
