import unittest

from replication_manager import ReplicationManager

class TestreplicationManager(unittest.TestCase):

	def setUp(self):
		number = self.model.nbr_of_replicas(0.9999)
		self.failUnless(number == -1)

	def testOne(self):


	def testTwo(self):





def main():
	unittest.main()

if __name__ == '__main__':
	main()