from unittest import TestCase

from goroscope_bot import command_answer
from goroscope_bot import generate_advice
from goroscope_bot import first
from goroscope_bot import second
from goroscope_bot import third
from goroscope_bot import second_add


class TestHoroscopeBot(TestCase):
    def test_calc(self) -> None:
        cases = [
            ("Hi! I can tell you your horoscope for today", "/start"),
            ("This bot can predict your horoscope for today. To get started, write /start", "/help"),
            ("I don't understand you. Please write /help.", "bla bla bla")
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected,  command_answer(args))

    def test_advice(self) -> None:
        advices_list = first + second + second_add + third
        check_if_contains = any(substring in generate_advice() for substring in advices_list)
        self.assertTrue(check_if_contains)