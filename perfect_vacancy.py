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


def get_skill_difference(person: PersonDescription, perfect_vacancy: VacancyDescription) -> Tuple[str, int]:
    difference = {}
    print(perfect_vacancy.skills)
    print(person.skills)
    for key, elem in person.skills.items():
        difference[key] = perfect_vacancy.skills[key] - elem
    print(difference)
    max_difference = max(difference, key=difference.get)
    return max_difference, difference[max_difference]
