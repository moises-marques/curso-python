# "str" É UMA STRING, CONVERSÃO FORÇADA DO n° inteiros
# quest converter do tipo inteiro para String

x=1 # int
#Ex: de Como execultar o x=1 nº int.
#Print("Valor: "+str(x))
#print("Tipo: "+str(type(x)))

x="Moisés marques" #O nome é uma string
x=15.6 #float, Nunero decimal
x=False # pode ser "x=true", também é "bool"
#Ex. de execução do String: "nome" / fload: "x=15.6" / boll: "False" ou "True"
#Ex: Print("Valor: "+str(x))
#print("Tipo: "+str(type(x)))


n1=5;n2=2;x=complex(n1,n2) #complex onde n1 é parte real e n2 é a parte imaginaria
n1=5;n2=2;x=complex(1j) #complex
#Exemplo de execução print(x.real)#parte real
#print(x.imag)# print(x.imag) #parte imaginaria
#print("Tipo: "+str(type(x)))


x=["Carro","Avião","Navio",1,58.3,True]  #O python chama o Array simples de List 
#Eu posso opera esse array se colocar o x[0]="Onibus", ele substitui o x[0]=["carro"]
#Exemplo de execução do array seimples list
#print("Valor: "+x[0])
#print("Tipo: "+str(type(x)))
#pode colocar tipo de dados diferente em uma coleção da lista
#Ex: x=[]"Carro","Avião","Navio",1,58.3,True]


("Carro","Avião","Navio",1,58.3,True)  
#Tupla: parece com a list, sendo que pode usar o indexador de execução normal da list
# Tupla modifica de couchetes para parenteses
#A Tupla do array é fechada, sendo que não da pra substituir um elemento
#EX:X[0="Bicicleta"]
#Exemplo de execução do array Tupla é o mesmo do array list
#print("Valor: "+x[0])
#print("Tipo: "+str(type(x)))


x=range(0,100,1) #um range de 0 a 100 permite que ele criou uma lista de 0 a 100
#Um range permite defini um array um list de forma facil
#Exemplo de execução do array Tupla é o mesmo do array list
#print("Valor: "+str(x))
#print("Tipo: "+str(type(x)))
                                    
x={
    "canal":"Moises cursos",
    "curso":"Curso Python",
    "nome":"Moisés Marques"
}
 #Dict: é o elemento {}-chave, valor
   #Dict significa dicionário
   #Para especificar um Dict, usa a chave com a anotação da list 
   #Ex: print("Valor: "+x["canal"])
   #com a anotação da list, informa qual chave quer imprimir
#Exemplo de execução do dict
#print("Valor: "+x["canal"])
#print("Tipo: "+str(type(x)))
   
   
   
x={5,7,4,5,7,4,8}   #Tipo set é dedicado com as chaves -> {}, 
#onde adiciona os elementos, onde não repete valores. 
# como execultar o Tipo set. Ex print("Valor: "+str(x))
print("Valor: "+str(x))
print("Tipo: "+str(type(x))) #type, retorna o tipo do objeto