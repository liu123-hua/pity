#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author    :刘清华
# @time      :2022/10/21 16:43
# @function  :
# @version   :v1
# @desc      :
import os



def replace_path(path):
    """替换路径"""
    path = path.replace('$', os.sep)
    return path


def generate_path(name: str):
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(root_path, name.replace('$', os.sep))


class ConfigHandler:
    # 用例路径
    case_path = generate_path("test_case$")
    # 测试用例数据路径
    data_path = generate_path('data$')

    class_info_path = generate_path('class_info_file$')
    cache_path = generate_path('Cache$')

    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
    common_path = generate_path('commonYAML$')
    config_path = generate_path('common$config.yaml')




if __name__ == '__main__':
    print(ConfigHandler.cache_path)
