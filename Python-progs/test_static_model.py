import unittest

from static_model import StaticModel

class TestStaticModel(unittest.TestCase):

	def setUp(self):
		self.reliabilities = [0.7, 0.6, 0.5, 0.6, 0.7, 0.8, 0.9]
		self.model = StaticModel(self.reliabilities)

	# Test the impossible case, when the number of required units is greater than the number of 
	# available units, i.e. the required level of reliability is not possible to meet.
	def test_one(self):
		number = self.model.nbr_of_replicas(0.9999)
		self.failUnless(number == -1)

	# Test for when the required reliability is the same as the for the first unit
	def test_two(self):
		number = self.model.nbr_of_replicas(self.reliabilities[0])
		self.failUnless(number == 1)

	# Test that it doesn't fail iff all units is required to meet the requirement
	def test_three(self):
		number = self.model.nbr_of_replicas(0.999)
		self.failUnless(number == 7)		

	# "Standard case". When a few number of units is requried. 
	def test_four(self):
		number = self.model.nbr_of_replicas(0.9)
		self.failUnless(number == 3)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
