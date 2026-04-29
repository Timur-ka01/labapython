# test_1.py
import pytest
from one import f


def test_generator_truncates_long_lines():
    """Проверка: строки длиннее 4 символов обрезаются до 4"""
    gen = f()
    
    # Первая строка в файле: "-46704" (5 символов с минусом)
    first_line = next(gen)
    
    assert len(first_line) == 4
    assert first_line == "-467"


def test_generator_keeps_short_lines():
    """Проверка: строки короче 4 символов не обрезаются"""
    gen = f()
    
    # Пропускаем до короткого числа (в файле есть "33", "-37", "-45")
    for line in gen:
        if len(line.strip()) <= 4:
            original_len = len(line.strip())
            assert len(line) == original_len
            break