from descriptions import default_skills, VacancyDescription


all_vacancies_descriptions = [
    VacancyDescription(
        id=1,
        name='Python разработчик',
        salary=80_000,
        link='https://hh.ru/vacancy/41959154',
        skills=default_skills,
    ),
    VacancyDescription(
        id=2,
        name='Python разработчик',
        salary=100_000,
        link='https://hh.ru/vacancy/41959154',
        skills=default_skills,
    ),
    VacancyDescription(
        id=3,
        name='Python разработчик',
        salary=110_000,
        link='https://hh.ru/vacancy/41959154',
        skills=default_skills,
    ),
]

all_vacancies_descriptions[0].skills.update({
        'python': 3,
        'sql': 2,
        'tests': 3,
        'web': 3,
        'teamwork': 4,
    })

all_vacancies_descriptions[1].skills.update({
        'python': 4,
        'sql': 2,
        'tests': 3,
        'web': 3,
        'teamwork': 5,
    })

all_vacancies_descriptions[2].skills.update({
        'python': 5,
        'sql': 5,
        'tests': 5,
        'web': 5,
        'teamwork': 4,
    })
