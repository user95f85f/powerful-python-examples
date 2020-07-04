#!/usr/bin/python3

import os
szText = """dear {name},
I think {verb1}
therefore {verb2}
we are stuck in {place}
adi, {mr}
-{author}"""

print(szText.format(name=os.getlogin(), verb1='you are awesome', verb2='everything is grand', place=os.getcwd(), mr='senior', author='yours truly, Ayebei'))
#dear debian-user,
#I think you are awesome
#therefore everything is grand
#we are stuck in /home/debian-user/power-python
#adi, senior
#-yours truly, Ayebei
