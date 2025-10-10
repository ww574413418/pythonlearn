# 实现中有两个共通的方法（接口） forward()和 backward()。forward()
# 对应正向传播，backward()对应反向传播。
# 现在来实现乘法层。乘法层作为 MulLayer类

class mutiLayer:


    def __init__(self):
        x = None
        y = None

    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x*y
        return out

    def backward(self,dout):
        # 翻转 x y
       dx = dout * self.y
       dy = dout * self.x

       return dx,dy

if __name__ == '__main__':
    apple = 100
    apple_num = 2
    tax = 1.1

    # layer
    mul_apple_layer = mutiLayer()
    mul_tax_layer = mutiLayer()
    # forward
    apple_price = mul_apple_layer.forward(apple, apple_num)
    price = mul_tax_layer.forward(apple_price, tax)

    print(price)

    # backward
    dprice = 1
    dappleTotlPrice,dtax = mul_tax_layer.backward(dprice)
    apple_price,apple_num = mul_apple_layer.backward(dappleTotlPrice)

    print(dtax,apple_price,apple_num)