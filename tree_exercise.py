
"""This is an exercise where you can create a tree with a ilimited number of nodes;
every node has it's own name, parent and a weight depending on how many ancestors
it has... the purpose of this script is that find the commond parent between two
nodes. You can only create one root and you can only create a node but not modify its
own properties."""


class Tree():
	root = None 

	def __init__(self, *root): #we can create a tree with or whitout a root
	 	self.list_nodes = []
	 	if root: self.root = root[0]#if we send root as parameter, then automatically 
	 	print("Tree created succesfully") #act as a root

	def addRoot(self,root): #we can add a root after create the tree
		if self.root == None:
			self.root = root
			print("Root created succesfully")
		else: print("There is a root!")

	def addNode(self, node):
	 	self.list_nodes.append(node)
	 	print("Node added")

	def delNode(self, node):
	 	self.list_nodes.remove(node)
	 	print("Node deleted")

	def findCommondParent(self, node1, node2):
	 	if node1.getParent() is node2.getParent(): #first we check directly if their parent is the same
	 		print("Commond parent is: ", node1.getParent().getName())
	 	elif node1.getWeight() < node2.getWeight():#if isn't then check for the 
	 		self.findCommondParent(node1, node2.getParent())#heaviest and the other one
	 	else:
	 		self.findCommondParent(node1.getParent(), node2)#using recursion we find the commond parent

class Node():
	def __init__(self, name, *parent):#all nodes need to have name, parent and weight
		self.name = name  #the weight is determinated on every parenting level, it means
		if parent[0] == None:#that root has weight zero; so it node has no parent then
			self.parent = self#parent its itself and weight goes to zero
			self.weight = 0  
		else:
			self.parent = parent[0] 
			self.weight = self.parent.getWeight()+1#auto increment weight on every level  

	def getName(self):
		return self.name  

	def getParent(self):
		return self.parent  

	def getWeight(self):
		return self.weight  

if __name__ == '__main__':
	
	node_1 = Node("1", None)
	tree = Tree()
	tree.addRoot(node_1)
	node_2 = Node("2", node_1)
	node_3 = Node("3", node_1)
	node_4 = Node("4", node_1)
	node_5 = Node("5", node_2)
	node_6 = Node("6", node_2)
	node_7 = Node("7", node_3)
	node_14 = Node("14", node_5)
	node_16 = Node("16", node_6)
	tree.findCommondParent(node_16, node_5)


