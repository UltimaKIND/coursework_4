# курсовая работа 4 Skypro python_dev

Привет! 
Я раскажу, вкратце, как это работает:
при запуске можно выбрать:
1 - для получения данных с удаленного ресурса (в нашем случае HH)
2 - для сохранения данных в файл(в нашем случае JSON)
3 - получить данные из файла(в нашем случае JSON)
любое другое число более или равное 4 - выход

1:
вводим поисковой запрос(api HH ищет его по всей вакансии)
вводим количество вакансий для получения топа(по зарплате)
вводим ключевые слова для фильтрации(фильтрация также осуществляется по всему представлению вакансии(широкие возможности для re))
вводим диапазон интересующей зарплаты в формате '10000-15000', можно и не вводить - получим топ по зарплате из всего выгруженного.

получаем вывод результатов на экран
можем прервать выполнение программы если введем любую строку содержащую 'не' - 'не', 'не хочу', 'не надо', даже 'снег' - сработает.
при любых других строках программа вернется к выбору:
1 - для получения данных с удаленного ресурса (в нашем случае HH)
2 - для сохранения данных в файл(в нашем случае JSON)
3 - получить данные из файла(в нашем случае JSON)
любое другое число более или равное 4 - выход

2:
теперь когда у нас есть данные мы можем их сохранить
вводим имя файла и данные сохраняются

3:
если хотим получить данные из файла, указываем из какого (расширение .json указывать не нужно)
загруженные данные используют для хранения ту же структуру что и загружаемые с сервера, то есть если
были загруженные с сервера на предыдущем шаге данные - они более недоступны.
для загружаемых из файла данных недоступна возможность сортировки, фильтрации и повторного сохранения.
получаем вывод на экран.

программа спросит хотим ли мы повторить, выход - строка содержащая 'не'
