import re


def keep_only_russian_letters(text: str) -> str:
    """
    Удаляет все строки, кроме русских букв
    :param text: Вла,дими р
    :return: Владимир
    """
    if not isinstance(text, str):
        text = str(text)
    return re.sub(r"[^а-яА-ЯёЁ]", "", text)


def clean_dataframe(df, columns=None):
    """
    Применяет отчистку ко всем указанным колонка
    Удаляет строки, если колонки пустые
    """
    if columns is None:
        columns = df.select_dtypes(include=["object"]).columns.tolist()
    for col in columns:
        df[col] = df[col].astype(str).apply(keep_only_russian_letters)

    for col in columns:
        df = df[df[col] != ""]
    return df
