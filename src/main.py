'''
    @author: Bolun Huang
    @copyright: hbl080212 AT neo DOT tamu DOT com
    @description: main UI entry for password username strength estimation software
'''
import score_tfidf_sim ## tfidf
import score_upper_case ## upper case check
import score_special_char ## spcial char check
import score_freq_distr ## frequency distribution
import score_len ## password len check
import score_pw_seq ## password sequential check
import score_comp_usn_pwd ## compare the similarity of usn and pwd
import score_editdist ## edit distance
import score_repeative_pattern ### password pattern
import math

def help():
    print '***********menu***********'
    print 'commands:'
    print "'help' -- show the user menu"
    print "'go' -- start {username, password} estimation"
    print "'report' -- print the estimation report of last trial"
    print "'exit' -- exit the program"

def main():
    '''
        we first have to initialize the program: the character vector, and the document frequency dictionary
        v_letter is the vector of all possible characters on keyboard; there are 94 characters including special characters
    ''''''
    v_letter = ['~','`','!','@','#','$','%','^','&','*','(',')','_','+','-','=','|','\\','}',']','{','[','"',"'",':',';',',','<','.','>','?','/','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    f = open('../data/2a18.txt', "r")
    print len(v_letter)
    dic_1 = {}
    count_doc = 0.0
    for i in v_letter:
        dic_1.update({i : 0})
    for line in f:
        line = line.split()
        for i in v_letter:
            if i in line[1]:
                dic_1[i] = dic_1[i] + 1
            if i in line[2]:
                dic_1[i] = dic_1[i] + 1
        count_doc = count_doc + 2
    #for key in dic_1:
    #    dic_1[key] = math.log(count_doc/(1+dic_1[key]))
    f.close()
    '''
    print 'Initialization starting...'
    dic_1 = {}
    f = open('../data/document_frequency.txt','r')
    for line in f:
        line = line.split()
        dic_1.update({line[0]: int(line[1])})
    f.close()
    count = sum(dic_1.values())
    #print count
    for key in dic_1:
        dic_1[key] = math.log(count/(1+dic_1[key]))
    print 'Initialization finished...'
    print '***********menu***********'
    print 'commands:'
    print "'help' -- user menu"
    print "'go' -- start application"
    print "'report' -- print the estimation report of last trial"
    print "'exit' -- exit "
    ## main loop ##
    while 1:
        command = raw_input(">")
        if command == 'help':
            help()
        elif command == 'go':
            
            while 1:
                usn = raw_input("USERNAME: ")
                pwd = raw_input("PASSWORD: ")
                #print 'password: %s username: %s' %(pwd, usn)
                i1 = score_tfidf_sim.score_tfidf_sim(usn, pwd, dic_1)
                i2 = score_freq_distr.score_freq_distr(usn, pwd)
                i3 = score_len.score_len(usn, pwd)
                i4 = score_upper_case.score_upper_case(pwd)
                i5 = score_special_char.score_special_char(pwd)
                i6 = score_pw_seq.score_pw_seq(usn, pwd)
                i7 = score_comp_usn_pwd.score_comp_usn_pwd(usn, pwd)
                i8 = score_editdist.score_editdist(usn, pwd)
                i9 = score_repeative_pattern.score_repeative_pattern(pwd)
                score_1 = i1.cal_tfidf() ## tfidf similarity score
                score_2 = i2.score_freq_pwd() ## frequency distribution score
                score_3 = i3.score_pwd() ## password length score
                score_4 = i4.check() ## upper case check
                score_5 = i5.check() ## special character check
                score_6 = i6.alphabet_seq() ## alphabetical sequence score
                score_7 = i6.keyboard_seq() ## keyboard sequence score
                score_8 = i6.is_Bday() ## check birthday
                score_9 = i7.ratePassword() ## percentage of usn in password
                score_10 = i8.ratePassword() ## edit distance score
                score_11 = i9.ratePassword() ## repeative pattern score
                print score_1, score_2, score_3, score_4, score_5, score_6, score_7, score_8, score_9, score_10, score_11
                score_fin = 0
                #### password length scale ####
                if score_3 <= 3:
                    alpha = 0.2
                    #score_fin = int((alpha*score_1 + score_2 + score_3 + alpha*score_4 + alpha*score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                    #print 'password strength: ', score_fin
                elif score_3 <= 5:
                    alpha = 0.4
                    #score_fin = int((alpha*score_1 + score_2 + score_3 + alpha*score_4 + alpha*score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                    #print 'password strength: ', score_fin
                elif score_3 <= 8:
                    alpha = 0.6
                    #score_fin = int((alpha*score_1 + score_2 + score_3 + alpha*score_4 + alpha*score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                    #print 'password strength: ', score_fin
                else:
                    alpha = 1.0
                
                if score_11 == 1: ### password repeative pattern scale
                    alpha = 0.3
                    score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + score_4 + score_5 + alpha*score_6 + score_7 + alpha*score_9 + alpha*score_10 + score_11)/10)
                    print 'password strength: ', score_fin
                elif score_1 <=2 or score_10 <= 2:
                    alpha = 0.3
                    score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + score_4 + score_5 + alpha*score_6 + score_7 + alpha*score_9 + alpha*score_10 + score_11)/10)
                    print 'password strength: ', score_fin
                else:
                    if score_3 >= 6 and (score_4 == 1 or score_5 == 1): ## no uppercase or no special char
                        if score_4 == 1 and score_5 == 1:
                            alpha = alpha*0.7
                            score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + alpha*score_4 + alpha*score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                            print 'password strength: ', score_fin
                        elif score_4 == 1:
                            alpha = alpha*0.8
                            score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + alpha*score_4 + alpha*score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                            print 'password strength: ', score_fin
                        elif score_5 == 1:
                            alpha = alpha*0.8
                            score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + alpha*score_4 + alpha*score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                            print 'password strength: ', score_fin
                    elif score_3 >= 6 and (score_6 <= 4 or score_7 <= 4): ## keyboard/alphabetical sequence scale
                        if score_6 <= 4 and score_7 <= 4:
                            alpha = alpha*0.6
                            score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + score_4 + score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                            print 'password strength: ', score_fin
                        elif score_6 <= 4:
                            alpha = alpha*0.7
                            score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + score_4 + score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                            print 'password strength: ', score_fin
                        elif score_7 <= 4:
                            alpha = alpha*0.7
                            score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + score_4 + score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                            print 'password strength: ', score_fin
                    else:
                        score_fin = int((alpha*score_1 + score_2 + alpha*score_3 + score_4 + score_5 + alpha*score_6 + alpha*score_7 + alpha*score_9 + alpha*score_10 + alpha*score_11)/10)
                        print 'password strength: ', score_fin
                f = open('../data/report.txt', 'w')
                f.write("password length    score: %d\n" %(score_3))
                f.write("similarity-tfidf   score: %d\n" %(score_1))
                f.write("edit-distance      score: %d\n" %(score_10))
                f.write("uname-in-passwd    score: %d\n" %(score_9))
                f.write("upper-case letter  score: %d\n" %(score_4))
                f.write("special character  score: %d\n" %(score_5))
                f.write("distribution       score: %d\n" %(score_2))
                f.write("keyboard sequence  score: %d\n" %(score_7))
                f.write("alphabet sequence  score: %d\n" %(score_6))
                f.write("repeative pattern  score: %d\n" %(score_11))
                f.write("-----------------------------\n")
                f.write("overall            score: %d\n" %(score_fin))
                f.write('**********comments**********\n')
                if score_1 <= 5 or score_9 <= 5 or score_10 <= 5:
                    f.write("@password and username is too similar\n")
                if score_2 <= 5:
                    f.write("@your combinations of password is commonly used\n")
                if score_3 <= 6:
                    f.write("@password length is too short\n")
                if score_4 == 1:
                    f.write("@password contains NO uppercase letters\n")
                if score_5 == 1:
                    f.write("@password contains NO special characters\n")
                if score_6 != 10:
                    f.write("@alphabetical sequence input is detected in password\n")
                if score_7 != 10:
                    f.write("@keyboard sequence input is detected in password\n")
                if score_8 != 10:
                    f.write("@suspected birthday in password\n")
                if score_11 != 10:
                    f.write("@repeative pattern is detected in password\n")
                f.close()
                break
                    
        elif command == 'report':
            f = open("../data/report.txt","r")
            print '***********report***********'
            for line in f:
                print line,
            f.close()
        elif command == 'exit':
            print 'bye'
            break
        else:
            print 'bad command'

if __name__ == '__main__':
    main()