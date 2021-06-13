from typing import List

from numpy import exp, log, ndarray

from descriptions import default_skills, VacancyDescription


def sigmoid(z, bias):
    return 1 / 2 / (1 + exp(-z + bias))


def optimizing_function(salary: int, rating: int):
    if salary >= 0:
        return (log(salary) ** 2) * (1 - sigmoid(rating, 2))
    else:
        return -1000


def scalar_optimize(vacancies_info: List[VacancyDescription], person_vector: ndarray):
    best_metric = -100
    best_vacancy = VacancyDescription(skills=default_skills)
    for vacancy in vacancies_info:
        difference_vector = vacancy.vector - person_vector
        sum_ratings = sum(difference_vector[:-1])
        salary_difference = difference_vector[-1]
        current_metric = optimizing_function(salary_difference, sum_ratings)
        if current_metric > best_metric:
            best_metric = current_metric
            best_vacancy = vacancy
    return best_vacancy
