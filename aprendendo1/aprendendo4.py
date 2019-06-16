#########################################################
#### AULA 13 : Advanced Functional Programming ##########
#########################################################

# Intro: 
# Funcoes, seus argumentos e default_arguments
# keyword_arguments sao aqueles que na invocacao de uma funcao sao colocados com o seu keyword
# default arguments e keyword_arguments sao diferentes
def asdf(*arg, **kwarg):  # o primeiro cria tuples, o segundo cria dicts
# isso flexibiiza a criacao de funcoes

def sum_multiple(*args):   # implica q se pode inserir uma quantidade indefinida de argumentos
    if not args:
        raise AttributeError("One must pass numbers to sum")    
    return sum(args)

# ver exercicio #3 da aula seguinte 



# Conceitos importantes de PROGRAMACAO FUNCIONAL
# Conceitos de funcoes Immutable e Mutable
# Immutable (nao altera o dado original, responde um resultado) 
# Mutable functions (altera o dado original)
# se e' possivel usar as duas solucoes, tende-se a preferir a solucao immutable



# LAMBDAS - 
# servem para criar versoes mais consisas de funcoes
# lambda e' outra forma de fazer funcoes. sao chamadas funcoes anonimas
# Com lambdas vc nao pode usar if, nem for-loop. Sao mais restritas, portanto.
def add(a,b):                # imagine essa funcao
    return a + b

add = lambda a, b: a + b     # essa e' a sintaxe equivalente



# LISTA DE FUNCOES. E' possivel criar uma lista de funcoes
add = lambda a, b: a + b 
subt = lambda a, b: a - b 
l = [add, subt]   #lista de funcoes  
l[0](7,5) # INVOCANDO a lista, primeiro vc diz o index da funcao desejada, depois passa os parametros
t = [add, 'hello', subt] # tambem e' possivel adicionar outras coisas q nao funcoes 
t[1](7,5) # nesse caso, vai dar erro, pois esses parametros nao fazem sentido apos o str. Assim: 'hello'(7,5)
# Outra forma de operar funcoes, com funcoes
def compute(a, b, operation):
    return operation(a, b)
compute(7, 5, subt)  # chamando a funcao


# USANDO LAMBDAS de forma mais criativa
d = {'jane':7, 'ze': 6, 'antonio': 8}
list(d.items()) # transforma os pares do dict em elementos de uma lista
# ... Perdi (acho que e' o final do segundo video)




# 3 importantes CONSTRUTOS FUNCIONAIS do paradigma da programacao funcional: map(), filter(), reduce()
# MAP
# map repete funcoes que devem transformar CADA UM DOS ELEMENTOS dos dados iniciais
result = map(get_length_of_name, list_of_names) 
# A sintaxe e': primeiro a funcao a ser aplicada, depois o dado para aplica-la
# No caso, get_length_of_name() e' uma funcao predefinida que converte os elementos da list_of_names em seus len()
result = map(len, list_of_names) # no caso, poderia ser simplesmente assim
result = map(square, l)  # Outro exemplo de funcao (square) que sera realizada para cada elemento de l
result = map(lambda x: x ** 2, l) # outro uso de map() + lambda
result = map(lambda n: n[::-1], list_of_names) # outro exemplo

# FILTER
# filter repete funcoes que selecionam o dado original (por uma condicao nela dada)
# para cada elemento o resultado e' O MESMO da entrada, a diferenca e' que nao retornam os filtrados
result = filter(lambda n: len(n) >= 4, l)      # exemplo com filter + lambda
result = filter(lambda n: len(n) % 2 == 1, l)  # outro exemplo com filter + lambda
# PERCEBER: map() e filter() sao immutable.

# REDUCE
# E' mutable. E' o construto mais problematico. Ele foi tirado do python 3.
from functools import reduce # portanto, tem que ser importado
# Serve para unir elementos em um so'. O exemplo simples e' a soma. Une tudo em unico elemento.
# Em suma, map() e filter() sao mais importantes.
# um exemplo
from functools import reduce
def mult(terms):
  return reduce(lambda a, b: a*b, terms, 1) # sintaxe: primeiro vem a funcao a ser aplicada,
                                            # terms e' a fonte dos dados a ser trabalhados
                                            # 1 e' um parametro opcional, acho q o index do comeco das interacoes

mult([5, 6, 7])  # retorna a multiplicacao




# LIST COMPREHENSIONS
# Sao uma das caracteristicas fundamentais da programacao em python. (pythonica, uau!)
# normalmente se pensa como algo avancado, mas qnd se conhece as bases, entende-se que sao parte dos fundamentos.
# List comprehensions sao construidas em cima dos construtos map() e filter(). Sao outras formas sintaticas delas.
# Sintaxe das list comprehension : [<EXPRESSION> for elem in <COLLECTION> if <CONDITION>]

