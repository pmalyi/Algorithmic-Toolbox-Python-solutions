money = int(input())
num10 = money // 10
num5 = money % 10 // 5
num1 = money % 5
numCoints = num10 + num5 + num1
ns10 = "10 " * num10
ns5 = "5 " * num5
ns1 = "1 " * num1
resS = ns10 + ns5 + ns1;
print(resS)
print(numCoints)