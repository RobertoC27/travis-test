import unittest
class simpleTest (unittest.TestCase):
	def setUp(self):
		print 'hehe'
		self.assertTrue(1,1)
	def tearDown(self):
		print 'pasado con exito'
	def test_extra(self):
		print 'placeholder'
	if __name__ == '__main__':
		unittest.main()