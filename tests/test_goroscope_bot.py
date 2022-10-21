from unittest import TestCase

from goroscope_bot import command_answer
from goroscope_bot import generate_advice
from goroscope_bot import first
from goroscope_bot import second
from goroscope_bot import third
from goroscope_bot import second_add


class TestHoroscopeBot(TestCase):
    def test_command(self) -> None:
        cases = [
            ("Hi! I can predict your success in the subject and give you a piece of advice.", "/start"),
            ("This bot can predict your success in the subject. To get started, write /start", "/help"),
            ("I don't understand you. Please write /help.", "bla bla bla")
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected,  command_answer(args))

    def test_advice(self) -> None:
        advice = generate_advice()
        check1 = any(substring in advice for substring in first)
        check2 = any(substring in advice for substring in second)
        check3 = any(substring in advice for substring in second_add)
        check4 = any(substring in advice for substring in third)
        self.assertTrue(check1 and check2 and check3 and check4)

