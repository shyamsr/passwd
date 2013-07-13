'''
    @author: Bolun Huang
    @date: 04/2013
'''

import math

class score_len():
    def __init__(self, username, password):
        self.usn = username
        self.pwd = password
        self.index = [2, 4, 6, 8, 10]
    '''
    def score_usn(self):
        score_usn = 0
        len_usn = len(self.usn)
        for i in range(0, len(self.index)):
            if i < len(self.index) - 1:
                if len_usn >= self.index[i] and len_usn < self.index[i+1]:
                    score_usn = self.index[i]
                    break
            else:
                if len_usn >= self.index[i]:
                    score_usn = self.index[i]
                    break
        return score_usn
    '''
    
    def score_pwd(self):
        score_pwd = 0
        len_pwd = len(self.pwd)
        if len_pwd < 2:
            score_pwd = 0
        if len_pwd >= 2 and len_pwd < 4:
            score_pwd = 2
        if len_pwd >= 4 and len_pwd < 6:
            score_pwd = 4
        if len_pwd >= 6 and len_pwd < 8:
            score_pwd = 6
        if len_pwd >= 8 and len_pwd < 10:
            score_pwd = 8
        if len_pwd >= 10:
            score_pwd = 10
        return score_pwd
'''      
def main():
    s = score_len('chenwan001', 'clcdgg28w')
    #score = s.score_usn()
    #print score
    score = s.score_pwd()
    print score
    

if __name__ == '__main__':
    main()
'''