from 加法层的实现 import addLayer
from 乘法层的实现 import mutiLayer

apple_price = 100
apple_num = 2
orange_price = 150
orange_num = 3
tax = 1.1

#layer
appleLayer = mutiLayer()
orangeLayer = mutiLayer()
afterTaxLayer = mutiLayer()
appleAddOrangeLayer = addLayer()

# forward
apple_price_sum = appleLayer.forward(apple_price,apple_num)
orange_price_sum = orangeLayer.forward(orange_price,orange_num)
totalSum = appleAddOrangeLayer.forward(apple_price_sum,orange_price_sum)
afterTax = afterTaxLayer.forward(totalSum,tax)

print(afterTax)

#backward
dtaxAfterPrice  =1
dtotalPrice,dtax = afterTaxLayer.backward(dtaxAfterPrice)
dappleTotalPrice,dorangeTotalPrice = appleAddOrangeLayer.backward(dtotalPrice)
dapplePrice,dappleNum = appleLayer.backward(dappleTotalPrice)
dorangePrice,dorangeNum = orangeLayer.backward(dorangeTotalPrice)

print(dapplePrice,dappleNum)
print(dorangePrice,dorangeNum)