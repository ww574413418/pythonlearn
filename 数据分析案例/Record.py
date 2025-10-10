# 数据定义
class Record:

    date:None
    order_id:None
    money:None
    province:None

    def __int__(self):
        pass

    def __init__(self,date:str = "",order_id:str = "",money:int = 0,province:str = ""):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"Record:[data:{self.date},order_id:{self.order_id},money:{self.money},province:{self.province}]"

    # 将对象转成dict类型
    def to_dict(self):
        return {
            "date": self.date,
            "order_id": self.order_id,
            "money": self.money,
            "province": self.province
        }


