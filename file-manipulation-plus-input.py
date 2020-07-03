#!/usr/bin/python3

import os #for rename of file and removal of file functionality

print('give me input to put into a.txt');
with open('a.txt', 'w') as myf:
   while True:
      szInput = input('--> ')
      if szInput == '':
         break
      print(szInput, file=myf, end='')

print(str(myf.closed))  #True
print('put contents into a.txt')
input('--> ')

os.rename('a.txt', 'b.txt')
print('moved a.txt to b.txt')
input('--> ')

os.remove('b.txt')
print('removed b.txt')
input('--> ')
print('exiting..')
