from typing import Tuple

from descriptions import VacancyDescription, PersonDescription


person_description = PersonDescription(
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
    VacancyDescription(
        id=1,
        name='Python разработчик',
        salary=80_000,
        link='https://hh.ru/vacancy/41959154',
        skills={
            'python': 3,
            'sql': 2,
            'tests': 3,
            'web': 3,
            'teamwork': 4,
        }
    ),
    VacancyDescription(
        id=2,
        name='Python разработчик',
        salary=100_000,
        link='https://hh.ru/vacancy/41959154',
        skills={
            'python': 4,
            'sql': 2,
            'tests': 3,
            'web': 3,
            'teamwork': 5,
        }
    ),
    VacancyDescription(
        id=3,
        name='Python разработчик',
        salary=110_000,
        link='https://hh.ru/vacancy/41959154',
        skills={
            'python': 5,
            'sql': 5,
            'tests': 5,
            'web': 5,
            'teamwork': 4,
        }
    ),
]


def get_skill_difference(person: PersonDescription, perfect_vacancy: VacancyDescription) -> Tuple[str, int]:
    difference = {}
    for key, elem in person.skills.items():
        difference[key] = perfect_vacancy.skills[key] - elem
    max_difference = max(difference, key=difference.get)
    return max_difference, difference[max_difference]
