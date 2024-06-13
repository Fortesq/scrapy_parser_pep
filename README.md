# Асинхронный парсер основаный на фреймворке Scrapy.

# Автор
Николай Байрамов
GitHub: https://github.com/Fortesq

### Описание
Парсер позволяет собирать данные о документации PEP.
Выводит список всех PEP 
Выводит информацию по статусам PEP

Собранные результаты выводятся в файл .csv.

### Запуск проекта
- Клонируйте репозитоий
```
git clone https://github.com/Fortesq/scrapy_parser_pep/
```
- Установите и активируйте виртуальное окружение
```
python3 -m venv venv
source venv/Scripts/activate
```
```
python3 -m pip install --upgrade pip
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 

### Запуск парсера:
Для запуска парсера введите команду в терминал:
```
scrapy crawl pep
```

Все данные сохраняются в файлах .csv в директории results/
