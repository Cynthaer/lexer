import unittest
import re

class TestLexer(unittest.TestCase):
	def test_float(self):
		pattern = r'''
					[+-]? # leading sign
					( (\d+(\.\d*)?) | (\.\d+) ) # body
					([eE][+-]?\d+)? # exponent
				  	'''
		re_float = re.compile(pattern, re.X)
		self.assertTrue(re_float.fullmatch('1'))
		self.assertTrue(re_float.fullmatch('3.14'))
		self.assertTrue(re_float.fullmatch('-3.'))
		self.assertTrue(re_float.fullmatch('.23'))
		self.assertTrue(re_float.fullmatch('3e+4'))
		self.assertTrue(re_float.fullmatch('11.22e-3'))
		self.assertTrue(re_float.fullmatch('8e3'))
		self.assertFalse(re_float.fullmatch('1.2.3'))


if __name__ == '__main__':
	unittest.main()