import re
'''
    Author: Shyam S Ramachandran
    sr DOT shyam AT gmail DOT com
    @summary: xx
'''

class score_comp_usn_pwd():
    def __init__(self, username, password):
        self.uname = username
        self.passwd = password

    def ratePassword(self):
		numset = 0
		j=1
		a=set()
		b=set()
		while True:
			for i in range(len(self.uname)-j+1):
				a.add(self.uname[i:i+j])
			if j==len(self.uname):
				break
			j+=1
	
		for n in a:
			length = len(n)
			if length>=1:
				b.add(n)
		greatest=0
		length1=0
		str1=[]
		for k in b:
			if k in self.passwd:
				length1 = len(k)
				if length1>greatest:
					str1=k
					greatest=length1
					continue
        
		if greatest>=numset:
			#print b
			occur = float(float(greatest) / float(len(self.passwd)))*100
			#print occur
			tempuname = self.uname
			temppasswd = self.passwd
			tempexists = str1
			if occur >90 and occur<=100:
				return 1
			if occur >80 and occur<=90:
				return 2
			if occur >70 and occur<=80:
				return 3
			if occur >60 and occur<=70:
				return 4
			if occur >50 and occur<=60:
				return 5
			if occur >40 and occur<=50:
				return 6
			if occur >30 and occur<=40:
				return 7
			if occur >20 and occur<=30:
				return 8
			if occur >10 and occur<=20:
				return 9
			if occur >=0 and occur<=10:
				return 10

#test = compUnamePassword('wwrw','wwrwe')
#print test.ratePassword()

