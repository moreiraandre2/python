from math import *

def calcular(x):
    res = sqrt(x)
    if res > 3 and res < 10:
        return res
    else:
        return 'Birl'

num = int(input("Digite um numero: "))
print(calcular(num))
lista = ['andre', '22/08/1987', 32]
for x in lista:
    print(x)
type(lista)
tupla = (32,33,33,35)
i = 0
while i < 4:
    print(tupla[i]) 
    i+=1
type(tupla)
dic = {'nome':'Adilson','idade':32,'altura':1.70}
print(dic['nome'])
print(dic['idade'])
print(dic['altura'])

for a in range(5):
    print(a)
print('------------')

for b in range(5,10):
    print(b)
print('------------')

for c in range(5,10,2):
    print(c)

print(pow(num,2))
num = num**3
print(num)
print(14 << 1)
print(14 >> 2)
