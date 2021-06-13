import numpy as np


def sigmoid(z, bias):
    return 1 / 2 / (1 + np.exp(-z + bias))


def optimizing_function(salary: int, rating: int):
    if salary >= 0:
        return (np.log(salary) ** 2) * (1 - sigmoid(rating, 2))
    else:
        return -1000


def scalar_optimize(vacancies_info, person_vector):
    best_metric = -100
    best_vacancy = []
    k = 1

    for vacancy in vacancies_info:
        vector = vacancy['vector']
        current_id = vacancy['id']
        print(f'#{k} vacancy \n')
        print(f'Вектор разницы рейтингов и зарплаты {vector - person_vector} \n')
        difference_vector = vector - person_vector
        sum_ratings = sum(difference_vector[:-1])
        salary_difference = difference_vector[-1]
        print(f' Общая разность между навыками {sum_ratings}. Повышение зарплаты на {salary_difference}')
        current_metric = optimizing_function(salary_difference, sum_ratings)
        print(f'Current metric = {current_metric}')
        if current_metric > best_metric:
            print(f'Current is better than the best! New best = {current_metric}, old was = {best_metric}')
            best_metric = current_metric
            best_vacancy = vacancy
        print('_________________________________________________\n')

        k += 1

    return best_vacancy
