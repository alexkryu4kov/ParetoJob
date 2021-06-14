from copy import deepcopy

from descriptions import default_skills, VacancyDescription


# TODO: получать вакансии из базы
real_vacancies = [
    VacancyDescription(
        name='Стажёр Data Scientist',
        salary=50000,
        link='https://opendatascience.slack.com/archives/C04DA5FUF/p1623430610039600',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Junior Data Scientist',
        salary=100000,
        link='https://opendatascience.slack.com/archives/C04DA5FUF/p1623410043499300',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Middle Аналитик Данных',
        salary=120000,
        link='https://opendatascience.slack.com/archives/C04DA5FUF/p1623406169497200',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Team Lead DS',
        salary=250000,
        link='https://opendatascience.slack.com/archives/C04DA5FUF/p1623248503415500',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Middle DS',
        salary=200000,
        link='https://opendatascience.slack.com/archives/C04DA5FUF/p1623242599398200',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Junior Python Developer',
        salary=100000,
        link='https://hh.ru/vacancy/45375879',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Team Lead DS',
        salary=250000,
        link='https://opendatascience.slack.com/archives/C04DA5FUF/p1623248503415500',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Python разработчик',
        salary=100000,
        link='https://novosibirsk.hh.ru/vacancy',
        skills=deepcopy(default_skills),
    ),
    VacancyDescription(
        name='Разработчик Python',
        salary=200000,
        link='https://career.habr.com/vacancies/1000078109',
        skills=deepcopy(default_skills),
    )
]


# TODO: жуткий код, нужен для решения проблемы с отсутствием у пользователя скиллов, нужных в вакансии
# TODO: решить эту проблему в коде алгоритма, он не должен падать от такого
real_vacancies[0].skills.update(
    {
        'Python': 3,
        'SQL': 1,
        'Git': 3,
        'Machine Learning': 2,
        'Algorithms': 2,
    }
)

real_vacancies[1].skills.update(
    {
        'Python': 3,
        'SQL': 2,
        'Git': 3,
        'Machine Learning': 3,
        'CI/CD': 1,
    }
)

real_vacancies[2].skills.update(
    {
        'Python': 5,
        'SQL': 4,
        'Git': 5,
        'Data Analysis': 4,
    }
)

real_vacancies[3].skills.update(
    {
        'Python': 5,
        'CI/CD': 2,
        'Algorithms': 3,
        'Machine Learning': 5,
        'Data Analysis': 4,
    }
)

real_vacancies[4].skills.update(
    {
        'Python': 4,
        'SQL': 3,
        'Machine Learning': 4,
        'Data Analysis': 4,
    }
)

real_vacancies[5].skills.update(
    {
        'Python': 4,
        'SQL': 3,
        'Algorithms': 3,
        'Data Analysis': 3,
    }
)

real_vacancies[6].skills.update(
    {
        'Python': 5,
        'CI/CD': 2,
        'Algorithms': 3,
        'Machine Learning': 5,
        'Data Analysis': 4,
    }
)

real_vacancies[7].skills.update(
    {
        'Python': 5,
        'CI/CD': 3,
        'SQL': 2,
        'Algorithms': 2,
        'Machine Learning': 1,
        'Data Analysis': 1,
    }
)

real_vacancies[8].skills.update(
    {
        'Python': 5,
        'Testing': 4,
        'CI/CD': 3,
        'SQL': 4,
        'Algorithms': 2,
    }
)
