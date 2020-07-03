#!/usr/bin/python3

import os #for rename of file and removal of file functionality

print("give me input to put into a.txt\n");
with open('a.txt', 'w') as myf:
   while True:
      szInput = input('--> ')
      if szInput == '':
         break
      print(szInput, file=myf, end='')

print(str(myf.closed))  #True
print("put contents into a.txt\n")
input('--> ')

os.rename('a.txt', 'b.txt')
print("moved a.txt to b.txt\n")
input('--> ')

os.remove('b.txt')
print("removed b.txt\n")
input('--> ')
print("exiting..\n")
