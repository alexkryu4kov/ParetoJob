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
    'Machine Learning',
    'Git',
    'Data Analysis',
))

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
