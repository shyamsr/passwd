'''
    @author: Bolun Huang
    @date: 04/2013
'''
class score_upper_case():
    def __init__(self, str_in):
        self.s = str_in
    def check(self):
        score = 1
        for i in self.s:
            if ord(i) >= 65 and ord(i) <= 90:
                score = 10
                break
        return score

'''
def main():
    s = score_upper_case('chenDan001')
    score = s.check()
    print score    

if __name__ == '__main__':
    main()
'''