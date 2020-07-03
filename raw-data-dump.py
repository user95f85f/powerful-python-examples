#!/usr/bin/python3

def mydump(_a):
   arOut = []
   len_a = len(_a)
   i = 0
   while i < len_a:
      arOut.append('{:06d}  '.format(i))
      for j in range(16):
         if (i + j) < len_a:
            myByte = _a[i + j];
            arOut.append('{:02X} '.format(myByte))
      i += 16
   return ''.join(arOut)

print(mydump(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a'));
#000000  00 01 02 03 04 05 06 07 08 09 0A
