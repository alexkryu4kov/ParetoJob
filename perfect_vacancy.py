from Descriptions import VacancyDescription, PersonDescription
from typing import List, Tuple
from synthetic_generator import Generator
from optimization import scalar_optimize
from Transformer import Transformer

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
# генерирует 5 синтетических вакансий
Generator(all_vacancies_descriptions, 5).generate()

transformer = Transformer()

person_vector = transformer.person_to_vector(person_description)['vector']

vacancies_vectors = transformer.vacancy_to_vector(all_vacancies_descriptions)

best_vacancy = scalar_optimize(vacancies_vectors, person_vector)

print(best_vacancy)
