import math

class score_freq_distr():
    '''
        @param: username
        @param: password
        @return: score according to the frequency distribution of username/password
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.f1 = open("password_letter_freq.txt","r")
        self.f2 = open("username_letter_freq.txt","r")
        self.dic_pwd = {}
        self.dic_usn = {}
        self.v_letter = ['~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','=','|','\\','}',']','{','[','"',"'",':',';',',','<','.','>','?','/','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        for i in self.v_letter:
            self.dic_pwd.update({i : 0})
        for i in self.v_letter:
            self.dic_usn.update({i : 0})
        for line in self.f1:
            line = line.split()
            self.dic_pwd[line[0]] = int(line[1])
        for line in self.f2:
            line = line.split()
            self.dic_usn[line[0]] = int(line[1])
        #print self.dic_pwd
        #print self.dic_usn
        
    def score_freq_pwd(self):
        rank = [] ### decreasing order of password letter distribution; index is corresponding to score
        swap = 1
        for key in self.dic_pwd:
            rank.append([key, self.dic_pwd[key]])
        while swap == 1:
            swap = 0
            for i in range(0, len(rank)-1):
                if rank[i][1] < rank[i+1][1]:
                    tmp = rank[i+1]
                    rank[i+1] = rank[i]
                    rank[i] = tmp
                    swap = 1
        score_pwd = 0
        #print rank
        sum1 = sum([i[1] for i in rank])
        #print sum1
        sum2 = 0
        for i in rank:
            sum2 = sum2 + i[1]
            if sum2 >= 0 and sum2 < sum1/10.0:
                i.append(1)
            if sum2 >= sum1/10.0 and sum2 < sum1*2/10.0:
                i.append(2)
            if sum2 >= sum1*2/10.0 and sum2 < sum1*3/10.0:
                i.append(3)
            if sum2 >= sum1*3/10.0 and sum2 < sum1*4/10.0:
                i.append(4)
            if sum2 >= sum1*4/10.0 and sum2 < sum1*5/10.0:
                i.append(5)
            if sum2 >= sum1*5/10.0 and sum2 < sum1*6/10.0:
                i.append(6)
            if sum2 >= sum1*6/10.0 and sum2 < sum1*7/10.0:
                i.append(7)
            if sum2 >= sum1*7/10.0 and sum2 < sum1*8/10.0:
                i.append(8)
            if sum2 >= sum1*8/10.0 and sum2 < sum1*9/10.0:
                i.append(9)
            if sum2 >= sum1*9/10.0 and sum2 <= sum1*10/10.0:
                i.append(10)
        for c in self.password:
            for i in range(0, len(rank)):
                if c == rank[i][0]:
                    score_pwd = score_pwd + rank[i][2]
        return int(math.ceil((score_pwd/float(10*len(self.password)))*10))
        
    def score_freq_usn(self):
        rank = [] ### decreasing order of password letter distribution; index is corresponding to score
        swap = 1
        for key in self.dic_usn:
            rank.append([key, self.dic_usn[key]])
        while swap == 1:
            swap = 0
            for i in range(0, len(rank)-1):
                if rank[i][1] < rank[i+1][1]:
                    tmp = rank[i+1]
                    rank[i+1] = rank[i]
                    rank[i] = tmp
                    swap = 1
        score_usn = 0
        #print rank
        sum1 = sum([i[1] for i in rank])
        #print sum1
        sum2 = 0
        for i in rank:
            sum2 = sum2 + i[1]
            if sum2 >= 0 and sum2 < sum1/10.0:
                i.append(1)
            if sum2 >= sum1/10.0 and sum2 < sum1*2/10.0:
                i.append(2)
            if sum2 >= sum1*2/10.0 and sum2 < sum1*3/10.0:
                i.append(3)
            if sum2 >= sum1*3/10.0 and sum2 < sum1*4/10.0:
                i.append(4)
            if sum2 >= sum1*4/10.0 and sum2 < sum1*5/10.0:
                i.append(5)
            if sum2 >= sum1*5/10.0 and sum2 < sum1*6/10.0:
                i.append(6)
            if sum2 >= sum1*6/10.0 and sum2 < sum1*7/10.0:
                i.append(7)
            if sum2 >= sum1*7/10.0 and sum2 < sum1*8/10.0:
                i.append(8)
            if sum2 >= sum1*8/10.0 and sum2 < sum1*9/10.0:
                i.append(9)
            if sum2 >= sum1*9/10.0 and sum2 <= sum1*10/10.0:
                i.append(10)
        print rank
        for c in self.username:
            for i in range(0, len(rank)):
                if c == rank[i][0]:
                    score_usn = score_usn + rank[i][2]
        return int(math.ceil((score_usn/float(10*len(self.username)))*10))
        

def main():
    s = score_freq_distr('@##$##$%','00111Z0A')
    f = s.score_freq_pwd()
    print f
    f = s.score_freq_usn()
    print f
if __name__ == "__main__":
    main()
