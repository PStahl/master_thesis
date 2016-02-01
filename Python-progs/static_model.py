class StaticModel(object):
	"""
	Very simple code for calcutaling the number of replicas needed, 
	given a certain reliability for each component and a required level of reliability
	"""

	# reliabilites is a list, #units long
	def __init__(self, reliabilities):
		self.reliabilities = reliabilities

	"""
	Calculate how many replicas is needed
	Return the number of replicas needed iff there is enough components/units, otherwise -1.
	"""
	def nbr_of_replicas(self, reliability_level):
		# Uncomment the following piece of code if you want the list to be sorted before continuing. 
		# Do we want to reverese the list or not? Maybe better to keep the highly reliable components to something that actualy requires them
		
		# (self.reliabilities).sort()
		# (self.reliabilities).reverse()

		nbr = 1
		p = 1 - self.reliabilities[0]
		while (1 - p) < reliability_level:
			# Check that we don't use more resources than we have access to
			if nbr > len(self.reliabilities) - 1:
				return -1
			p = p * (1 - self.reliabilities[nbr])
			nbr = nbr + 1
		return nbr		

	#def estimate_reliability(self, parameters):
	#maybe this class should be able to estimate a components reliability from a number of parameters