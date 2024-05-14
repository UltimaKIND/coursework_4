import requests, json

class Vacancy:
    #список для хранения экземпляров класса
    vacancies = []
    #список атрибутов для инициализация
    options = ['id', 'name', 'experience', 'salary', 'schedule']
    #получение курса валют центробанк
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    exchange_rates = json.loads(response.text)['Valute']
    #api HH предоставляет код белорусского рубля как BYR(до 2016) а центробанк как BYN(после 2016)
    exchange_rates['BYR'] = exchange_rates['BYN']

    def __init__(self, **params):
        #инициализируем атрибуты из списка класса options если таковые есть в params, иначе None 
        for option in Vacancy.options:
            if option in params.keys():
                self.__dict__[option] = params[option]
            else:
                self.__dict__[option] = None
        #переводим зарплату в рубли, список курсов также на уровне класса

        if self.salary:
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

        if self.experience:
            self.experience = self.experience['name']

        if self.schedule:
            self.schedule = self.schedule['name']

        #добавляем объект в список на уровне класса
        Vacancy.vacancies.append(self)

    @classmethod
    def new_vacancy(cls, params):
        return cls(**params)


    def __str__(self):
        return f'id:\t\t{self.id}\nname:\t\t{self.name}\nexperience:\t{self.experience}\
                \nsalary:\t\t{self.salary}\nshedule\t\t{self.schedule}\n'

    def cast_to_object_list(vacancies):
        for vacancy in vacancies:
            Vacancy.new_vacancy(vacancy)
        return Vacancy.vacancies

if __name__ == '__main__':
    test_1 = {'id':'test1', 'name':'test1', 'experience':'test1', 'salary':None, 'shedule':'test1', 'test_key':'test1'}
    test_2 = {'id':'test2', 'name':'test2', 'experience':'test2', 'salary':None, 'shedule':'test2', 'test_key':'test2'}
    test_list = [test_1, test_2]

    vacancies = Vacancy.cast_to_object_list(test_list)


    for vacancy in vacancies:
        print(vacancy)

        
