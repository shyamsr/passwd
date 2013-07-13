'''
    @author: Bolun Huang
    @date: 04/2013
'''

class score_special_char():
    def __init__(self, str_in):
        self.s = str_in
    def check(self):
        score = 1
        for i in self.s:
            if (ord(i) >= 33 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 126):
                score = 10
                break
        return score
    
'''
def main():
    s = score_special_char('cheDan001')
    score = s.check()
    print score    

if __name__ == '__main__':
    main()
'''