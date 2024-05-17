import requests, json


class Vacancy:
    '''
    класс для представления объектов вакансий
    '''
    #список для хранения экземпляров класса
    vacancies = []
    #получение курса валют центробанк
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    exchange_rates = json.loads(response.text)['Valute']
    #api HH предоставляет код белорусского рубля как BYR(до 2016) а центробанк как BYN(после 2016)
    exchange_rates['BYR'] = exchange_rates['BYN']

    def __init__(self, **params: dict):
        self.id = params.get('id')
        self.name = params.get('name') or None
        self.area = (params.get('area') or None).get('name')
        self.experience = (params.get('experience') or None).get('name')
        self.salary = params.get('salary')
        self.schedule = (params.get('schedule') or None).get('name')

        #переводим зарплату в рубли
        if not isinstance(self.salary, int):
            if self.salary['currency'] != 'RUR':
                currency = Vacancy.exchange_rates[self.salary['currency']]
                nominal = currency['Nominal']
                value = currency['Value']
                self.salary['currency'] = 'RUR'
                if self.salary['from']:
                    self.salary['from'] = self.salary["from"]*value/nominal
                if self.salary['to']:
                    self.salary['to'] = self.salary["to"]*value/nominal

            #если у зарплаты есть поле от (from) инициализируем зарплаты, иначе полем до (to)
            if self.salary['from']:
                self.salary = self.salary['from']
            else:
                self.salary = self.salary['to']

        #строковое представление того что получили с внешнего ресурса
        self.params = json.dumps(params, ensure_ascii=False)

        #добавляем объект в список на уровне класса
        Vacancy.vacancies.append(self)

    @classmethod
    def new_vacancy(cls, params: dict):
        '''
        инициализация нового объекта
        '''
        return cls(**params)

    @classmethod
    def clear_vacancies(cls):
        '''
        очищаем список вакансий
        '''
        cls.vacancies = []

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]):
        '''
        инициализация списка вакансий
        '''
        cls.clear_vacancies() 
        for vacancy in vacancies:
            cls.new_vacancy(vacancy)
        return cls.vacancies

    def __str__(self):
        '''
        строковое представление объекта
        '''
        return f'id:\t\t{self.id}\nname:\t\t{self.name}\ncity:\t\t{self.area}\
                \nexperience:\t{self.experience}\nsalary:\t\t{self.salary}\
                \nschedule\t{self.schedule}\n'

    def __dict__(self):
        '''
        метод для сериализации объектов
        '''
        return{'id': self.id, 'name': self.name, 'area': {'name': self.area},\
                'experience': {'name': self.experience}, 'salary': self.salary,\
                'schedule': {'name': self.schedule}}

    #методы для реализаций операций сравнения
    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False

    def __ne__(self, other):
        if isinstance(other, Vacancy):
            return not self.salary == other.salary

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary
        return False

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        return False

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        return False

    def __ge__(self, other):
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        return False


