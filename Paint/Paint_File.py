# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 22:49:35 2016

@author: Administrator
"""
import numpy as np 
import matplotlib.pyplot as plt 
class Paint_File(object):
    
    def paintFuction(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        x = np.arange(0,25)
        y1 = np.exp(-0.3*x)
        y2 = np.exp(-0.4*x)
        y3 = np.exp(-0.5*x)
        y4 = np.exp(-0.6*x)
        y5 = np.exp(-0.7*x)
        ax.plot(x,y1, label="a=0.3")
        ax.plot(x,y2, label="a=0.4")
        ax.plot(x,y3, label="a=0.5")
        ax.plot(x,y4, label="a=0.6")
        ax.plot(x,y5, label="a=0.7")
        plt.ylim(0,1.2)
        plt.xlabel("value of x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

if __name__=='__main__':
    pt = Paint_File()
    pt.paintFuction()