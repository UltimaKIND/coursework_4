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

    def __init__(self, f_path, data: list[Vacancy]):
        self.f_path = f'{JSONSaver.filepath}{f_path}.json'
        self.data = data

    def read_data(self, f_path):
        pass

    def save(self):
        to_save = []
        for vacancy in self.data:
            to_save.append(json.dumps(vacancy, default=src.utils.class_to_dict))
        with open(self.f_path, 'w') as f:
            f.writelines(to_save)
        print('данные успешно записаны')



    def add(self, vacancy: Vacancy):
        pass

    def delete(self):
        pass

