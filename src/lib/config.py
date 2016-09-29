import logging


NMAP_CMD = ['-sS', '-Pn', '-sV', '-oX', '-']
ZMAP_CMD = ['-q', '-v', '0'] # silent
PORTS = [80,
         22,
         443]

# only when cpint's level >= this, will print
CONSOLE_PRINT = logging.INFO

LOG_FILE = 'data/log/test.log'