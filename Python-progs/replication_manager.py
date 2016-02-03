# Small test script for Static model
import subprocess, math

class ReplicationManager(object):
	"""
	A central replication manager. 
	Examines the connected nodes reliabilities and replicates tasks in order to achieve a given reliability level 
	"""
	def __init__(self):
		self.nodes = {}
		self.actors = {}
		self.actor_ids = {}
	
	def add_node(self, node_id):
		self.nodes[node_id] = None
		self._update_reliabilities()
		print "Added a node with id:", node_id
	
	def add_actor(self, actor_id, reliability_level):
		self.actor_ids[actor_id] = reliability_level
		self._update_reliabilities()
		n = self._nbr_of_replicas(actor_id)
		for k in range(0, n-1):
			self._relicate_actor_to(self.nodes[k], actor_id)
		print "Added an actor with id:", actor_id, "and reliability level", reliability_level

	def lost_node(self, actor_id, node_id):
		del self.nodes[node_id]
		print "We lost node:", node_id

	def _update_reliabilities(self):
		# Examine each nodes reliability level and update the list.
		for node in self.nodes:
			self.nodes[node] = 0.8
		print "Updated the reliabilities"

	def _relicate_actor_to(self, node_id, actor_id):
		n = _nbr_of_replicas(actor_id)
		print "Replicated actor to node", node

	def _nbr_of_replicas(self, actor_id):
		nbr = 1
		p = 1 - self.nodes[0]
		while (1 - p) < reliability_level:
			# Check that we don't use more resources than we have access to
			if nbr > len(self.nodes) - 1:
				return -1
			p = p * (1 - self.reliabilities[nbr])
			nbr = nbr + 1
		return nbr	


"""
# Here are several alternatives for calculating the reliabilities for available resources. 

1. As simple as entering constants reliabilities
2. From the MTTFs for the resources, but I think I have to define a "repair time" for when the resource goes down in order to get a reliability which is timeindependent
3. Similar to #2 but instead of estimating MTR we use the timedependent formula and set t = exection time for that specific applications execution time
4. Each components reliability is calculated from a number of factors, such as (probability that the hardware works), (probability that the software works) etc
	One factor is the reliability from number 4 above. I believe this is the best model since it quite general and takes several facots into account
5. Uses "1 - the average load" directly from the machine 
"""

#1
#reliabilities = [0.7, 0.6, 0.5, 0.6, 0.9, 0.8, 0.9]

#2
"""
MTTFs = [1000.0, 3000.0, 5000.0, 1000.0, 3000.0, 4000.0, 5000.0]
reliabilities = []
for n in range(1, len(MTTFs)):
	reliabilities.append(MTTFs[n] / (MTTFs[n] + 1))	#Estimated MTR on 1 hour
"""

#3
# R(t) = e^(-t/MTBF)
"""
MTBFs = [100.0, 300.0, 500.0, 100.0, 300.0, 400.0, 500.0]
t = 0.1 #execution time
reliabilities = []
for n in range(0, 6):
	reliabilities.append(math.e ** (-t/MTBFs[n]))	
"""

#4
"""
MTBFs = [100.0, 300.0, 500.0, 100.0, 300.0, 400.0, 500.0, 700.0, 800.0, 900.0, 1000.0]
SW_probabilities = [0.96, 0.999, 0.99, 0.95, 0.97, 0.95, 0.9, 0.85, 0.95, 0.95]
Network_probabilities = [0.95, 0.85, 0.87, 0.89, 0.83, 0.7, 0.99, 0.9, 0.9, 0.9]
t = 0.1 #execution time
reliabilities = []
for n in range(0, len(MTBFs) - 1):
	print (math.e ** (-t/MTBFs[n])) * SW_probabilities[n] * Network_probabilities[n]
	reliabilities.append((math.e ** (-t/MTBFs[n])) * SW_probabilities[n] * Network_probabilities[n])
"""

#5
# More dynamic approach
# Derive reliabilites from the machine average load during the last minute (or if you want the last 5 or 15 minutes). 
# $1 - last minute, $2 - last 5 minutes and $3 - last 15 minutes
"""
p = subprocess.Popen("(awk \'{printf \"%s/\", $1}\' /proc/loadavg; nproc;) | bc -l", stdout = subprocess.PIPE, shell= True)	
(load_avg, error) = p.communicate();

reliabilities  = []
p = 1 - float(load_avg)
for i in range(1,10):
	reliabilities.append(p)
"""