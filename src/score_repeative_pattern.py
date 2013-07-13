import re
'''
Author: Shyam S Ramachandran
sr DOT shyam AT gmail DOT com

'''
class score_repeative_pattern():
	def __init__(self, password):
		self.passwd = password

	def ratePassword(self):
		a = list()
		j=10
		b=list()
		for x in xrange(len(self.passwd)/2):
			a=list()
			name = self.passwd[0:x+1]
			start = x+1
			l = x+1
			#print 'Length: '+str(l)
			for y in xrange((len(self.passwd)/l)-1):
				#print y
				a.append(self.passwd[start:start+l])
				start = start+l

			a.append(name)

			#print a
			if all(x == a[0] for x in a):
				j=len(a[0])
				break
		if len(self.passwd) == len(a)*j:
			return 1
		else:
			return 10

test = score_repeative_pattern('aAaAaAaA')
print test.ratePassword()
