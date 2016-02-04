

from replication_manager import ReplicationManager

rm = ReplicationManager()
rm.add_node("n1")
rm.add_node("n2")
rm.add_node("n3")
rm.add_node("n4")

rm.add_actor("a1", 0.99)
rm.print_nodes("a1")

rm.add_actor("a2", 0.7)
rm.print_nodes("a2")

rm.lost_node("n1")
rm.print_nodes("a1")
rm.print_nodes("a2")