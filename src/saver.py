from src.vacancy import Vacancy
import src.utils
from abc import ABC, abstractmethod
import json, os

class Saver(ABC):

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
    filepath = './data/'

    def __init__(self, f_path, data: list[Vacancy]):
        self.f_path = f'{JSONSaver.filepath}{f_path}.json'
        self.data = data

    def save(self):
        to_save = []
        for vacancy in self.data:
            to_save.append(json.dumps(vacancy, default=src.utils.class_to_dict))
        with open(self.f_path, 'w') as f:
            f.writelines(to_save)



    def add(self, vacancy: Vacancy):
        pass

    def delete(self):
        pass

