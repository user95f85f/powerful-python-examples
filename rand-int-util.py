#!/usr/bin/python3

import random
import sys

if len(sys.argv) != 3:
   exit(1)

try:
   print(str(random.randint(int(sys.argv[1]), int(sys.argv[2]))))
except:
   exit(2)


#~$ python3 randint.py 1 2
#2
#~$ python3 randint.py 1 2
#1
#~$ python3 randint.py 1 2
#2
#~$ python3 randint.py 1 2
#2
#~$ python3 randint.py 1 6
#5
#~$ python3 randint.py 1 6
#1
#~$ python3 randint.py 1 6
#2
#~$ python3 randint.py 1 6
#3
#~$ python3 randint.py 1 6
#2
#~$ python3 randint.py 1 6
#1
