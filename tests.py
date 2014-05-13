import unittest
from bracketbalancer import is_balanced

class TestBracketBalancer(unittest.TestCase):

	def test_positive_simple(self):
		self.assertTrue(is_balanced("({[]})"))

	def test_positive_complex(self):
		self.assertTrue(is_balanced("[({[{({(({{[]}}))})}]})]"))

	def test_positive_otherCharactersString(self):
		self.assertTrue(is_balanced("[ab]"))

	def test_negative_oddString(self):
		self.assertFalse(is_balanced("[]("))

	def test_negative_simple(self):
		self.assertFalse(is_balanced("([)]"))

	def test_negative_complex(self):
		self.assertFalse(is_balanced("{[({([])})}]"))

	def test_positive_emptyString(self):
		self.assertTrue(is_balanced(""))


if __name__ == '__main__':
    unittest.main()
