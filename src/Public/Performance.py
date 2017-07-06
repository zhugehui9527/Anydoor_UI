# -*- coding:utf-8 -*-
#######################################################
#filename:Performance.py
#author:Jeff
#date:2017-07-03
#function:根据cpu、内存绘制曲线图
#######################################################

from src.Public.Global import L
def data_marker(cpu, mem, h_cpu, h_mem, path):
    """

    :param cpu: cpu列表
    :param mem: 内存列表
    :param path: 存储的文件路径
    :return:
    """
    import matplotlib

    matplotlib.use('Agg')
    import pylab as pl
    pl.plot(cpu, 'r')
    pl.plot(mem, 'g')

    pl.title('performance')
    pl.xlabel('second')
    pl.ylabel('percent')

    pl.plot(cpu, color="red", linewidth=2.5, linestyle="-", label="this_cpu")
    pl.plot(mem, color="blue", linewidth=2.5, linestyle="-", label="this_mem")
    if h_mem is not None:
        pl.plot(
            h_cpu,
            color="magenta",
            linewidth=2.5,
            linestyle="-",
            label="historical_cpu")
        pl.plot(
            h_mem,
            color="green",
            linewidth=2.5,
            linestyle="-",
            label="historical_mem")
    pl.legend(loc='upper left')
    pl.xlim(0.0, len(mem))
    pl.ylim(0.0, 100.0)
    pl.savefig(path)
    L.logger.debug('Report:%s' % path)
    # pl.show() #调出GUI实时查看
    pl.close()  # 必须关闭,不然值会在内存中不销毁
