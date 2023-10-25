from enum import unique, Enum


@unique
class ProjectMsEnum(Enum):
    """
     业务线对应的渠道类型枚举
    """
    CS = "1"
    QN = "2"
    LC = "3"
    DSP = "5"