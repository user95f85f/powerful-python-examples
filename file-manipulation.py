#!/usr/bin/python3

import os

myf = open('1.txt', 'w')
print("wudup\n", file=myf)
myf.close()
print("created 1.txt")
input('--> ')

os.rename('1.txt', '2.txt')   #REM 2.txt gets replaced even if 2.txt exists
print("moved 1.txt to 2.txt\n")
input('--> ')

os.remove('2.txt')
print("removed 2.txt\n")
print("exiting..\n")
