class Node():
	def __init__(self,item):
		self.element = item
		self.next = None


# 创建单链表类
class SingleLinkList():
	def __init__(self):
		self.header = None # 头指针
		self.length = 0

	# 1.判断是否为空
	def isEmpty(self):
		if self.header == None:
			return True
		else:
			return False


	# 2.头部插入
	def add(self,node):
		if self.isEmpty():
			self.header = node
		else:
			node.next = self.header
			self.header = node
		self.length += 1


	# 3.尾部插入
	def append(self,node):
		currentNode = self.header
		if self.isEmpty():
			self.add(node)
		else:
			while (currentNode.next != None):
				currentNode = currentNode.next # 找到最后的节点
			currentNode.next = node
		self.length += 1


	# 4.指定位置插入
	def insert(self,node,index):
		currentNode = self.header
		if index > self.length + 1 or index <= 0:
			print('插入位置不对，请重新选择位置')
		
		if index == 1:
			self.add(node)
			self.length += 1
		elif index == 2:
			node.next = self.header.next
			self.header.next = node
			self.length += 1
		else:
			for i in range(1,index-1):
				currentNode = currentNode.next
			node.next = currentNode.next
			currentNode.next = node
			self.length += 1









