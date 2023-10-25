#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author    :刘清华
# @time      :2022/10/25 20:05
# @function  :
# @version   :v1
# @desc      :
import datetime
import time
from typing import Text

def count_milliseconds():
    """
    计算时间
    :return:
    """
    access_start = datetime.now()
    access_end = datetime.now()
    access_delta = (access_end - access_start).seconds * 1000
    return access_delta


def timestamp_conversion(time_str: Text) -> int:
    """
    时间戳转换，将日期格式转换成时间戳
    :param time_str: 时间
    :return:
    """

    try:
        datetime_format = datetime.strptime(str(time_str), "%Y-%m-%d %H:%M:%S")
        timestamp = int(
            time.mktime(datetime_format.timetuple()) * 1000.0
            + datetime_format.microsecond / 1000.0
        )
        return timestamp
    except ValueError as exc:
        raise ValueError('日期格式错误, 需要传入得格式为 "%Y-%m-%d %H:%M:%S" ') from exc


def time_conversion(time_num: int):
    """
    时间戳转换成日期
    :param time_num:
    :return:
    """
    if isinstance(time_num, int):
        time_stamp = float(time_num / 1000)
        time_array = time.localtime(time_stamp)
        other_style_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        return other_style_time


def now_time():
    """
    获取当前时间, 日期格式: 2021-12-11 12:39:25
    :return:
    """
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


def now_time_day():
    """
    获取当前时间, 日期格式: 2021-12-11
    :return:
    """
    localtime = time.strftime("%Y-%m-%d", time.localtime())
    return localtime


def get_time_for_min(minute: int) -> int:
    """
    获取几分钟后的时间戳
    @param minute: 分钟
    @return: N分钟后的时间戳
    """
    return int(time.time() + 60 * minute) * 1000


def get_now_time() -> int:
    """
    获取当前时间戳, 整形
    @return: 当前时间戳
    """
    return int(time.time()) * 1000


def getFutureTime_by_offset(offSet=1):
    """
    根据现在时间和设定偏移量获取标准时间
    :param offSet:偏移类型，1为加法，其他为减法
    :param year:年
    :param month:月
    :param day:日
    :param hour:小时
    :param minute:分钟
    :param second:秒
    :return:如1970-01-01 00:00:00
    """

    FutureTime = (datetime.datetime.now() + datetime.timedelta(days=offSet)).strftime("%Y-%m-%d")
    FutureTime += ' 18:00'
    return FutureTime


def getFutureTime_by_Time(offSet=1):
    """
    根据现在时间和设定偏移量获取标准时间
    :param offSet:偏移类型，1为加法，其他为减法
    :param year:年
    :param month:月
    :param day:日
    :param hour:小时
    :param minute:分钟
    :param second:秒
    :return:如1970-01-01 00:00:00
    """

    FutureTime = (datetime.datetime.now() + datetime.timedelta(days=offSet)).strftime("%Y-%m-%d")
    return FutureTime


if __name__ == '__main__':
    a = getFutureTime_by_offset(1)

    print(a)
