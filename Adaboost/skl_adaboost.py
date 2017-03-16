# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 20:00:15 2016

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score
class SKL_adaboost(object):
    
    def __init__(self, num):
        self.n_estimators = num
        
    def loadDataSet(self,fileName):      #general function to parse tab -delimited floats
        numFeat = len(open(fileName).readline().split('\t')) #get number of fields 
        dataMat = []; labelMat = []
        fr = open(fileName)
        for line in fr.readlines():
            lineArr =[]
            curLine = line.strip().split('\t')
            for i in range(numFeat-1):
                lineArr.append(float(curLine[i]))
            dataMat.append(lineArr)
            labelMat.append(float(curLine[-1]))
        return dataMat,labelMat
    
    def adaboostClassifying(self, datMat, classlabels):
        bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1),
                                 algorithm="SAMME",
                                 n_estimators=self.n_estimators)
        bdt.fit(datMat, classlabels)
        return bdt
    
if __name__ == "__main__":
    sklada = SKL_adaboost(100)
    datArr, labelArr = sklada.loadDataSet('horseColicTraining2.txt')
    classifier = sklada.adaboostClassifying(datArr,labelArr)
    testArr, testLabelArr = sklada.loadDataSet('horseColicTest2.txt')
    result = classifier.predict(testArr)
    error = result[np.nonzero(testLabelArr!=result)[0]]
    errorate = len(error)*1.0/ len(testArr)
    score = classifier.score(testArr, testLabelArr) # correct rate
    scores = cross_val_score(classifier, testArr, testLabelArr)
    print errorate,1-score
    print score.mean()
    print scores.mean()
