from src.cleaner import keep_only_russian_letters


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