# -*- coding:utf-8 -*-
# import os
#
# case_path = os.path.abspath('./TestCase/Scripts/Anydoor.py')
# report_path = os.path.abspath('./output/html/report.html')
#
# # 命令拼接,注意每一个参数之间加空格
# cmd1 = 'py.test ' + case_path + ' --html=' + report_path + ' --rerun 1' + ' --self-contained-html'
# os.system(cmd1)

# from multiprocessing import Pool
# import os, time
#
#
# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(3)
#     end = time.time()
#     print 'Task %s runs %0.2f seconds.' % (name, (end - start))
#
# if __name__=='__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool()
#     for i in range(4):
#         p.apply_async(long_time_task, args=(i,))
#     print 'Waiting for all subprocesses done...'
#     p.close()
#     p.join()
#     print 'All subprocesses done.'


import threading,os
from time import ctime,sleep
from multiprocessing import Pool


def music(func,name):
    for i in range(1):
        
        print " %s : I was listening to %s. %s and pid is %s" %(name,func,ctime(),os.getpid())
        sleep(2)

# def move(func):
#     for i in range(1):
#         print "I was at the %s! %s" %(func,ctime())
#         sleep(5)

threads = []
for i in range(2):
    t1 = threading.Thread(target=music,args=(u'爱情买卖',))
    threads.append(t1)
# t2 = threading.Thread(target=move,args=(u'阿凡达',))
# threads.append(t2)



if __name__ == '__main__':
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join()
    pool = Pool(processes=2)
    for i in range(2):
        pool.apply_async(music, (u'爱情买卖', i))
    pool.close()
    pool.join()
    
    print "all over %s" % ctime()
    import datetime
    print datetime.datetime.now()
