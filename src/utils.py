from src.saver import JSONSaver
from src.parser import HH
from src.vacancy import Vacancy
import os, time


endl = '\n'

def clear_console():
    '''
    почисти консоль
    '''
    os.system('clear')

def class_to_dict(obj):
    '''
    функция для сериализации объектов
    '''
    return obj.__dict__()

def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    '''
    фильтруй вакансии по списку слов
    '''
    #поиск по строковому представления вакасиии в целом, возможно стоит
    #добавить регулярные выражения.
    filtered_vacancies = []
    if filter_words:
        for vacancy in vacancies_list:
            filtered = []
            for word in filter_words:
                if word in vacancy.params:
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies
    else:
        return vacancies_list
          
def get_vacancies_by_salary(vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    '''
    фильтруй вакансии по зарплате пример '100000-120000'
    '''

    filtered_vacancies = []
    if salary_range:
        between = tuple(int(i) for i in (salary_range.split('-')))
    else:
        return vacancies

    for vacancy in vacancies:
        if between[0] <= vacancy.salary <= between[1]:
            filtered_vacancies.append(vacancy)

    return filtered_vacancies

def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    '''
    отсортируй список вакансий
    '''
    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)

def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    '''
    верни топ по заданному числу
    '''
    return vacancies[:top_n]

def print_vacancies(vacancies: list[Vacancy]):
    '''
    распечатай вакансии
    '''
    for vacancy in vacancies:
        print(f'{vacancy}')

def user_interaction():
    '''
    функция для взаимодействия с пользователем
    '''
    clear_console()
    platforms = ['HeadHunter']

    while(True):
        user_select = ''
        print('hello_')
        print('что желаете? можно:')
        print(f"1 - получить данные о вакансиях из {', '.join(platforms)}")
        print(f'2 - сохранить данные в файл')
        print(f'3 - получить данные из файла')
        print(f'>= 4 ===> выход')
        try:
            select_mode = int(input())
        except ValueError:
            print('можно только цифры, эх')
            break
        clear_console()
        
        if select_mode == 1:
            search_query = input('Введите поисковой запрос: ')
            top_n = int(input('Введите количество вакансий для вывода в топ N: '))
            filter_words = input('Введите ключевые слова для фильтрации вакансий: ').split()
            salary_range = input('Введите диапазон зарплат: ') # Пример: 100000-150000

            fileworker = 'fileworker'
            
            #инициализация объекта работающего с api внешнего ресурса
            #и вызовы его методов
            hh_api = HH(fileworker)
            hh_vacancies = hh_api.get_vacancies(search_query)
            vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

            #вызовы функций осуществляющих:
            #фильтрацию по словам
            filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
            #фильтрацию по зарплате
            ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
            #сортировку по зарплате
            sorted_vacancies = sort_vacancies(ranged_vacancies)
            #срез по отсортированному списку -> топ
            top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

            #печать
            print_vacancies(top_vacancies)

            user_select = input('можем сохранить данные в файл или повторить поиск, продолжаем?\n')
            if 'не' in user_select:
                clear_console()
                break
            else:
                clear_console()
                continue

        elif select_mode == 2:
            #сохраняем данные в файл
            try:
                file_name = input(f'введи имя файла:{endl}') 
                clear_console()
                file_worker = JSONSaver(file_name, top_vacancies)
                file_worker.save()
            except UnboundLocalError:
                print('данных то нет, эх')
                break

            #---------------------------------------
            user_select = input('хочешь повторить?\n')
            if 'не' in user_select:
                clear_console()
                break
            else:
                clear_console()
                continue
        elif select_mode == 3:
            #читаем данные из файла
            available_files = os.listdir('data')
            if available_files:
                print(f'доступны файлы: {", ".join(available_files)}')
                selected_file = input('напиши какой ты хочешь: ')
                if selected_file + '.json' not in available_files:
                    print('а такого файла нет')
                    time.sleep(3)
                    clear_console()
                else:
                   file_worker = JSONSaver(selected_file)
                   file_worker.read_data()
                user_select = input('хочешь повторить?\n')
                if 'не' in user_select:
                    clear_console()
                    break
                else:
                    clear_console()
                    continue
            else:
                print(f'файлов для чтения пока нет')
                time.sleep(3)
                clear_console()

        else:
            break
            

