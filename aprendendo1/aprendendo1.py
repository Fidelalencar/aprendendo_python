# Em Phyton, as FUNÇÕES sempre vem seguidas de parênteses e as KEYWORDS não (apesar de parecerem ser funções).
# site para rodar phyton online: https://repl.it/languages/python3

#### KEYWORDS

def nnnn(): # define função nnnn() e dentro dos parênteses coloca-se os parametros entre virgulas
return xxxx
assert xxxx # é usada para criar verificações do código dentro do proprio código

import xxxx    # importa um "pacote" xxxx de funções

in   #

if    # adiciona uma condição
elif  # adiciona uma nova condição
else: # depois de uma ou mais condições, adiciona a ação para os casos que não se encaixam nas condições


while
for


#### FUNÇÕES 

type() # indica qual o tipo do objeto

# Tipos de Objeto
    # interger, int   # números inteiros
    # boolean, bool   # True ou False
    # string, str #
    #    # número com casa decimal finita
    #    # número com casa decimal infinita, logo aproximado

    # tuple (ver aula 3) são como listas, mas que você não consegue mudar os valores. Para isso, é preciso mudar para outro tipo... Pode ser usado para não permitir que modifiquem uma lista, por exemplo.


abs() # é tipo o módulo de um número

xxxx = input("insira um valor: ")  # pede ao usuário ("através da string") que insira um valor q será atribuido à variável xxxx 

print("texto {}".format(nnnn)) # o texto xxxxx é seguido pela variável (nnnn) no lugar das chaves {}
print("texto {} texto {}".format(nnnn, mmm)) # é possível fazer 2 inserções de variáveis, sempre em ordem

len(x)  # informa o tamanho, no de characters (length), de x



################
#### AULA 2 ####
################

# https://docs.python.org/2/library/stdtypes.html?highlight=count#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange DOCUMENTAÇÃO sobre Strings 7.1

# Quando se escreve strings é possível usar ' ou ". Tanto faz. 

# SOBRE INDEX COM STRINGS:

#         01234567  # essa é a 'ID' q ele dá aos characters da coleção (PORTANTO, e' non-inclusive - no final)
#         12345678  # no entanto, quando se pede uma sequencia, a numeracao nao começa do zero 
string = "abc fgh!"

# buscando elementos:
string[0]    # a
string[4]    # f
string[-1]   # !      # Numera a partir do 1 na ordem inversa
# buscando sequencias de elementos:
string[0:8]  # abc fgh!
string[:8]   # abc fgh!
string[1:8]  # bc fgh!   (PORTANTO: e' inclusive no final, MAS NON-INCLUSIVE no inicio)
string[::2]  # acfh   # Responde de dois em dois

string[-:3]  # ERRO!!: Aparentemente nao tem como pedir sequencias na ordem contraria. 
##

enumerate()  # quebra uma coleção (de type enumerate) em cada um de seus valores e seus indexes

# E' util usar o for com index, caracter e com enumerate()
""" 
def count_in_position(a_string, a_char, position_type):
    count = 0
    for index, current_char in enumerate(a_string):
        if a_char == current_char:
            if position_type == 'even' and index % 2 == 0:
                count += 1
            elif position_type == 'odd' and index % 2 != 0:
                count += 1
return count
"""


########################
#### AULA 3 : Introduction to collections
########################

# Introdução a Collections - Armazenam valores simultâneamente
# Diferentes tipos de collections dão diferentes resultados (velocidade)
# As alula trata de listas, strings e stacks (pilhas)

a = ["asd", "asd","ad"]  # listas. Podem receber qualquer tipo de dado, mas é melhor que sejam do mesmo tipo
# as listas preservam a ordem dos elementos
# as listas são mutable. Outras collections não são.



# Criando uma lista a partir de um string de texto
nomes = ""
andreza, fidel,
ze
""                     # aqui temos um elemento (salvo como a variável nomes) com várias coisas escritas

pessoas = nomes.split(',')    # A função split apaga todos os espaços em branco e quebra o "texto" em uma lista usando o elemento entre aspas (vírgula).  
                              # o oposto (reunir elementos num só) é feito com   .join   : pessoas.join

pessoas = ["fidel", "andreza", "ze"]   # Aqui é a forma de criar a mesma lista de elementos. (sem partir to texto desorganizado)
# Uma característica fundamental das listas (diferente de outras coleções) é que elas mantém a ordem dos elementos
# IMPORTANTE: ORDER é diferente de SORT   -> Os eementos podem ser sorted em outra ordem!


# Adicionar elementos a uma lista
pessoas = []                # Aqui criamos a mesma lista, mas adicionando elementos. Também serve: pessoas = list()
pessoas.append("fidel")     # Com append, voce sempre adiciona o novo elemento ao fim
pessoas.append("andreza")   #
pessoas.append("ze")        #

