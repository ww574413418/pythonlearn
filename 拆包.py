tuple = (1,2,3,4)

a,b,c,d = tuple

print("a=",a,"b=",b,"c=",c,"d=",d) # a= 1 b= 2 c= 3 d= 4

a,b,*c = tuple
print("a=",a,"b=",b,"*c=",*c) # a= 1 b= 2 *c= 3 4

