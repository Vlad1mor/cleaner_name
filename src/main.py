import os
import sys
import pandas as pd
from dotenv import load_dotenv

from cleaner import clean_dataframe
from db_loader import load_to_postgres

load_dotenv()

DATA_DIR = "data"
TABLE_NAME = "cleaned_names"
TXT_COLUMN_NAME = "cleaned_name"

DB_URL = (
    f"postgresql://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', '')}"
    f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'postgres')}"
)

def find_file_by_name(filename):
    """Возвращает полный путь к файлу в папке DATA_DIR, если он существует."""
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    return file_path

def read_file(file_path):
    """Читает файл в зависимости от расширения."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.csv':
        return pd.read_csv(file_path)
    elif ext in ('.xlsx', '.xls'):
        return pd.read_excel(file_path)
    elif ext == '.json':
        return pd.read_json(file_path)
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
        return pd.DataFrame({TXT_COLUMN_NAME: lines})
    else:
        raise ValueError(f"Неподдерживаемый формат: {ext}")

def main():
    if len(sys.argv) != 2:
        print("Использование: python src/main.py <имя_файла>")
        print("Файл должен находиться в папке data/")
        return

    filename = sys.argv[1]
    try:
        file_path = find_file_by_name(filename)
    except FileNotFoundError as e:
        print(e)
        return

    print(f"Обрабатывается файл: {file_path}")

    df = read_file(file_path)
    print(f"Исходная размерность: {df.shape}")

    df_clean = clean_dataframe(df)
    print(f"После очистки: {df_clean.shape}")

    if df_clean.empty:
        print("Нет данных для загрузки")
        return

    load_to_postgres(df_clean, TABLE_NAME, DB_URL, if_exists='append')
    print("Готово")

if __name__ == "__main__":
    main()