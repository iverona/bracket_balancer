import unittest
from bracketbalancer import isBalanced

class TestBracketBalancer(unittest.TestCase):

	def test_positive_simple(self):
		self.assertTrue(isBalanced("({[]})"))

	def test_positive_complex(self):
		self.assertTrue(isBalanced("[({[{({(({{[]}}))})}]})]"))

	def test_negative_wrongString(self):
		self.assertFalse(isBalanced("[ab]"))

	def test_negative_oddString(self):
		self.assertFalse(isBalanced("[]("))

	def test_negative_simple(self):
		self.assertFalse(isBalanced("([)]"))

	def test_negative_complex(self):
		self.assertFalse(isBalanced("{[({([])})}]"))

	def test_negative_emptyString(self):
		self.assertTrue(isBalanced(""))


if __name__ == '__main__':
    unittest.main()
