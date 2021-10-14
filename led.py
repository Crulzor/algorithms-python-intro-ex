# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 10:10:04 2021

@author: bartc
"""

class Led:
    def __init__(self, pin): #self is een beetje zoals this. Het is een verwijzing naar hetzelfde object
        self.__isOn = False
        self.__pin = pin      #dit zijn attributen. Dus eerst self.__HIERDENAAM
    
            
    def on(self):
        self.__isOn = True
        return self.__isOn


    def off(self):
        self.__isOn = False
        return self.__isOn

    def toggle(self):
        self.__isOn = not self.__isOn
        return self.__isOn

    def getState(self):
        return self.__isOn

led = Led(1)
print(led.getState())
print(led.on())
print(led.toggle())
otherLed = Led(2)
