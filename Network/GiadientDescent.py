# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 08:54:21 2017

@author: Administrator
"""
import numpy as np

class Network(object):
    
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in
                         zip(sizes[:-1], sizes[1:])]