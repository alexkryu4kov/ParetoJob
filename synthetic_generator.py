from descriptions import VacancyDescription
from typing import List

from numpy import random

sample_links_of_vacancies = [
    'https://hh.ru/vacancy/45409422',
    'https://hh.ru/vacancy/40612238',
    'https://hh.ru/vacancy/45375879',
    'https://hh.ru/vacancy/45415115',
    'https://hh.ru/vacancy/43949678',
]


class Generator:
    def __init__(self, vacancies: List[VacancyDescription], amount: int):
        self.list_of_vacancies = vacancies
        self.amount = amount

    def generate(self):
        start = self.list_of_vacancies[-1].id + 1
        for i in range(start, start+self.amount):
            vacancy = VacancyDescription(
                id=i,
                name='Python разработчик',
                link=random.choice(sample_links_of_vacancies, size=1)[0],
                salary=random.randint(50000, 100000),
                skills={
                    'python': random.randint(1, 5),
                    'sql': random.randint(1, 5),
                    'tests': random.randint(1, 5),
                    'web': random.randint(1, 5),
                    'teamwork': random.randint(1, 5),
                }
            )
            self.list_of_vacancies.append(vacancy)