# exemplo1:
result = map(len, list_of_names)  # funcao com map()
list(result)

[len(n) for n in list_of_names] # ISSO e' uma list comprehension equivalente


# exemplo2:
result = []
for k, v in d.items():           # uma funcao equivalente ao uso de map()
    new_elem = k * v
    result.append(new_elem)
result

[k * v for k, v in d.items()]   # uma list comprehension equivalente


#exemplo3: list comprehension com map e filter
result = filter(lambda n: len(n) >= 4, list_of_names)
list(result)

[n for n in list_of_names if len(n) >= 4]     # list comprehension equivalente


#exemplo4: list comprehension com map e filter
result = filter(lambda n: len(n) % 2 == 1, list_of_names)
list(result)

[n for n in list_of_names if len(n) % 2 == 1]  # list comprehension equivalente


#exemplo5:
result = []
for name in list_of_names:                        # Solucao classica
    if len(name) % 2 == 1:
        result.append(len(name))
result


result = map(
    lambda n: len(n),                             # Solucao com Lambda
    filter(lambda n: len(n) % 2 == 1, list_of_names)
)
list(result)


[len(n) for n in list_of_names if len(n) % 2 == 1]  # Solucao com List Comprehension. SOLUCAO PYTHONICA.


#exemplo6: Criando funcao com Lambda + List Comprehension
# uma funcao que converta uma lista de temperaturas de celsius para fahrenheit
def to_fahrenheit(a_list):
    result = lambda x: x * 9/5 + 32)
    return [result(x) for x in a_list]    # Aqui, a solucao separando lambda da list comprehension

def to_fahrenheit(a_list):                                  # Aqui, a solucao com tudo numa so linha.   
    return [(lambda x: x * 9/5 + 32) (x) for x in a_list]   # O (x) chama a funcao imediatamente criada com lambda


#exemplo7: Nested list comprehension: 
# Uma funcao que retorna todos os valores de a_list que sao divisiveis por todos os termos de a_list_of_terms
def divisible_numbers(a_list, a_list_of_terms):
    return [x for x in a_list if all([x % t == 0 for t in a_list_of_terms])]  # Nao entendi direito


#exemplo8: list comprehension com lambda + reduce e com if + else
# uma funcao recebe uma lista e retorna um string com os itens separando-os com espaco+virgula, mas no ultimo com and
def comma_code(a_list):
    from functools import reduce  #             
    return reduce(lambda x, y: x + ", " + y if y != a_list[len(a_list)-1] else x + " and " + y, a_list)
# tb funciona:
def comma_code(a_list):
    from functools import reduce
    funcao = lambda x, y: x + ", " + y if y != a_list[len(a_list)-1] else x + " and " + y
    return reduce(funcao, a_list)






##########################################
#### AULA 14 : File Management  ##########
##########################################


# Python e' cada vez mais utilizado para file management
# Mas essa area exige muito codigo, muita correcao, muita sugestao de causa de erro, etc.
# E' uma area complicada pq sao mts cenarios possiveis para dar erro: diferentes arquivos e sists. operacionais, etc.


# COMANDOS BASICOS:
# 1)Abrir arquivos:
f = open('data.csv', 'r') # arquivo + modo (leitura, edicao, append, etc. = r, w, a, ...)
# o modo read 'r' e' o padrao e pode ser omitido
f.read()   # f se torna o file em uso - a funcao manda le-lo inteiro (Nesse caso, cuidado com o tamanho do arquivo)

with open('data.csv', 'r') as my_file:  #esse metodo e' mais usado, pois cria uma versao para uso (my_file), 
    # e fecha o arquivo ao final das linhas de codigo. portanto, otimiza o uso da memoria  



# 2)Operando o pointer(cursor) dentro de um arquivo
f.read()   # le todo o arquivo como str (caracter por caracter)
f.read(10) # funciona como um cursor (pointer). Ele vai ler os prxms 10 caracteres a apartir de onde esta no momento
f.tell()   # diz a posicao do cursor
f.seek(0)  # volta para a posicao zero
f = open('data.csv', 'a')  # quando se abre no modo append, o cursos comeca no fim do arquivo


# 3)O que python deve ler
f.readline()     # trata o dado como string. Le toda a linha ate encontrar um 'caracter de nova linha' (\n)
f.readlines()[3] # transforma o dado em lista de linhas. Le a linha do correspondente index
f.readlines()    # transforma as linhas em uma lista de linhas 

for line in f:   # Serve para ler linha por linha  PERCEBER!!! 
    print(line)


