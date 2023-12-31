#bytes data type 
ourlist = [1,2,3,4,5,6,7,8,9,0,255]
b =  bytes(ourlist)
print (type(b))

# bytes bytearray
b1 = bytearray(ourlist)
b1[1] = 100
print(type(b1))
print(b1[1])