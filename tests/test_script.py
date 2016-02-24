
from replication_manager import ReplicationManager

rm = ReplicationManager()
rm.add_node("n1")
rm.add_node("n2")
rm.add_node("n3")
rm.add_node("n4")
print ""
rm.add_actor("a1", 0.99)
print ""
rm.print_nodes("a1")
print ""
rm.add_actor("a2", 0.9)
print ""
rm.print_nodes("a2")
print ""
rm.lost_node("n1")
print ""
rm.print_nodes("a1")
print ""
rm.print_nodes("a2")