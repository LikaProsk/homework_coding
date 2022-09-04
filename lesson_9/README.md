# Парсер access логов
Для запуска парсера и формирования отчета можно выполнить двумя способами:
1. Запуск с указанием пути к файлус access логми
    `python parse_access_log.py --file_path=<Путь до файла> `
2. Запуск с указанием пути до деректории с файлами access логов
    `python parse_access_log.py --dir_path=<Путь до файла> `

После выполнения скрипта вы получите отчет сохраниться файл report.json, а также будет выведет в консоль в следующем формате
```bash
Общее количество выполненных запросов: 1136509
Количество запросов по HTTP-методам:
    DELETE
    GET
    HEAD
    OPTIONS
    POST
    PUT
Топ 3 IP адресов, с которых были сделаны запросы:
    193.106.31.130
    198.50.156.189
    149.56.83.40
Tоп 3 самых долгих запросов:
    {'method': 'GET', 'uri': '/administrator/ ', 'ip': 'GET', 'response_time': '9999', 'date_and_time': '18/Feb/2016:08:51:56 +0100'}
    {'method': 'GET', 'uri': '/administrator/ ', 'ip': 'GET', 'response_time': '9999', 'date_and_time': '18/Feb/2016:09:24:10 +0100'}
    {'method': 'GET', 'uri': '/administrator/ ', 'ip': 'GET', 'response_time': '9999', 'date_and_time': '18/Feb/2016:16:54:22 +0100'}
```