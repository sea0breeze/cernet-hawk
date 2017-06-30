#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utils.domain import gethostip


class Mode(object):
    """
    使用这个类决定当前处于那个模式下
    分三种环境
    生产环境：上线的环境，谨慎配置
    测试环境：测试的环境，会有较多的输出
    本地环境：用于本地测试的环境，可以在没安装部分
    """

    def __init__(self, mode):
        self.mode = mode
        # print("[*] Init with mode: %s " % mode)

    def isProduct(self):
        # product environment
        return self.mode == "PRODUCT"

    def isTest(self):
        # test environment
        return self.mode == "TEST"

    def isLocal(self):
        # run as local machine
        return self.mode == "LOCAL"

hostip = gethostip()

if hostip in ["", ""]:
    # 用生产环境的IP指定
    mode = Mode("PRODUCT")
else:
    mode = Mode("TEST")

# if False:
if True:
    # 也可以指定模式
    mode = Mode("LOCAL")

if mode.isLocal():
    # warning it!
    print("=== Run As Local ===")

if __name__ == '__main__':
    print(mode.isProduct())
    print(mode.isTest())
    print(mode.isLocal())
