from typing import List

from pydantic import BaseModel, validator



class divideUser(BaseModel):
    goodsId: str = ""
    usersId: List[int] = None
    assignClassInfoId: str = None
    revenueProjectId: str = ""
    courseVersionId: str = ""
    divideType:str = ""

