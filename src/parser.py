import requests, pprint
from abc import ABC, abstractmethod

class Parser(ABC):
    def __init__(self, file_worker):
        self.fileworker = file_worker
    
    @abstractmethod
    def load_vacancies(self):
        pass 

    @abstractmethod
    def get_vacancies(self):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_salary':True}
        self.__vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 3:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.params['page'] += 1

    def get_vacancies(self, keyword):
        self.load_vacancies(keyword)
        return self.__vacancies

if __name__ == '__main__':
    hh = HH('fileworker')
    hh_vacancies = hh.get_vacancies('Python')
    pprint.pprint(hh_vacancies[0])
