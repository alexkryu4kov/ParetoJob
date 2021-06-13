from descriptions import PersonDescription, VacancyDescription
from typing import List

from numpy import array


class Transformer:
    def vacancy_to_vector(self, vacancies: List[VacancyDescription]) -> List[VacancyDescription]:
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
            common_vector = array(common_vector)
            vector_of_ratings = array(vector_of_ratings)
            vector_of_vacancies.append(
                VacancyDescription(
                    id=current_id,
                    name=vacancy.name,
                    ratings=vector_of_ratings,
                    salary=salary,
                    link=vacancy.link,
                    vector=common_vector,
                    skills=vacancy.skills,
                )
            )
        return vector_of_vacancies

    def person_to_vector(self, person: PersonDescription) -> PersonDescription:
        salary = person.salary
        keys = person.skills.keys()
        vector_of_ratings = []
        for key in keys:
            vector_of_ratings.append(person.skills[key])
        common_vector = vector_of_ratings.copy()
        common_vector.append(salary)
        common_vector = array(common_vector)
        vector_of_ratings = array(vector_of_ratings)
        person_vector = PersonDescription(
            ratings=vector_of_ratings,
            salary=salary,
            vector=common_vector
        )
        return person_vector
