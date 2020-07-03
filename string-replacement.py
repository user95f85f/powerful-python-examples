#!/usr/bin/python3

import re

out = re.sub('a+', 'bbbbbbb', 'aaaaaaaaaccccc');
print(out) #bbbbbbbccccc
