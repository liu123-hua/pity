from fastapi import APIRouter

from app.crud.yxtxuser.divideClassFlag import divideClassFlagService
from app.crud.yxtxuser.zeroUser import divideUserService
from app.handler.fatcory import PityResponse
from app.routers.config import router
from app.schema.divideClass import divideUser

router = APIRouter(prefix="/divide")

@router.post("/Users")
async def divide_Class(data: divideUser):
    print(divideUser)
    result = divideUserService.zeroDivideUser(data)
    print(result)

    return PityResponse.success_divideResult_xb(data =result)

@router.post("/jjUsers")
async def divide_Class(data: divideUser):
    result = divideUserService.zeroDivideJjUser(data)
    print(result)

    return PityResponse.success_divideResult_xb(data =result)

@router.post("/checkClassFlag")
async def divide_Class_Check(data: divideUser):
    resp = divideClassFlagService.checkGoodsIDCourseClass(data.goodsId)
    return resp

@router.post("/checkClassBatchFlag")
async def divide_Batch_Check(data: divideUser):
    resp = divideClassFlagService.checkjjClassFlag(data.goodsId)
    return resp