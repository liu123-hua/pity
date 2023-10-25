from enum import Enum, unique


@unique
class ProjectChannelEnum(Enum):
    """
     业务线对应的渠道类型枚举
    """
    CS = "tg_wx_v1-0306_testlqh_a"
    QN = "tg_wx_v1-0821_testlqh"
    LC = "tg_wx_v1-0421_lqh_default"
    DSP = ""


if __name__ == '__main__':
   print(ProjectChannelEnum['CS'].value)


