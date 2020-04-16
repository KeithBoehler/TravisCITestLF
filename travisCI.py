#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:56:04 2020

@author: keithnator3000

Some code to test an implementation for Travis CI.

Converting LoFASM Py2 code to Py3
"""

def simpleAdd(num):
    return num + 5

def doNothing():
    pass

print("Hello world!")

x = simpleAdd(4)

print("Simple add has returned " + str(x))