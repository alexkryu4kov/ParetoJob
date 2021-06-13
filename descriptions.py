from collections import defaultdict
from dataclasses import dataclass, field

from numpy import ndarray


@dataclass
class BaseDescription:
    salary: int = 0
    skills: dict = field(default_factory=defaultdict)


@dataclass
class PersonDescription(BaseDescription):
    ratings: ndarray = field(default_factory=list)
    vector: ndarray = field(default_factory=list)


@dataclass
class VacancyDescription(BaseDescription):
    name: str = ''
    link: str = ''
    id: int = 0
    ratings: ndarray = field(default_factory=list)
    vector: ndarray = field(default_factory=list)
