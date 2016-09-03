import unittest
import re

class TestExercises(unittest.TestCase):
	def test_2_1(self):
		pattern_a = r'0*42'
		re_a = re.compile(pattern_a)
		self.assertTrue(re_a.fullmatch('42'))
		self.assertTrue(re_a.fullmatch('042'))
		self.assertTrue(re_a.fullmatch('0000042'))
		self.assertFalse(re_a.fullmatch('420'))
		self.assertFalse(re_a.fullmatch('0420'))
		self.assertFalse(re_a.fullmatch('43'))

		pattern_b = r'(?!0*42$)\d+'
		re_b = re.compile(pattern_b)
		self.assertFalse(re_b.fullmatch('42'))
		self.assertFalse(re_b.fullmatch('042'))
		self.assertFalse(re_b.fullmatch('0000042'))
		self.assertTrue(re_b.fullmatch('420'))
		self.assertTrue(re_b.fullmatch('0420'))
		self.assertTrue(re_b.fullmatch('43'))
		
		pattern_c = r'^0*([1-9]\d{2,}|[5-9]\d+|4[3-9])'
		re_c = re.compile(pattern_c)
		self.assertFalse(re_c.fullmatch('42'))
		self.assertFalse(re_c.fullmatch('042'))
		self.assertFalse(re_c.fullmatch('0000042'))
		self.assertTrue(re_c.fullmatch('420'))
		self.assertFalse(re_c.fullmatch('41'))
		self.assertFalse(re_c.fullmatch('041'))		
		self.assertTrue(re_c.fullmatch('0420'))
		self.assertTrue(re_c.fullmatch('43'))
		self.assertTrue(re_c.fullmatch('98'))


if __name__ == '__main__':
	unittest.main()