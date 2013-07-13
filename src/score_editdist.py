import re
'''
	@author: Shyam S Ramachandran
	@copyright: sr DOT shyam AT gmail DOT com
	@change: Bolun Huang 4/2013
	@ref: http://code.activestate.com/recipes/576874-levenshtein-distance/
	@summary:Calculates the Levenshtein distance of 2 strings
'''

class score_editdist():
	def __init__(self, username, password):
		self.uname = username
		self.passwd = password

	def ratePassword(self):
		distance = self.levenshtein()
		if distance >= 12:
			return 10
		if distance < 12 and distance >= 9:
			return 9
		if distance < 9 and distance >= 7:
			return 8
		if distance == 6:
			return 7
		if distance == 5:
			return 6
		if distance == 4:
			return 5
		if distance == 3:
			return 4
		if distance == 2:
			return 3
		if distance == 1:
			return 2
		if distance == 0:
			return 1
		
	def levenshtein(self):
		l1 = len(self.uname)
		l2 = len(self.passwd)

		matrix = [range(l1 + 1)] * (l2 + 1)
		for zz in range(l2 + 1):
			matrix[zz] = range(zz,zz + l1 + 1)
		for zz in range(0,l2):
			for sz in range(0,l1):
				if self.uname[sz] == self.passwd[zz]:
					matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz])
				else:
					matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
		return matrix[l2][l1]

#test = score_editdist('abcabcab','abcabdes')
#print test.ratePassword()
