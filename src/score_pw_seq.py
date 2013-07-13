'''
@author: Seungho@04/2013
@change: Bolun@04/2013
'''

class score_pw_seq():
	def __init__(self, username, password):
		self.usn = username
		self.pwd = password
		self.keyboard = ["`1234567890-=", "=-0987654321`",
						"~!@#$%^&*()_+", "+_)(*&^%$#@!~",
						"qwertyuiop[]\\", "\\][poiuytrewq",
						"QWERTYUIOP{}|", "\][POIUYTREWQ",
						"asdfghjkl;'", "';lkjhgfdsa",
						"ASDFGHJKL:\"", '";LKJHGFDSA',
						"zxcvbnm,./", "/.,mnbvcxz",
						"ZXCVBNM<>?", "/.,MNBVCXZ"]
		self.alphabet = "abcdefghijklmnopqrstuvwxyz"
		self.sub_pwd = []
		for i in range(0, len(self.pwd)-2):
			for j in range(i+2, len(self.pwd)):
				self.sub_pwd.append(self.pwd[i:j+1])
		#print self.sub_pwd
		self.sub_pwd_b = []
		for i in range(0, len(self.pwd)-7):
			if self.pwd[i:i+8].isdigit():
				self.sub_pwd_b.append(self.pwd[i:i+8])
		for i in range(0, len(self.pwd)-5):
			if self.pwd[i:i+6].isdigit():
				self.sub_pwd_b.append(self.pwd[i:i+6])
		#print self.sub_pwd_b
	'''
		@summary: it can detect keyboard sequence in subpassword now and give a reasonable score for it
				we take sequence >= 3 and neglect two letter sequency such as "ab" or "56".
				we also consider reversed-ordered sequence of keyboard row
		@change: Bolun Huang
	'''
	def keyboard_seq(self):
		k_seq = []
		for i in self.sub_pwd:
			for k in self.keyboard:
				if ( i in k ):
					k_seq.append(i)
				else: pass
		#print k_seq
		k_seq_2 = list(k_seq)
		#print k_seq_2
		#print k_seq
		for i in range(0, len(k_seq_2)):
			for j in range(0, len(k_seq_2)):
				if k_seq_2[i] in k_seq_2[j] and k_seq_2[i] != k_seq_2[j]:
					k_seq.remove(k_seq_2[i])
					break
		#print k_seq
		ii = ''
		ii=''.join(k_seq)
		#print ii
		## return score according to the length of keyboard sequence
		if len(ii) == 0:
			return 10
		elif len(ii) >=3 and len(ii) <6:
			return 7
		elif len(ii) >= 6 and len(ii) < 9:
			return 4
		else: # keyboard sequence >= 9
			return 1

	'''
		@summary: it can detect alphabetical sequence in subpassword now and give a reasonable score for it
				we take sequence >= 3 (e.g. abc, or efgh)and neglect two letter sequency such as "ab" or "xy"
		@change: Bolun Huang
	'''
	def alphabet_seq(self):
		a_seq = []
		for i in self.sub_pwd:
			if ( i in self.alphabet):
				a_seq.append(i)
		#print a_seq
		a_seq_2 = list(a_seq)
		#print a_seq_2
		#print a_seq
		for i in range(0, len(a_seq_2)):
			for j in range(0, len(a_seq_2)):
				if a_seq_2[i] in a_seq_2[j] and a_seq_2[i] != a_seq_2[j]:
					a_seq.remove(a_seq_2[i])
					break
		#print a_seq
		ii = ''
		ii=''.join(a_seq)
		#print ii
		## return score according to the length of keyboard sequence
		if len(ii) == 0:
			return 10
		elif len(ii) >=3 and len(ii) <6:
			return 7
		elif len(ii) >= 6 and len(ii) < 9:
			return 4
		else: # keyboard sequence >= 9
			return 1
	'''
		@summary: detect whether there are suspected birthday within the password & username
		@change: Bolun Huang
	'''
	def is_Bday_pwd(self):
		if len(self.sub_pwd_b) == 0:
			return 10
		score = 10
		for i in self.sub_pwd_b:
			if ( len(i) == 6):
				# mm dd yy
				if (int(i[0:2]) >= 1 and int(i[0:2]) <=12 and int(i[2:4]) >= 1 and int(i[2:4]) <= 31 and int(i[4:6]) >= 0 and int(i[4:6]) <=99):
					score = 5
					break
				# dd mm yy
				elif (int(i[2:4]) >= 1 and int(i[2:4]) <=12 and int(i[0:2]) >= 1 and int(i[0:2]) <= 31 and int(i[4:6]) >= 0 and int(i[4:6]) <=99):
					score = 5
					break
				# yy mm dd
				elif (int(i[0:2]) >= 0 and int(i[0:2]) <=99 and int(i[2:4]) >= 1 and int(i[2:4]) <=12 and int(i[4:6]) >= 1 and int(i[4:6]) <= 31):
					score = 5
					break
			elif ( len(i) == 8):
				# mm dd yyyy
				if ( int(i[0:2]) >= 1 and int(i[0:2]) <=12 and int(i[2:4]) >= 1 and int(i[2:4]) <= 31 and int(i[4:8]) >= 1914 and int(i[4:8]) <= 2013):
					score = 5
					break
				# dd mm yyyy
				elif ( int(i[2:4]) >= 1 and int(i[2:4]) <=12 and int(i[0:2]) >= 1 and int(i[0:2]) <= 31 and int(i[4:8]) >= 1914 and int(i[4:8]) <= 2013):
					score = 5
					break
				# yyyy mm dd
				elif ( int(i[4:6]) >= 1 and int(i[4:6]) <=12 and int(i[6:8]) >= 1 and int(i[6:8]) <= 31 and int(i[0:4]) >= 1914 and int(i[0:4]) <= 2013):
					score = 5
					break
		return score	
			
	def is_Bday(self):
		#print 'xx', self.is_Bday_pwd()
		idc = 0
		for p in self.sub_pwd_b:
			if p in self.usn:
				idc = 1
				break
		if self.is_Bday_pwd() == 5 and idc == 1:
			return 1
		else:
			return self.is_Bday_pwd()

'''
	def isallNumber(self):
		if (self.pwd.isdigit()): return 1
		else: return 10
'''
'''
def main():
	sps = score_pw_seq('sfwerwerwe','sdfdswerwerwe')
	print sps.keyboard_seq()
	print sps.alphabet_seq()
	t = sps.is_Bday()
	print t
if __name__ == '__main__':
	main()
'''