pessoas.insert(4, "ze")           # com insert, vc precisa dizer o lugar (index) onde será adicionado

lista_x = []     # Para adicionar elementos repetidamente a uma lista (em loop), também é possível usar a concatenação
lista_x += [posi,] # Mas lembrar de mostrar q a variável é um elemento de lista. Usa-se [ ,]


# SOBRE INDEX COM LISTAS

# Indexes, como muitas outras funcoes, funcionam do mesmo modo para listas e strings.
string = "abcdefg"    
lista = ["a", "b", "c", "d", "e", "f", "g"]

# Essa notacao pega os elementos de 2 em 2 a partir do primeiro
string[::2] #   Responde: aceg
lista[::2]  #   Responde: ['a', 'c', 'e', 'g']

# pegando o indice de um elemento
index_f = pessoas.index(fidel)   # retorna o index em que está salvo fidel (e adiciona o valor à variável xxx)
index_z = pessoas.index(ze)


      print(pessoas[index_f: index_z])   # aqui retorna todos os indexes que estão no intervalo
      print(pessoas[index_f: index_z + 1])   #aqui ele retorna a mesma lista de indexes incluindo o de ze 
      print(index_a, index_z)   # imprime somente os selecionados


nova_lista_pessoas = pessoas.copy()   #aqui criamos uma cópia da lista.
                                      # O que é diferente de copiar somente uma variável que acessa os mesmos valores: pessoas = nova_lista_pessoas





# ! CONCEITO IMPORTANTE: Há as operações MUTABLE e as UNMUTABLE   
# # refere-se a se as operações mudam os valores com que vc está trabalhando.
pessoas.remove(ze)   # remove zé da lista.  
#IMPORTANTE: o elemento é retirado e não retorna nada. (é uma função MUTABLE)
# a tentativa de salvar o objeto:   y = pessoas.remove(ze)   retonar   y = None
pessoas.pop()   # remove o último elemento ou o index que você colocar  
# o resultado é o objeto retirado (É uma função UNMUTABLE)
# se vc quer o objeto, é possível salvá-lo:   x = pessoas.pop()


# Contatenando Listas
lista_1.extend(lista_2)      # .extend adiciona os elementos da lista 2 à lista 1 (mutable)
lista_1 += lista_2           # faz o mesmo 
lista_3 = lista_1 + lista_2  # concatenation cria uma terceira lista com todos os elementos (immutable)


lista_a.sort()      # ordena  (mutable)
lista_b = sorted()  # ordena (immutable)
lista_a.sorted(reverse=True) # a funcao sorted() tem o parametro booleano reverse, que indica o sentido

sorted = sorted(pessoas)  # cria uma variável com os elementos em ordem alfabética.
# IMPORTANTE!!! Os elementos continuam fora de ordem na variavel pessoas (portanto, é UNMUTABLE)

min(lista_a)  # retorna o menor elemento (serve para lista, string, tuple)
max(lista_b)  # retorna o maior elemento


# a coleção STACK é LI-FO. "The Last in is the first out". Mas é tipo uma lista mesmo. Não entendi a diferença.


# a coleção TUPLE é uma sequencia com a diferença que ela é sempre IMMUTABLE
tuple1 = ("a", "b", "c")  # é feita com parênteses
tuple2 = ("a", )   # para criar tuple com 1 elemento, precisa colocar uma vírgula (ou ele acha q é 'str').

tuple(lista_a)  # converte a lista em tuple


### FOR loop 

lista = ("arma", "bola", "caderno", "dedo")
for objeto in lista:  # para retnornar os objetos da lista, "Para cada elemento da lista, retorne o elemento"
    print(objeto)
    return elemento

import random   # chama o pacote random
lista_aleatoria = random.choices(lista, k = 2)  # escolhe aleatoriamento dois elementos da lista
print(lista_aleatoria)

    ### ATENÇÃO !!!!!! LEMBRAR!!!
    for _ in lista:   # apesar de ele estar interagindo com cada objeto,
        lista2 += _   # essa forma adiciona cada caracter como novo elemento da lista
        lista2 += _,  # para ele adicionar objeto por objeto, é preciso da , (virgula) 
    ###


# FOR loop com outras funções (range, enumerate,  )

range(0, 10, 2)  # gera uma "lista" numérica a partir de zero, com 10 elementos (até 9) de dois em dois
# na verdade não é uma lista. É uma coleção RANGE, que serve pra facilitar processamentos grandes
range(10, 0, -1) # cria um range inverso
list(range(0,10,2))  # A lista de verdade seria gerada assim
for i in range(5)   # Essa função pode ser útil para usar com o for-loop. Mas não entendi exatamente como.


list(enumerate(lista_a)) # exibe os elementos da lista e suas posições (index)
list(enumerate(lista_a, 1)) # também é possível que as posições sejam contadas a partir do 1


