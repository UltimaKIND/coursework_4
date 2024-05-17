from src.vacancy import Vacancy
import src.utils
from abc import ABC, abstractmethod
import json, os


class Saver(ABC):
    '''
    абстрактный класс для чтения, сохранения, добавления, удаления данных
    ''' 

    @abstractmethod
    def read_data(self, data):
        pass

    @abstractmethod
    def save(self, data: list[Vacancy]):
        pass

    @abstractmethod
    def add(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def delete(self, vacancy: Vacancy):
        pass

class JSONSaver(Saver):
    '''
    класс для чтения, сохранения, добавления, удаления данных в формате JSON
    пока реализовано только сохранение
    '''
    filepath = './data/'

    def __init__(self, f_path, data: list[Vacancy] = []):
        self.f_path = f'{JSONSaver.filepath}{f_path}.json'
        self.data = data

    def read_data(self):
        '''
        чтение данных, для хранения вакансий используется таже структура
        '''
        with open(self.f_path, 'r') as f:
            vacancies = Vacancy.cast_to_object_list(json.loads(f.read()))
            src.utils.print_vacancies(vacancies)
            
    def save(self):
        '''
        сохранение данных
        '''
        to_save = []
        for vacancy in self.data:
            to_save.append(vacancy.__dict__())
        with open(self.f_path, 'w') as f:
            json.dump(to_save, f)
        print('данные успешно записаны')

    def add(self, vacancy: Vacancy):
        pass

    def delete(self):
        pass


