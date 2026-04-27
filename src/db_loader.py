from sqlalchemy import create_engine, text


def load_to_postgres(df, table_name, db_url, if_exists="append"):
    """
    Загружает данные(df) в базу данных(table_name)
    """
    engine = create_engine(db_url)
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)
    print(f"Загружено {len(df)} записей в таблицу '{table_name}'")
