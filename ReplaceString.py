# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:47:01 2020

@author: Administrator
"""
import os
import sys

class ReplaceString:
    def __init__(self):
        self.oldString = None
        self.newString = None
        self.filePath  = None
    
    def replaceAction(self):
        pass
    
    def setOldString(self,string):
        self.oldString = string
        
    def setNewString(self,string):
        self.newString = string
        
    def setFilePath(self,path):
        self.filePath = path