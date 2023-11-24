curso="Curso de Python"
# Uma string nada mais é do que um array 
# de uma lista de caracteres 
# O operador de indexão, o couchete pode ser ultilizado com um array

# Se eu quiser imprimir alguma posição determinada do meu array 
# eu consigo, basta coloca o operador de indexação e indicar a posição
# desse array que eu quero imprimir
# Então se eu imprimir, na posição "0", irá aparecer a letra "C"
# e assim por diante as demais letras sendo posição 1,2,3,4,5 e ETC
# EX:Ex: print(curso[0]) LETRA "C" 
# Ex: print(curso[1]) LETRA "u" 
# Ex: print(curso[2]) LETRA "r"

# Também posso imprimir de uma posição a outra ao mesmo tempo
# Ex:print(curso[0:5]) e irá imprimir "CURSO"
# até os espaços entre letras contam como números também.

# Eu consigo delimitar uma faixa de intervalo na minha impressão.
# Podemos usar uma série de funções, métodos implementado pra quele tipo de String 
# eu posso ultilizar o método len. O len retorna o tamanho da string 
# EX:print(curso[9:15])
#    print("Tamanho: " + len())


# O método strip remove espaço do inicio e do fim da string. Ex: " Curso de Python "
# Ex:print(curso.strip())

# Função lower converte a string para minúsculo
# Ex:print(curso lower())

# Lower com strip junto, coloca minúslulo e tira espaço
# Ex:print(curso.lower().strip())

# Função upper converte tudo em maiúsculo
# EX:print(curso.upper().strip())

# Função replace faz a substituição de uma string por um caracter 
# por outra string o outro caracter
# Ex:print(curso.replace("Python","c#")). Troca a palavra "Python" por "c#""

# Função split. Ela faz uma subdivisão na nossa string pelo indicador que indicarmos. 
# Ex: da um split no espaço("  ") ele vai da um corte. O resultado desse split eu quero
# que seja armazenado na variável a
# Porque tem "curso", porque fez o split, onde encontrar o espaço e retorna um list, u array
# Ex: a=curso.split("  ")
# print(a[0])
# a=curso.split("."). Essa função quebra os espaços executando toda a frase "Curso de Python"


# print(curso[9:15])
a=curso.split(".")
print(a[0])
print("Tamanho: " + str(len(curso)))

