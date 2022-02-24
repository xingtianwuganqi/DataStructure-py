class Stack:
	def __init__(self):
		self.items = []

	# 判空
	def isEmpty(self):
		return self.items == []

	#入栈
	def push(self,item):
		self.items.append(item)

	#出栈
	def pop(self):
		return self.items.pop()

	#peek 查看
	def peek(self):
		return self.items[len(self.items) - 1]

	#size 长度
	def size(self):
		return len(self.items)


# 栈的应用：括号匹配算法

def parChecker(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == '(':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()
		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False




if __name__ == '__main__':
	value = parChecker('(())')
	print(value)










