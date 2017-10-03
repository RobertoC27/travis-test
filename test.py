import unittest

class Simple(unittest.TestCase):
	def setUp(self):
		print 'hola'
	def testMe(self):
		print 'nuay'
	def test_malo(self):
		print 'va pasar'
		#raise ValueError()
if __name__=="__main__":
    unittest.main()