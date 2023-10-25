import base64
import os
from typing import Any

import requests

from app.utils.localPathSetting import ConfigHandler


def decorator(func):
    def wrapper(*args, **kwargs):
        for i in range(5):
            try:
                res = func(*args, **kwargs)
            except AssertionError as e:
                # 判断当用例执行到第三次的时候，抛异常
                print("第%d次尝试重新登录" % i)
                if i == 3:
                    raise e
            else:
                # 执行通过，直接返回函数内容
                return res

    return wrapper


@decorator
def LoginUser() -> Any:
    url = 'https://api-ms-test.yixueniuniu.com/login/loginByAcNo'
    method = "POST"
    reqData = {
        "account": "admin",
        "captchaId": "16424848-b81c-48bc-a03f-a8119d010c",
        "captchaValue": "123",
        "password": "yxnn@20@!888"
    }

    resUserInfo = requests.request(method=method, url=url, json=reqData)
    assert str(resUserInfo.json()['code']) == "OK"

    print("admin登录成功")
    return resUserInfo.json()['data']['token']
