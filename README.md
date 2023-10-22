# FastAPI-приложение: получения случайных вопросов для викторины
## Описание

В сервисе реализовано REST API, принимающее на вход POST запросы с содержимым вида {"count": integer}
После получения запроса сервис, в свою очередь, запрашивает с публичного [API (англоязычные вопросы для викторин)](https://jservice.io/api/random?count=1) указанное в полученном запросе количество вопросов.
Далее, полученные ответы сохраняются в базе данных в следующем формате: 
- ID вопроса
- Текст вопроса
- Текст ответа
- Дата создания вопроса.

В случае, если в БД уже имеется сохраненный вопрос из запроса, такой вопрос будет пропущен. Ответ на PoST-запрос будет возврвщен последний сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.

### Пример POST-запроса

**Запрос** - *http://host/questions?count=1*


**Ответ** 
```JSON
{
  "id": 25414,
  "question": "Ellen Terry was acclaimed for her 1875 performance in this role in \"The Merchant of Venice\"",
  "answer": "Portia",
  "created_at": "2022-12-30T18:48:00.275000"
}
```

## Установка
В приложении используется база данных PostgreSQL. Для корректной работы приложения, необходимо выполнить следующие шаги:
1. в корневой директории проекта создать новый файл с названием .env и скопировать в него все названия переменных окружения из файла .env.sample.
2. заполнить значения переменных в файле .env
3. находясь в корневой директории, последовательно запустить в терминале команды:
   ```bash
   docker-compose build
   docker-compose build
   ```
