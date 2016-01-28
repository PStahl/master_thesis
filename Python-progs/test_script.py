# Small test script for Static model
import subprocess

from static_model import StaticModel

"""
# Here are three alternatives for calculating the reliabilities for available resources
#1 is as simple as entering constants
#2 From the MTTFs for the resources, but I think I have to define a "repair time" for then the resource goes down in order to get a reliability
#3 uses "1 - the average load" directly from the machine 
"""


#1
#reliabilities = [0.7, 0.6, 0.5, 0.6, 0.7, 0.8, 0.9]

#2
"""
MTTFs = [1000.0, 3000.0, 5000.0, 1000.0, 3000.0, 4000.0, 5000.0]
reliabilities = []
for n in range(1, len(MTTFs)):
	reliabilities.append(MTTFs[n] / (MTTFs[n] + 1))
"""

#3
#Derive reliabilites from the machine average load during the last minute (or if you want the last 5 or 15 minutes). 
# $1 - last minute, $2 - last 5 minutes and $3 - last 15 minutes
p = subprocess.Popen("(awk \'{printf \"%s/\", $1}\' /proc/loadavg; nproc;) | bc -l", stdout = subprocess.PIPE, shell= True)	
(load_avg, error) = p.communicate();

reliabilities  = []
p = 1 - float(load_avg)
for i in range(1,10):
	reliabilities.append(p)


#Send the reliabilities to the model and print the result
statmodel = StaticModel(reliabilities)
print statmodel.nbr_of_replicas(0.99999)
