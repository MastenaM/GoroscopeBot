from unittest import TestCase

from project_213 import calc


class TestProject213(TestCase):
    def test_calc(self) -> None:
        """`calc` should sum two numbers."""
        cases = [
            (3, (1, 2)),
            (0, (-1, 1)),
        ]
        for expected, args in cases:
            with self.subTest(expected):
                self.assertEqual(expected, calc(*args))
