from lib.scan.log import cprint
# from lib.modules.ftp import ftp_detect
# import lib.modules.http as ht
# print dir(ht)
from lib.modules.http import httpDetect
# from lib.schema.mongo import Mongo
# from lib.db import *

h = httpDetect("180.97.33.107")
h.pprint()
h = httpDetect("104.116.10.49")
h.pprint()


# m = Mongo()



# x = get('i')

# print x
'''
tmp = []

for i in x:
    print i
    t = ftpDetect(i)
    print t
    tmp.append(t)

save(tmp, 'i')
'''

# 
# cprint("test","info")
# cprint("test","debug")
# cprint("test","warning")
# cprint("test","error")
# cprint("test","critical")

#help(log)

'''
x = [1,23,5,4]

save(x,'x')

x=[11]

print get('x')
'''

