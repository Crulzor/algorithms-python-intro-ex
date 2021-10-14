# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:12:39 2021

@author: bartc
"""

def divisable(amount):
    sum = 0
    for i in range(1 , amount):
        if i % 7 == 0 :
            sum += i
            print(i)
        elif i % 9 == 0:
            print(i)
            sum += i
    return sum
print(divisable(10000))