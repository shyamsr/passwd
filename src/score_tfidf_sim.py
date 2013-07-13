'''
    @author: Bolun Huang
    @date: 04/2013
'''
import math

class score_tfidf_sim():
    def __init__(self, username, password, dic_origin):
        self.usn = username
        self.pwd = password
        self.dic_1 = dic_origin
        
    def cal_tfidf(self):
        #print 'idf: ', self.dic_1
        dic_2 = {} ## local term frequency of username
        dic_3 = {} ## local term frequency of password
        for key in self.dic_1:
            dic_2.update({key : 0})
            dic_3.update({key : 0})
        ### term freq of username
        for i in self.usn:
            dic_2[i] = dic_2[i] + 1
        for key in dic_2:
            dic_2[key] = dic_2[key]/float(len(self.usn))
        ### term freq of password
        for i in self.pwd:
            if i in self.pwd:
                dic_3[i] = dic_3[i] + 1
        for key in dic_3:
            dic_3[key] = dic_3[key]/float(len(self.pwd))
        for key in self.dic_1:
            dic_2[key] = self.dic_1[key]*dic_2[key] ### tfidf of username
        for key in self.dic_1:
            dic_3[key] = self.dic_1[key]*dic_3[key] ### tfidf of password
        #print dic_2
        #print dic_3
        #print self.usn, self.pwd,
        cosine_sim = self.cal_cosine_sim(dic_2, dic_3)
        #print cosine_sim
        return self.score(cosine_sim)
        
    def cal_cosine_sim(self, vector1,vector2):
        # Calculate numerator of cosine similarity
        if len(vector1) == len(vector2):
            dot = 0.0
            for key in vector1:
                dot = dot + vector1[key]*vector2[key]
            #print dot
            # Normalize the first vector
            sum_vector1 = 0.0
            for key in vector1:
                sum_vector1 = sum_vector1 + vector1[key]*vector1[key]
            norm_vector1 = math.sqrt(sum_vector1)
            # Normalize the second vector
            sum_vector2 = 0.0
            for key in vector2:
                sum_vector2 = sum_vector2 + vector2[key]*vector2[key]
            norm_vector2 = math.sqrt(sum_vector2)
            if not norm_vector1 == 0 and not norm_vector2 == 0:
                return dot/float(norm_vector1*norm_vector2)
            else:
                return 1
            
    def score(self, val):
        index = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        for i in range(0, len(index)):
            if i < len(index) - 1:
                if val >= index[i] and val < index[i+1]:
                    return int((1.0-index[i])*10)
                    break
            else:
                if val >= index[i]:
                    return int((1.0-index[i])*10)
                    break
