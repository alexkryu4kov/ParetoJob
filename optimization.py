from typing import List

import numpy
import numpy as np

from descriptions import VacancyDescription


def sigmoid(z, bias):
    return 1 / 2 / (1 + np.exp(-z + bias))


def optimizing_function(salary: int, rating: int):
    if salary >= 0:
        return (np.log(salary) ** 2) * (1 - sigmoid(rating, 2))
    else:
        return -1000


def scalar_optimize(vacancies_info: List[VacancyDescription], person_vector: numpy.ndarray):
    best_metric = -100
    best_vacancy = {}
    for vacancy in vacancies_info:
        vector = vacancy.vector
        difference_vector = vector - person_vector
        sum_ratings = sum(difference_vector[:-1])
        salary_difference = difference_vector[-1]
        current_metric = optimizing_function(salary_difference, sum_ratings)
        if current_metric > best_metric:
            best_metric = current_metric
            best_vacancy = vacancy
    return best_vacancy
