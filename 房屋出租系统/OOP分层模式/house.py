# @Version  : 1.0
# @Author   : Deeo
# Time      : 2024/7/11 17:57
"""
    说明: 数据层: House类，  一个House对象表示一个房屋信息
"""


class House:
    def __init__(self, id, name, phone, address, rend, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rend = rend
        self.state = state

    # 重写__str__ 按照指定的格式输出对象
    def __str__(self):
        return f"{self.id}\t\t{self.name}\t\t{self.phone}\t\t{self.address}\t\t{self.rend}\t\t{self.state}"
