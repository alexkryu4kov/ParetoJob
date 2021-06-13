from Descriptions import PersonDescription, VacancyDescription
import numpy as np
from typing import List


class Transformer:
    def vacancy_to_vector(self, vacancies: List[VacancyDescription]):
        vector_of_vacancies = []
        for vacancy in vacancies:
            salary = vacancy.salary
            keys = vacancy.skills.keys()
            current_id = vacancy.id
            vector_of_ratings = []
            for key in keys:
                vector_of_ratings.append(vacancy.skills[key])
            common_vector = vector_of_ratings.copy()
            common_vector.append(salary)
            common_vector = np.array(common_vector)
            vector_of_ratings = np.array(vector_of_ratings)
            vector_of_vacancies.append(
                {'id': current_id, 'ratings': vector_of_ratings, 'salary': salary, 'link': vacancy.link,
                 'vector': common_vector})
        return vector_of_vacancies

    def person_to_vector(self, person: PersonDescription) -> dict:
        salary = person.salary
        keys = person.skills.keys()
        vector_of_ratings = []
        for key in keys:
            vector_of_ratings.append(person.skills[key])
        common_vector = vector_of_ratings.copy()
        common_vector.append(salary)
        common_vector = np.array(common_vector)
        vector_of_ratings = np.array(vector_of_ratings)
        person_vector = {'ratings': vector_of_ratings, 'salary': salary, 'vector': common_vector}
        return person_vector
