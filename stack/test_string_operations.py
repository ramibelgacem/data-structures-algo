# -*- coding: utf-8 -*-
from string_operations import main


def test_main_01():
    assert main("2 6 DUP POP 1 + 11 - -") == 2


def test_main_push_unallowed_number():
    assert main("1024 -") == -1


def test_main_addition_empty_stack():
    assert main("8 4 + POP DUP") == -1


def test_main_stack_addition_with_one_element():
    assert main("8 4 + -") == -1


def test_main_stack_overflow():
    assert main("1000 25 +") == -1


def test_main_stack_empty_at_the_end():
    assert main("21 25 + POP") == -1
