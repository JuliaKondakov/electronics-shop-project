from src.keyboard import KeyBoard

if __name__ == '__main__':
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert (kb.language) == "EN"

    kb.change_lang()
    assert (kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert (kb.language) == "RU"

    kb.language = 'FR'
    assert kb.language == "FR"

    try:
        kb.language = 'CH'
    except ValueError as e:
        assert str(e) == "Unsupported language: CH"

    # AttributeError: property 'language' of 'KeyBoard' object has no setter
