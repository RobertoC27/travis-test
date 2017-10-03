import unittest
class simpleTest (unittest.TestCase):
	def setUp(self):
		print 'hehe'
	def pruebanum2(self):
		print 'pasado con exito'
	def extra(self):
		print 'placeholder'
	if __name__ == '__main__':
		unittest.main()