for posic, char in enumerate(lista_x) # o for reconhece dois "parâmetros" em enumerate(). O index e o caracter.
            # é possível usar esses parâmetros... 
            # ATENÇÃO: O index sai como inteiro e o caracter como string
            # Parece fundamental para trabalhar com strings, pq "enfatiza" o número(index) de cada caracter
    


dados_maria = (30, "maria", "da silva") # se você tem uma lista (tuple) de dados,
idade, nome, ultimo_nome = dados_maria  # você pode atribuir um nome para a coluna em seguida


########################
#### AULA 4 : DICT e SET
########################

## DICT
# A coleção dict (dicionário) serve para atribuir KEYs (tags) (labels) próprios para cada valor.
x = {                           # é criada com chaves 
    "primeiro" : 5023.03,       # para cada valor, cria-se um KEY separado por :
    "veloz" : 4993.87,          # acho q os keys só podem ser str
    "ultimo" : 2345.04,         # todos os valores precisam ter keys
    "incompleto" : "não teve"   # os valores tb podem ser strings
}

x["primeiro"]   # acessa o valor com esta key
x = dict()  # criar dicts vazios
x = {}
x.keys()   # retorna uma lista com todas as keys do dict
x.values() # retorna uma lista com todos os valores do dict
x.items()  # retorna um tuple com todas as "duplas" (key, valor) de um dict


# adicionando ao dict
x["country_code"] = 81   # para adicionar valores ao dict é preciso colocar  a key e o valor.
x.update({"fav": 31, "worst": 64}) # adiciona um dicionário a outro dicionário x

# Atualizando valores. 
x["country_code"] += 1   # Se o key já existe, assim vc adiciona 1 ao valor:  81 -> 82 

# deletando valores
del x["country_code"]  # apaga o valor do dict, mas não retorna nada
code = x.pop["country_code"]  # apaga o valor do dict, mas permite salvar o valor retirado 

# Dict tem a propriedade de os itens NAO terem uma ORDEM
# Dicts operam MUITO RAPIDO. São coleções eficientes para o processamento.

# Interagindo com od DICTs. A forma standard de interagir com os dicts é através das keys
for key in x             # faz um for-loop pelas keys. É o normal
for values in x.values   # para fazer um for-loop pelos valores é preciso adicionar .values 


for key in price:        # para interagir com os keys e os valores do dict 
    value = price[key]   # é preciso chamar também o valor
    print("Today's '{}' was: {}".format(key, value))

for key, value in price.items()   #  também é possível acessar keys e valores simultâneamente usando .items()



## SET

# São como os conjuntos da teoria dos conjuntos na matemática. Sao uteis na sua funcao, mas de uso nao muito comum.
# os elementos do Set não tem ordem. E só existe 1 elemento de cada. Não existem duplicatas.
# operações com a operação in são extremamente eficientes com sets (pq a ordem nao importa)

s = {1,2,3} #cria set
s = set() #cria set
s = {} # vazio, cria um dict, nao um set

s.add(a)  #adiciona o elemento a. (Não tem index)
s.update(s1)  # adiciona um set a outro

s.pop()  # retira um elemento  . Como os outros pops, retorna o elemento removido e salva o set sem o elemento
s.remove(x) # retira o elemento x contido no set. Logo, é preciso saber qual elemento será removido
s.discard(x) # é igual ao .remove, mas ele não dá erro se vc colocar um elemento não existente no set. ! .remove da erro

s1 | s2  # Uniao
s1 & s2  # Intersecao
s1 - s2  # Diferença
s1 < s2  # checar sub-conjuntos  => Responde true ou false a respeito da quantidade de elementos


## HASHTABLES

# Tabelas de dispersao
# hashtables sao "tabelas" baseadas em funcoes.  
# operações com hashtable exigem muita memoria, mas são computacionalmente eficientes
# Sets são bons para implementar hashtables sem ter que lidar com muitas de suas complexidades. 


############
# SOBRE ANDS e ORS 
# (O exercicio que origina esse exemplo está nas anotacoes da aula 5)
# Pergunto: Qual a diferenca entre esses tres ifs?:
# 1.
if animal_type not in (animal['animal_type'] and animal['street_name']):
    continue
result.append(animal)
# 2.
if animal_type not in (animal['animal_type'] or animal['street_name']):
    continue
result.append(animal)
# 3.
if animal_type not in animal['animal_type'] and animal_type not in animal['street_name']:
    continue
result_animals.append(animal)

# Como estou entendendo:
# A terceira parece ser a correta, porque 'not in' é mais forte 
# Por isso, o "estilisticamente"(?) correto deve ser sempre repetir essa parte quantas vezes for necessario. 
# Como se fosse assim  =>   ('a' is not 'b')  and  ('a' is not 'c')
#           nunca      =>    'a' is not ('b' and 'c')
#           nem        =>    'a' is not ('b' or  'c') 






