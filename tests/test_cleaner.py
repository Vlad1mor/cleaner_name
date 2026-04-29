import pandas as pd
import pytest
from src.cleaner import keep_only_russian_letters, clean_dataframe


def test_keep_only_russian_letters_basic():
    assert keep_only_russian_letters("Владимир") == "Владимир"
    assert keep_only_russian_letters("Вла димир") == "Владимир"
    assert keep_only_russian_letters("Вла,димир") == "Владимир"
    assert keep_only_russian_letters("Вла-димир") == "Владимир"
    assert keep_only_russian_letters("Вла/димир") == "Владимир"
    assert keep_only_russian_letters("Вла1димир") == "Владимир"
    assert keep_only_russian_letters("Вла!!!димир") == "Владимир"
    assert keep_only_russian_letters("1223") == ""
    assert keep_only_russian_letters("avg") == ""
    assert keep_only_russian_letters(" ") == ""

def test_clean_dataframe_removes_non_russian():
    df = pd.DataFrame({
        'name': ['Владимир', 'John', 'Петр', '123', ''],
        'city': ['Москва', 'New York', 'СПБ', '!!!', '']
    })
    result = clean_dataframe(df, columns=['name', 'city'])
    expected = pd.DataFrame({
        'name': ['Владимир','Петр'],
        'city': ['Москва', 'СПБ']
    })
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
