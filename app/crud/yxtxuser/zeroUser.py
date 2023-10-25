import json
import time

import requests

from app.utils.logger import Log
from app.utils.yxtxLogin import LoginUser
from app.enums.ProjectMsEnum import ProjectMsEnum
from app.enums.ProjectChannelEnum import ProjectChannelEnum
from app.crud.yxtxuser.divideClassFlag import divideClassFlagService


class divideUserService():
    log = Log("divideUserService")

    @classmethod
    def getMsHeader(cls, revenue_project_id):
        token = LoginUser()
        msHeader = {
            'authorization': token,
            'tenant_id': ProjectMsEnum[revenue_project_id].value,
            'revenue_project_id': ProjectMsEnum[revenue_project_id].value
        }
        return msHeader

    @classmethod
    def zeroDivideUser(cls, divideUser):
        resultDict = []
        if divideUser.assignClassInfoId:
            print("指定分班")

            for userId in divideUser.usersId:
                print(userId)
                flag = cls.createMsOrderuser(divideUser, userId, resultDict)
                if not flag:
                    continue

        else:
            print("正常分班")
            resultDict = []
            userTokenDict = divideUserService.getUserToken(divideUser.usersId, divideUser.revenueProjectId)
            for key, value in userTokenDict.items():
                cls.createOrderUser(key, value, divideUser.revenueProjectId, divideUser.goodsId, resultDict,
                                    divideUser.divideType)
                time.sleep(3)
        return resultDict

    @classmethod
    def zeroDivideJjUser(cls, divideUser):
        userTokenDict = divideUserService.getUserToken(divideUser.usersId, divideUser.revenueProjectId)
        for key, value in userTokenDict.items():
            cls.createOrderJjUser(key, value, divideUser.revenueProjectId, divideUser.goodsId, resultDict)
            time.sleep(3)

    # 获取用户token
    @classmethod
    def getUserToken(cls, user_data: [], revenue_project_id: str):
        dict = {}
        for user in user_data:
            url = 'https://api-ms-test.yixueniuniu.com/member/getToken/{}'.format(user)
            method = 'GET'
            header = divideUserService.getMsHeader(revenue_project_id)
            resp = requests.request(method=method, url=url, headers=header)
            if resp.json()['code'] == 'OK':
                print(str(user) + "获取成功")
                userTokenData = str(resp.json()['data'])
                dict[user] = userTokenData
        print(dict)
        return dict

    @classmethod
    def createOrderUser(cls, userId: str, userToken: str, revenue_project_id: str, goodsId: str, resultDict: [],
                        divideType: str):
        url = 'https://api-test.yixueniuniu.com/uc/pay/create-order'
        method = 'POST'
        header = {"Content-Type": "application/json",
                  "X-USER-TOKEN": userToken,
                  "PROJECT": revenue_project_id
                  }
        reqData = {
            "source": 1,
            "app_id": "system",
            "isZeroGoods": True,
            "pay_type": 5,
            "pay_style": 5,
            "tag": "",
            "channel_no": None,
            "goods_id": goodsId
        }
        if divideType == "xb":
            reqData["channel_no"] = ProjectChannelEnum[revenue_project_id].value
        else:
            reqData["channel_no"] = "packageXB_link_default"

        res = requests.request(method=method, url=url, json=reqData, headers=header)
        resultCreateTmp = res.json()
        flag = "data" in dict(res.json()).keys()
        if flag is False:
            resultCreateTmp["userID"] = userId
            resultCreateTmp['desc'] = '购课结果'
            resultDict.append(str(resultCreateTmp))
        else:
            OrderPayResultUrl = "https://api-test.yixueniuniu.com/un/order/queryOrderPayResult"
            reqOrderData = {
                "orderNo": res.json()['data']['order_no']
            }
            resResult = requests.request(method=method, url=OrderPayResultUrl, json=reqOrderData, headers=header)
            resultTmp = resResult.json()
            if resResult.json()['code'] == 'OK':
                resultTmp['userID'] = userId
                resultTmp['desc'] = '购课结果'
                resultDict.append(str(resultTmp))
            else:
                resultTmp['userID'] = userId
                resultTmp['desc'] = '购课结果'
                resultDict.append(str(resultTmp))

        if divideType == "jj":
            print("=========开始进行进阶分班，学员ID为{}======".format(userId))
            divideUrl = 'https://api-ms-test.yixueniuniu.com/coursePermission/divideClassV3/{}/1'.format(userId)
            msHeader = cls.getMsHeader(revenue_project_id)
            divideResp = requests.request(url=divideUrl, headers=msHeader, method=method)
            print(flag)
            print(type(resultCreateTmp))
            tmp = divideResp.json()
            tmp['userID'] = userId
            tmp['desc'] = '分班结果'
            resultDict.append(str(tmp))
            pass

    @classmethod
    def createMsOrderuser(cls, userData: dict, userId: str, resultDict: []):
        courseVersionId = divideClassFlagService.getGoodsIDCourseVersionID(userData.goodsId)
        url = 'https://api-ms-test.yixueniuniu.com/divideClassApply/applyDivideClass'
        method = 'POST'
        msHeader = cls.getMsHeader(userData.revenueProjectId)
        payOrderNo = int(time.mktime(time.localtime(time.time())))
        reqData = {
            "goodsId": userData.goodsId,
            "payMethod": 4,
            "payOrderNo": str(payOrderNo),
            "payAmount": "0",
            "remark": "",
            "targetClassInfoList": [{
                "courseVersionId": courseVersionId,
                "classInfoId": userData.assignClassInfoId
            }],
            "mchId": "system",
            "userId": userId,
            "relationUserId": ""
        }
        print(reqData)
        resResult = requests.request(method=method, url=url, json=reqData, headers=msHeader)
        resultTmp = resResult.json()
        if resultTmp['code'] == 'OK':
            print(str(userId) + "小白开课成功")
            resultTmp['userID'] = userId
            resultDict.append(str(resultTmp))
            return True
        else:
            print(str(userId) + "小白开课失败" + str(res.json()))
            resultTmp['userID'] = userId
            resultDict.append(str(resultTmp))
            return False


if __name__ == '__main__':
    divideUserService.getMsHeader(1)
