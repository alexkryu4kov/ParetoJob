from dataclasses import dataclass


@dataclass
class VacancyDescription:
    name: str
    salary: int
    link: str
    skills: dict
    id: int


@dataclass
class PersonDescription:
    salary: int
    skills: dict
