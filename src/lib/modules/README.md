every module should be wirte as below

~~~

from Detect import Detect

class xxxDetect(Detect):

    def __init__(self, ip, port, timeout):
        # init at here
        super(xxxDetect, self).__init__(ip, port)
~~~