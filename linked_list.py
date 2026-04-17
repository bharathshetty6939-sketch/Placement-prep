class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1= Node(10)
node2= Node(20)
node1.next=node2
print("node 1 data",node1.data)
print("node 2 data(via node1)",node1.next.data)
