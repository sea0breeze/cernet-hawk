import logging
import time


NMAP_CMD = ['-sS', '-Pn', '-sV', '-oX', '-']
ZMAP_CMD = ['-q', '-v', '0'] # silent
PORTS = [80,
         21,
         22,
         443]

# only when cpint's level >= this level, will print
CONSOLE_PRINT = logging.INFO

# log file's path and name
LOG_FILE = 'data/log/'
LOG_FILE += time.strftime('%Y-%m-%d',time.localtime(time.time()))
LOG_FILE += '.log'
