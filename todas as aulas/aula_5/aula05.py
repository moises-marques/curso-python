import random

num_i=10  #class numero int
num_f=5.2 #class float
num_c=1j  #class complex

num_r=[
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
    ]



print("valor 1: " + str(num_r[0]))
print("valor 2: " + str(num_r[1]))
print("valor 3: " + str(num_r[2]))
print("valor 4: " + str(num_r[3]))
print("valor 5: " + str(num_r[4]))
print("valor 6: " + str(num_r[5]))
#OPERAÇÃO DE QUEST PARA STRING 

#Nao da pra contatena um inteiro com uma string 
#nem contatena uma string com type então é preciso
#converter. EX: str(x) e str (type(x))

# x=(num_i): Valor: 10 - <Class 'int'>
# x=(num_f): Valor: 5.2 - <Class 'float'>
# x=(num_c): Valor: 1j - <class 'complex'>

#(Passou um float mais fez um quest para um int)
#Ex: x=int(num_f) Valor: 5 - <Class 'int'>

# (Num int, convertido pra fload)
# x=float(num_int) Valor: 10.0 - <Class 'float'>

# (num_r=random.randrange gera valores aleatórios)
# EX:x=(num_r): Valor: 57 - <class 'int'>

# print("valor: " + str(x) + " - Tipo: " + str(type(x))) para todos esses de cima

#(Se eu quiser gera 6 valores diferentes entre (0 e 59))
#eu posso criar um arrey
#Gerando um valor aleatório para a primeira posição e 
#acrescentando mais cinco posição e gerando seis valor aleatório 

# num_r=[ Elemento do tipo list que é um Array
#     random.randrange(0,59),
#     random.randrange(0,59),
#     random.randrange(0,59),
#     random.randrange(0,59),
#     random.randrange(0,59),
#     random.randrange(0,59)
#     ]

# print("valor 1: " + str(num_r[0])) Valor: 1: 24
# print("valor 2: " + str(num_r[1])) Valor: 2: 38
# print("valor 3: " + str(num_r[2])) Valor: 3: 29
# print("valor 4: " + str(num_r[3])) Valor: 4: 40
# print("valor 5: " + str(num_r[4])) Valor: 5: 41
# print("valor 6: " + str(num_r[5])) Valor: 6: 16




