
class StaticModel(object):
	"""
	A very simple model for calcutaling the number of replicas given 
	a certain reliability for each component and a required level of reliability
	Assumes that the input list with the reliabilites is sorted by priority (1 st element to be scheduled first)
	"""

	# reliabilites is a list, #units long
	def __init__(self, reliabilities):
		self.reliabilities = reliabilities

	# Calculate how many replicas is needed
	def nbr_of_replicas(self, reliability_level):
		nbr = 1
		p = 1 - self.reliabilities[0]

		while (1 - p) < reliability_level:
			# Check that we don't use more resources that we have access to
			if nbr > len(self.reliabilities) - 1:
				return -1
			p = p * (1 - self.reliabilities[nbr])
			nbr = nbr + 1
		return nbr