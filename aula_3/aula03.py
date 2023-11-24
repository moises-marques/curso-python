num1=num2=res=0
# canal="CBF Cursos" #esta em escopo global, fora, externo

def cn():
    global canal
    canal="Moises marques" #escopo agora está dentro da função "def cn()", é local
                              #da pra acessa essa variavel canal, desde que defina como "global"
cn()

print(canal)