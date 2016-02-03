

from replication_manager import ReplicationManager

rm = ReplicationManager()
rm.add_node("n1")
rm.add_node("n2")
rm.add_node("n3")

rm.add_actor("a1", 0.99)
rm.add_actor("a3", 0.7)

rm.lost_node("a1","n1")
