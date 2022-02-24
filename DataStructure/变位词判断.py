# 变位词：两个词之间存在组成字母的重新排列关系
'''
法①：检查标记【时间复杂度为O(n2)】

　　思路：检查第一个字符串中的所有字符是不是都在第二个字符串中出现。 
如果能够把每一个字符都“检查标记”一遍，那么这两个字符串就互为变位词。
检查标记一个字符 要用特定值 None 来代替，作为标记。
然而，由于字符串不可变，首先要把第二个字符串转化成一个列表。
第一个字符串中的每一个字符都可以在列表的字符中去检查，如果找到，就用 None 代替以示标记。
'''
def anagramSolution1(s1,s2):
	alist = list(s2)
	pos1 = 0
	stillOK = True
	while pos1 < len(s1) and stillOK:
		pos2 = 0
		found = False
		while pos2 < len(alist) and not found:
			if s1[pos1] == alist[pos2]:
				found = True
			else:
				pos2 = pos2 + 1

		if found:
			alist[pos2] = None
		else:
			stillOK = False
		pos1 = pos1 + 1

	return stillOK


if __name__ == '__main__':
	value = anagramSolution1('abcd','cdba')
	print(value)