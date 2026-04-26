# Russian Name Cleaner

Очищает имена от лишних символов (пунктуация, пробелы, латиница, цифры) и загружает в PostgreSQL.

## Форматы входных файлов

- .txt – каждая строка становится отдельной записью
- .csv – обрабатываются все текстовые колонки
- .xlsx / .xls – обрабатываются все текстовые колонки
- .json – обрабатываются все строковые поля


## Установка

```bash
poetry install
```

Настроить подключение к PostgreSQL в файле `.env`:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

## Запуск

```bash
python src/main.py names.txt
```

Вместо `names.txt` укажите имя вашего файла (лежит в папке `data`).

## Что делает скрипт

1. Читает файл из `data/`
2. Удаляет всё, кроме русских букв (`а-яА-ЯёЁ`)
3. Отбрасывает строки, ставшие пустыми
4. Добавляет очищенные записи в таблицу `cleaned_names`

## Проверка результата в PostgreSQL

```sql
SELECT * FROM cleaned_names LIMIT 10;
```
