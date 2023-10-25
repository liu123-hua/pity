# !/usr/bin/python
# -*- coding:utf-8 -*-
# @author    :刘清华
# @time      :2023/09/11 14:56
# @function  :
# @version   :v1
# @desc      :
import json
from typing import Any

import pymysql

from app.handler.fatcory import PityResponse
from app.utils.time_control import now_time


class DBClient:

    def getCourseDBClient(self):
        courseDB = pymysql.connect(host='bj-test-yxtx-01-public.mysql.polardb.rds.aliyuncs.com',
                                   user='yxtx_test',
                                   password='wld42Rbxr7xcEyBT',
                                   database='yxtx_course_test',
                                   charset='utf8')
        return courseDB

    def getShopDBClient(self):
        shopDB = pymysql.connect(host='bj-test-yxtx-01-public.mysql.polardb.rds.aliyuncs.com',
                                 user='yxtx_test',
                                 password='wld42Rbxr7xcEyBT',
                                 database='yxtx_shop_test',
                                 charset='utf8')
        return shopDB


if __name__ == '__main__':

    courseDB = DBClient().getCourseDBClient()

    cursorCourseDB = courseDB.cursor()
    nowTime = now_time()
    sql = """ SELECT  t. * FROM yxtx_course_test.advanced_receive_batch t WHERE 
    goods_id = %s  and pause_flag = 0 and full_flag =0 and %s BETWEEN receive_start_time  and receive_end_time"""
    print(sql)
    cursorCourseDB.execute(sql, [1148,nowTime])

    courseDB.commit()
    # 获取所有记录列表
    courseResults = cursorCourseDB.fetchall()
    print(courseResults)