# 4)Escrevendo
f = open('data.csv', 'w') # abre permitindo escrever. CUIDADO, vai mudar o arquivo.
f.write('hello\n', 'World!')    # escreve esse conteudo na primeira linha. CUIDADO, vai mudar o arquivo.


# 5)managing 
f.close()     # Salva o arquivo e Fecha, para poupar a RAM. Ou ao final 
f.flush()     # salva, fecha e abre o arquivo como esta. #acho


# 6)Lidando com erros: Criar bloco  try/except/finally


# LIDANDO COM .CSV: 
#1) abrindo o .csv
import csv
reader = csv.reader(f)

#2) importando um .csv como um list por linha
i = 0
for line in reader:
    if i == 10:   # digamos que vc so' queira as 10 primeiras linhas
        break
    print(line)
    i += 1

next(reader) # next() retorna a proxima lista, ou seja, a prxm linha 

#3) Escrevendo em um .csv
f = open('./products-new.csv', 'w')  
writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL) # existem mts configs. nesta, os campos sao todos quoted 
# cuidado com os dialetos de csv, na hora de abri-los e' possivel informa'-lo nos parametros
writer.write(['Invoice Number', 'Customer', 'Total'])  # escrevendo o cabecalho (header)
writer.write([38192, 'John Doe', 117.32])              # escrevendo as linhas (rows)
f.close() 


# EXEMPLOS DE EXERCICIOS
#1. funcao que diz a linha onde esta um string dado 

def which_line(filepath, a_string):   # minha solucao. trabalha o arquivo ainda como string
    with open(filepath) as data:      # Usa o count para dizer o intervalo ("linha") em q se encontra a string dada dentro da string analisada
        count = 0
        for line in data:
            count += 1
            if a_string in line:
                return count
        return None

def which_line(filepath, a_string):   # solucao da licao
    with open(filepath) as data:
        read_data = data.readlines()
        for line_num, line in enumerate(read_data): # usa enumerate. E' melhor para grandes processamentos 
            if a_string in line:
                return line_num + 1
        return None

def which_line(filepath, a_string):   # outra solucao
     with open(filepath) as data:
        read_data = data.readlines()  # transforma o dado em lista de linhas
        for line in read_data:
            if a_string in line:
                return read_data.index(line)+1
        return None

#2. recebe um string com uma palavra por linha e retorna um dict {primeira letra de cada palavra : quantas palavras com essa letra}

def counter_by_letter(filepath):
    with open(filepath) as data: 
        data = data.readlines() # solucao so colocando as letras das palavras no arquivo
        letters = {}
        for line in data:
            if line[0] in letters:
                letters[line[0]] += 1
            else:
                letters[line[0]] = 1
        return letters

import string
def counter_by_letter(filepath):
    with open(filepath) as data: 
        data = data.readlines()
        letters = dict([(letter, 0) for letter in string.ascii_lowercase])  # solucao colocando as letras sem palavras correspondentes :0
        for line in data:
            if line[0] in letters:
                letters[line[0]] += 1
            else:
                letters[line[0]] = 1
        return letters


#3. funcao que receba varios enderecos de arquivos e responda o nome do arquivo q tem mais linhas
def max_lines(*file_names):
    lines = 0
    for file_name in file_names:
        with open(file_name) as data:
            read_data = data.readlines()
            if len(read_data) >= lines:
                lines = len(read_data)
                name = file_name
    return name


#4. funcao recebe um endereco de arquivo e uma lista de strs. Ela escreve cada str em uma nova linha (no arquivo dado)
def write_lines(filepath, list_of_strings):
    with open(filepath, 'w') as data:
        for string in list_of_strings:
            data.write(string + '\n')


#5. funcao q escreve um str dado num arquivo. O parametro condicional indica se: adiciona ao final ou sobrepoe 1a linha
def write_string(filepath, a_string, overwrite_all=False):
    if overwrite_all == False:
        with open(filepath, 'a') as data:        
            data.write(a_string + '\n')
    else:    
        with open(filepath, 'w') as data:
            data.write(a_string + '\n')  # IMPORTANTE: write nao so' sobrepoe os caracteres, mas substitui a linha!


#6. Funcao que recebe um arquivo e reescreve suas linhas em ordemem ordem crescente ou decrescente
def sort_lines(filepath, sorting='asc'):
    with open(filepath, 'r') as data:
        cont = data.readlines()
    if sorting == 'asc':
        cont.sort()              # atencao para a funcao sort()
    else:
        cont.sort(reverse=True)  # atencao para a funcao sort()  com o parametro reverse       
    with open(filepath, 'w') as data1:
        for line in cont:
            data1.write(line)























