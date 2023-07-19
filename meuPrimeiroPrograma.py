print("Hello")

#Tipos de dados
    #- define as as caracteristicas e comportamentos
    # de um valor para o interpretador
#Classes de Tipos de dados
int()
float()
str()
bool()


#Numéricos
    # int, float, complex
print(11+10, type(11+10))
print(11.4+0.5, type(11.4+0.5))

#Sequência
    # list, tuple, range
BRAZILIAN_STATES = ["SP","RJ","SC"]
print(BRAZILIAN_STATES, type(BRAZILIAN_STATES))

#Mapa
    # dict
#Coleção
    # set, fronzenset

#Booleanos
    # bool
isEquals = 100/0.5==200
print(isEquals, type(isEquals))


#Texto
    # str
py1 = "Python"
print(py1, type(py1))


#Binário
    # bytes, bytearray, memoryview

#Variáveis
    # valore que sofrem alterações no decorrer 
    # do programa
age = 28
print(age, type(age))

#Constantes
    # não existe uma clausula de declaração de constantes,
    # por padrão são declaradas com maiúsculo, SNAKE_CASE
CODIGO_CLIENTE = "232"
print(CODIGO_CLIENTE, type(CODIGO_CLIENTE))


#Conversão de tipos
    #
print(int(1.93453453), type(int(1.93453453)))

saldo = float(CODIGO_CLIENTE)
print(saldo, type(saldo))

saldoInt = int(CODIGO_CLIENTE)
print(saldoInt, type(saldoInt))

saldoDiv = saldoInt/2
print(saldoDiv, type(saldoDiv))

saldoDoubleDiv = saldoInt//2
print(saldoDoubleDiv, type(saldoDoubleDiv))

codigoClienteString = str(CODIGO_CLIENTE)
print(codigoClienteString, type(codigoClienteString))

codigoClienteStringConcat = f"idade {age} saldo {saldo}" 
print(codigoClienteStringConcat, type(codigoClienteStringConcat))


#INPUT OUTPUT
    # função builtin input(, utilizada)
    # quando queremos ler dados
    # da entrada padrão (teclado).
    # ela recebe um argumento do 
    # tipo string, que é exibido 
    # para o usuário na saída padrão (tela). A função lê a
    # entrada converte em string e 
    # retorna o valor
#nome = input("Informe o seu nome: ")
#sobreNome = input("Informe o seu sobrenome:")

    #função builtin print() é utilizada 
    # quando queremos exibir dados na 
    # saída pradrão (tela). Ela recebe um 
    # argumento obrigatório do tipo varargs
    # de objetos e 4 argumentos opcionais
    #(sep, end, file, flush). Todos os objetos 
    # são convertidos para string, separados 
    # por sep e terminados por end. A string 
    # final é exibida para p usuário.
#print(nome,sobreNome)
#print(nome,sobreNome, end="...\n")
#print(nome,sobreNome, sep="...")



#Manipulando strings
    # a classe String do python 
    # é rica em métodos e possui uma 
    # interface fácil de trabalhar

meu_nome = "Pedro Marcos Ramos"

print(meu_nome.upper())
meu_nome = meu_nome.lower()
print(meu_nome)
print(meu_nome.title())
meu_nome = " Pedro Marcos Ramos "
print(meu_nome.strip())
meu_nome = " Pedro Marcos Ramos "
print(meu_nome.lstrip())
meu_nome = " Pedro Marcos Ramos "
print(meu_nome.rstrip())
meu_nome = " Pedro Marcos Ramos "
print(meu_nome.center(25,"#"))
print(".".join(meu_nome.strip()))#join funciona com todo tipo de iteravel



#Interpolação de variáveis

    # % , format, f''
    # é recomendado o uso de f strings
nome = "Pedro"
idade = 32
profissao = "Learn Hacker"
linguagens = ["Java", "Python"]

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como  %s"%(nome,idade,profissao))
print(f"Olá, me chamo {nome}. programo em {linguagens}")
print("Olá, me chamo {}".format(nome))
print("Olá, me chamo {0}. Eu tenho {1} anos de idade.".format(nome, idade))
print("Hello, my name is {name}. I have {age} years old.".format(name =nome, age=idade))
PI=3.14159
print(f"Valor de PI:{PI:.2f}")
dados = {"nameData" : "Pedro", "ageData" : 32}
print("Nome:{nameData}, idade:{ageData}".format(**dados))


# String multi-linhas

mensagem = f"""
Olá meu nome é {nome},
   estou aprendendo {linguagens[1]}
"""

print(mensagem)

