#!/usr/bin/python3

import os
szText = """dear {name},
I think {verb1}
therefore {verb2}
yada yada yada sofoh eekwahna dooshor
adi, {mr}
-{author}"""

print(szText.format(name=os.getlogin(), verb1='you are awesome', verb2='everything is grand', mr='senior', author='yours truly, Ayebei'))
#dear debian-user,
#I think you are awesome
#therefore everything is grand
#yada yada yada sofoh eekwahna dooshor
#adi, senior
#-yours truly, Ayebei
