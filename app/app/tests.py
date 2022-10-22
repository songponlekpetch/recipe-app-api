"""
Sample test
"""
from django.test import TestCase

from app import calc


class CalcTests(TestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtract numbers."""
        res = calc.subtract(5, 6)

        self.assertEqual(res, 1)
