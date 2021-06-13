
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class VacancyDescription:
    name: str = ''
    salary: int = 0
    link: str = ''
    skills: dict = field(default_factory=defaultdict)
    id: int = 0


@dataclass
class PersonDescription:
    salary: int = 0
    skills: dict = field(default_factory=defaultdict)
