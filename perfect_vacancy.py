from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Description:
    name: str
    salary: int
    link: str
    skills: dict


person_description = Description(
    name='Python разработчик',
    salary=60_000,
    link='https://hh.ru/vacancy/44856473',
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
        name='Python разработчик',
        salary=80_000,
        link='https://hh.ru/vacancy/44856473',
        skills={
            'python': 3,
            'sql': 2,
            'tests': 3,
            'web': 3,
            'teamwork': 4,
        }
    ),
    Description(
        name='Python разработчик',
        salary=100_000,
        link='https://hh.ru/vacancy/44856473',
        skills={
            'python': 4,
            'sql': 2,
            'tests': 3,
            'web': 3,
            'teamwork': 5,
        }
    ),
    Description(
        name='Python разработчик',
        salary=110_000,
        link='https://hh.ru/vacancy/44856473',
        skills={
            'python': 5,
            'sql': 5,
            'tests': 5,
            'web': 5,
            'teamwork': 4,
        }
    ),
]


def get_perfect_vacancy(person: Description, all_vacancies: List[Description]) -> Description:
    """Возвращает оптимальную вакансию.

    Вакансия выбирается из списка all_vacations, и должна соответствовать двум критериям:
    * максимальная разница в salary с person
    * минимальная разница в скиллах с person
    """

    return all_vacancies[0]


def get_skill_difference(person: Description, perfect_vacancy: Description) -> Tuple[str, int]:
    difference = {}
    for key, elem in person.skills.items():
        difference[key] = elem - perfect_vacancy.skills[key]
    max_difference = max(difference, key=difference.get)
    return max_difference, difference[max_difference]
