# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 19:49:12 2016

@author: Administrator
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.cross_validation import cross_val_score

class SKL_RandomForests(object):
    
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
    
    def randomForestsClassifying(self, datMat, classlabels):
        rfc = RandomForestClassifier(n_estimators=self.n_estimators, max_depth=None,
                                     min_samples_split=1, random_state=0)
        rfc.fit(datMat, classlabels)
        return rfc
    
    def extraForestsClassifying(self, datMat, classlabels):
        efc = ExtraTreesClassifier(n_estimators=self.n_estimators, max_depth=None, 
                                   min_samples_split=1, random_state=0)
        efc.fit(datMat, classlabels)
        return efc

if __name__ == "__main__":
    sklrf = SKL_RandomForests(500)
    datArr, labelArr = sklrf.loadDataSet('horseColicTraining2.txt')
    rfclassifier = sklrf.randomForestsClassifying(datArr,labelArr)
    efclassifier = sklrf.extraForestsClassifying(datArr,labelArr)
    
    testArr, testLabelArr = sklrf.loadDataSet('horseColicTest2.txt')
    rfscore = rfclassifier.score(testArr, testLabelArr)
    efscore = efclassifier.score(testArr, testLabelArr)
    print rfscore, efscore
    
    
    
    
    