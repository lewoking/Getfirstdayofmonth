# -*- encoding: utf-8 -*-
'''
@File    :   firstworkday.py
@Time    :   2019/05/07 20:03:53
@Author  :   guozi
@Version :   1.0
@WebSite    :  github.com/lewoking
'''

import requests
import datetime
import time
import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='output.log',
    datefmt='%Y/%m/%d %H:%M:%S',
    format='%(asctime)s - %(name)s - %(levelname)s - '
           '%(lineno)d - %(module)s - %(message)s'
)
logger = logging.getLogger(__name__)


def api(day):
    server_url = "http://api.goseek.cn/Tools/holiday?date="
    logger.info('today is ' + day)
#    holiday = [1, 3]
    workday = [0, 2]  # 正常工作日对应结果为 0, 法定节假日对应结果为 1, 节假日调休补班对应的结果为 2，休息日对应结果为 3
    try:
        response = requests.get(server_url + day)
    except UnicodeDecodeError:
        print('please check network!')

    else:
        timedata = json.loads(response.text)
        daytype = int(timedata["data"])
        worktype = daytype in workday
    return worktype


def dateRange(bgn, end):  # 测试用 日期列表
    fmt = '%Y%m%d'
    bgn = int(time.mktime(time.strptime(bgn, fmt)))
    end = int(time.mktime(time.strptime(end, fmt)))
    return [time.strftime(fmt, time.localtime(i))
            for i in range(bgn, end+1, 3600*24)]


if __name__ == '__main__':
    mydate = datetime.datetime.now()
    day = mydate.strftime("%Y%m%d")
    for day in dateRange('20190101', '20191230'):  # 正常运行时注释此行并调整下文对齐
        dayofmonth = day[-2:]
        if dayofmonth == '01':
            warned = False
        if (not warned):
            worktype = api(day)
            if worktype and (not warned):
                print('warning ! !' + day)  # 第一次运行或月第一个工作日
                warned = True
