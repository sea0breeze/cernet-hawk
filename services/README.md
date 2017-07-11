every module should be wirte as below

~~~

from common.classes.PortBase import PortBase

class xxxDetect(PortBase):

    def __init__(self, ip, port, timeout):
        super(xxxDetect, self).__init__(ip, port)
        # init and finish scan at here
~~~