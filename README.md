# MIFIIB-HW-PYTHON

Реализация сквозной задачи по седьмому модулю вводного курса.

> **!** | Если вы зашли сюда и не понимаете, о чём идёт речь, сохраняйте спокойствие: мне временно потребовалось сделать этот репозиторий публичным в ходе обучения на курсах, чтобы это смогли проверить преподаватели (важно было разместить это общедоступным и именно на GitHub). Можете заниматься своими делами и не обращать внимание на сей казус с моей стороны.

## API функционал

В данной версии доступ к скрипту реализован через веб API. В отличие от версии с argparse, опциональных параметров теперь практически нет (ибо высока вероятность кривого запроса, в которой пользователь ввёл какие-то данные, но сделал это некорректно, в таком случае лучше ему об этом явно сообщить).

Тип запроса обуславливает то, в каком режиме будет работать скрипт:

* При формировании GET запроса - режим ping sweep
* При формировании POST запроса - режим http request

---

Далее, если был выбран режим ping sweep, все следующие аргументы указываются в body в формате text/json.

* `"ip_address":"значение"` - IP-адрес для сканирования
* `"num_of_hosts":"значение"` - Количество хостов

---

Если же был выбран режим http request, все следующие аргументы указываются в body в формате text/json.

* `"target":"значение"` - URL-адрес для запроса
* `"method":"значение"` - GET или POST метод
* `"headers":"значение"` - Header'ы в формате Имя:Значение через пробел
* `"payload":"значение"` - payload строка в произвольной форме
  * Игнорируется, если был указан метод запроса GET

## Пример использования

GET запрос из Postman на `127.0.0.1:8081/scan`, body:
```json
{"ip_address":"192.168.1.0", "num_of_hosts":"4"}
```

POST запрос из Postman на `127.0.0.1:8081/sendhttp`, body:
```json
{"target":"https://ya.ru", "method":"GET", "headers":"Content-Type:text"}
```

POST запрос из Postman на `127.0.0.1:8081/sendhttp`, body:
```json
{"target":"https://ya.ru", "method":"POST", "headers":"Content-Type:text", "payload":"lol"}
```
