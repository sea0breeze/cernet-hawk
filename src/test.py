import lib.log as log
from lib.enums import PRINT_LEVEL

#help(log)

'''
x = [1,23,5,4]

save(x,'x')

x=[11]

print get('x')
'''

log.cprint("test", PRINT_LEVEL.ERROR)