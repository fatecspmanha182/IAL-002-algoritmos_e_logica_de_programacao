"""
Dada a seqüência, calcular o cos:
"""

cos = 1.0
fatorial = 1.0
fator = -1.0
n = 1.0

while n % 2 != 0:
    x = float(input("Digite o ângulo em radianos: "))
    n = int(input("Digite o N: "))

for j in range(0,20):
    for i in range(2,3):
        fatorial *= i
        if i % 2 == 0:
            cos += fator*((j**i) / fatorial)
            fator *= -1
            # print(fatorial, cos)
    print(cos)

