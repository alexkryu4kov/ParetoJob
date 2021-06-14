from collections import defaultdict
from dataclasses import dataclass, field

from numpy import ndarray


skills = frozenset((
    'Python',
    'SQL',
    'Web',
    'CI/CD',
    'Golang',
    'Testing',
    'Algorithms',
    'Docker',
    'Asyncio',
    'ML',
    'Git',
    'Data Analysis',
))

courses = {
    'Python': 'https://stepik.org/course/67/promo\n'
              'https://stepik.org/course/512/promo\n'
              'https://www.coursera.org/specializations/python\n'
              'https://docs.python.org/3/index.html\n',
    'SQL': 'https://netology.ru/programs/sql-lessons#/\n'
           'https://www.udacity.com/course/sql-for-data-analysis--ud198\n'
           'https://stepik.org/course/55776/promo',
    'CI/CD': 'https://www.udacity.com/course/intro-to-devops--ud611\n'
             'https://www.oreilly.com/library/view/effective-devops/9781491926291/\n',
    'Golang': 'https://stepik.org/course/54403/promo\n'
              'https://www.coursera.org/specializations/google-golang\n',
    'Testing': 'https://netology.ru/programs/qa\n'
             'https://stepik.org/course/575/promo\n',
    'Algorithms': 'https://stepik.org/course/217/promo\n'
                  'https://www.coursera.org/learn/algorithms-part1\n'
                  'https://www.coursera.org/learn/algorithms-part2\n'
                  'https://www.labirint.ru/books/671295/\n',
}

default_skills = defaultdict(int, {k: 0 for k in skills})


@dataclass
class BaseDescription:
    salary: int = 0
    skills: dict = field(default_factory=defaultdict)


@dataclass
class PersonDescription(BaseDescription):
    needed_skill: str = ''
    ratings: list = field(default_factory=list)
    vector: list = field(default_factory=list)


@dataclass
class VacancyDescription(BaseDescription):
    name: str = ''
    link: str = ''
    id: int = 0
    ratings: ndarray = field(default_factory=list)
    vector: ndarray = field(default_factory=list)
