from src.parser import HH
from src.vacancy import Vacancy
from typing import List

def filter_vacancies(vacancies_list, filter_words):
    pass

def get_vacancies_by_salary(filtered_vacancies, salary_range):
    pass

def sort_vacancies(vacancies):
    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)

def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]

def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(f'{vacancy}')

def user_interaction():
    platforms = ['HeadHunter']
    search_query = input('Введите поисковой запрос: ')
    top_n = int(input('Введите количество вакансий для вывода в топ N: '))
    #filter_words = input('Введите ключевые слова для фильтрации вакансий: ').split()
    #salary_range = input('Введите диапазон зарплат: ') # Пример: 100000-150000

    fileworker = 'fileworker'
    hh_api = HH(fileworker)
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    sorted_vacancies = sort_vacancies(vacancies_list)
    
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)


    #---------------------------------------

    print_vacancies(top_vacancies)

    #---------------------------------------


    #filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    #ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    #sorted_vacancies = sort_vacancies(ranged_vacancies)
    #top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #print_vacancies(top_vacancies)

