import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import os


if __name__ == '__main__':
    testdir = './'  # 定义相对路径为当前路径
    discover = unittest.defaultTestLoader.discover(testdir, pattern='*testreport.py')  #查找当前路径下所有满足test_*.py格式的模块内的测试用例
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))  #格式化时间，为后面输出测试报告做准备

    localpath = os.path.abspath("..")
    print('本文件目录位置：' + localpath)
    filepath = os.path.join(localpath, 'test_report', now + '.html')
    print('报告存放路径  ：' + filepath)

    repoertpath = open(filepath, 'wb')  #指定测试报告的存放路径
    runner = HTMLTestRunner(stream=repoertpath,title=u'自动化测试报告',description='testcase_excute !')  #实例化测试报告模块的测试报告对象
    runner.run(discover)
    repoertpath.close()