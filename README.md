# MIFIIB-HW-07

Реализация сквозной задачи по седьмому модулю вводного курса.

> **!** | Если вы зашли сюда и не понимаете, о чём идёт речь, сохраняйте спокойствие: мне временно потребовалось сделать этот репозиторий публичным в ходе обучения на курсах, чтобы это смогли проверить преподаватели (важно было разместить это общедоступным и именно на GitHub). Можете заниматься своими делами и не обращать внимание на сей казус с моей стороны.

## API

Теперь функции do_ping_sweep и send_http_request возвращают результаты своего выполнения в виде словарей. Подробности в процессе добавления.

## Тесты

```python
result_func_1 = do_ping_sweep("192.168.0.1", 3)
result_func_2 = send_http_request("https://pastebin.com/raw/7wmiJKnG")

print("\nReturn values of both functions:", end = "\n\n")
print(result_func_1, end = "\n\n")
print(result_func_2["Status"], end = "\n\n")
print(result_func_2["Headers"], end = "\n\n")
print(result_func_2["Content"])
```
