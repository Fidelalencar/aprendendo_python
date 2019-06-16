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




#########################################################
#### AULA 15 : HTTP ##########
#########################################################

# Client-serever architecture
# Protocolo http (buscar https status codes, na wikipedia)
# Exemplos de Status-Codes: 2xx sao respostas de sucessos, 4xx sao erros de cliente, 404 e' not found, 5xx erros de servidor, etc..
# Body e' a parte do conteudo da comunicacao entre usuario e servidor 
# http headers - E' otra parte da informacao dessa comunicacao. Refere-se a informacoes ...
# Headers se estruturam como dict. 
# Estudar http


# Metodos de comunicacao do protocolo http - metodos do usua'rio
import requests  # busca

get    # pedido (ao servidor) para acessar informacao 
post   # pedido (ao servidor) para entregar uma informacao
delete
put  # entrega uma informacao (como post), mas atualizando uma ja existente ou enviada





####################################################
#### AULA 16 : Intro to Databases ##################
####################################################

## Intro c
# Database Engine/Server - Um programa que organiza os dados (MySQL, SQL Server, PosrgreSQL)
# SQlite e' um engine um pouco diferente - e e' o que usamos no curso. E' mais proxima de uma livraria
# ORACLE e' um engine pago. 
# Paradigma Relational (paradigma não-SQL = não-relacional)
# primary key / foreign key

# SQL - Structured Query Language. 'E uma linguagem de manipulacao de bases de dados.
# Ela e' teoricamente dividida em duas partes:
# ddl - é a parte da SQL que manipula a estrutura: cria tabelas, esquemas, bases, etc. 
# dml - é a parte da SQL que manipula os dados: como ler dados, retirar e adicionar dados, etc. 



## Methodos de Python para rodar SQL

#1 Importando e criando o banco de dados no local
import sqlite3
db = sqlite3.connect('example.db')  # aqui aconteceria a conexao com o server de dados SQL
cursor = db.execute('SELECT * FROM country;')  # cria um objeto (cursor) com os dados selecionados
cursor = db.execute('SELECT id, title FROM book;')  # selecionando o q vai ser importado (ou consultado, nao sei bem)
cursor = db.execute('SELECT id idx, title book_title FROM book;') # vc pode atribuir apelidos novos para as colunas assim
# 'SELECT * FROM country;' -> E' SQL. -> Significa, pegar todas as linhas e colunas da tabela country
# 'SELECT id, name FROM country;' -> Significa, pegar as colunas id e name da tabela country
# 'SELECT id idx, title book_title FROM book;' -> Significa, pegue id as idx e title as book_title (da tabela book)
cursor = db.execute('SELECT * FROM author WHERE country_id = 1') # vc pode add um filtro para a selecao
cursor = db.execute('SELECT * FROM author WHERE country_id = 1 AND xxx = 4') # ou mais de 1


#2 Selecionando partes dos dados
cursor.fetchone()  # retorna o prxm elemento (linha) do objeto cursor
cursor.fetchmany(size=3) # retorna varios elementos (linhas) do objeto cursor
cursor.fetchall()    # retorna todos os elementos. Voce pode ter um problema acessando todo o dado de uma vez


#3 Pedindo para imprimir os dados:
# imprimindo poucos dados
cursor = db.execute('SELECT id, title FROM book;')  # selecionando o q vai ser importado (ou consultado, nao sei bem)
row = cursor.fetchone() 
row # imprime a posicao na memoria
row.keys() # imprime os nomes das colunas  # no caso, ['id', 'title'] pois foram as unicas celecionadas acima
row['title'] # imprime o prxm title (o title da prxm linha)

# interagindo para imprimir muitos dados
cursor = db.execute('SELECT * FROM book;')
for row in cursor:
    id = row[0]  # identificando as colunas pelo index # Tb e' possivel identificar pelo header ou alias do header
    title = row[2]
    print("{} - {}".format(id, title)) # Imprimindo como o .fetchall(), so' que mais bonitinho
# ou
cursor = db.execute('SELECT id idx, title book_title FROM book;') # atribuindo apelidos novos para as colunas 
for row in cursor:
    id = row['idx']  # Tb e' possivel identificar pelo nome da coluna ou seu alias
    title = row['book_title']
    print("{} - {}".format(id, title)) # Imprimindo como o .fetchall(), so' que mais bonitinho


#4 Importando com PARAMETROS DINAMICOS (mas apenas do filtro, nao sei como faz para atributo)
params = [country_id]
cursor = db.execute('SELECT * FROM author WHERE country_id = ?', params) # perceber q essa sintaxe so serve para filtro
cursor.fetchall()

# em SQL existe formas de manipular as possibilidades de valores a serem filtrados
# usa-se a funcao LIKE para esas manipulacoes
params = ['The%', 1]  # % significa q se desconhece o numero de caracteres e quais sao eles
# params = ['The_____', 1] # _ (underline) -> significaq para cada underline, ha' um caracter desconhecido
cursor = db.execute('SELECT * FROM book WHERE title LIKE ? AND author_id = ?', params)
cursor.fetchall()

# usando um dict para manipular os filtros
params = {'title': 'The%', 'author': 1} # E' possivel criar um dict para facilitar a manipulacao
cursor = db.execute('SELECT * FROM book WHERE title LIKE :title AND author_id = :author', params)
cursor.fetchall()

# tambem e' possivel manipular utilizando  a funcao .format -> ver exemplo de exercicio 3.


#5 #######################################################################################
################### O banco 'example.db', usado acima, foi criado assim: #################
import sqlite3
db = sqlite3.connect('example.db')

# DDL: Create the Database Structure
db.executescript("""
drop table if exists country;
create table country (
  id integer primary key autoincrement,
  name text not null
);
drop table if exists author;
create table author (
  id integer primary key autoincrement,
  country_id integer,
  name text not null
);
drop table if exists book;
create table book (
  id integer primary key autoincrement,
  author_id integer,
  title text not null,
  isbn text
);
""")

# DML: Insert Countries
db.executescript("""
INSERT INTO country (id, name) VALUES (1, 'United Kingdom');
INSERT INTO country (id, name) VALUES (2, 'USA');
INSERT INTO country (id, name) VALUES (3, 'Republic of Ireland');
""")

# DML: Insert Authors
db.executescript("""
INSERT INTO author (id, country_id, name) VALUES (1, 2, 'Mark Twain');
INSERT INTO author (id, country_id, name) VALUES (2, 3, 'Oscar Wilde');
INSERT INTO author (id, country_id, name) VALUES (3, 1, 'George Orwell');
""")

# DML: Insert Books
db.executescript("""
INSERT INTO book (id, author_id, title, isbn) VALUES (1, 3, '1984', 'XYZ-1');
INSERT INTO book (id, author_id, title, isbn) VALUES (2, 2, 'The Happy Prince', 'XYZ-2');
INSERT INTO book (id, author_id, title, isbn) VALUES (3, 2, 'The Picture of Dorian Gray', 'XYZ-3');
INSERT INTO book (id, author_id, title, isbn) VALUES (4, 1, 'The Adventures of Tom Sawyer', 'XYZ-4');
INSERT INTO book (id, author_id, title, isbn) VALUES (5, 1, 'The Adventures of Huckleberry Finn', 'XYZ-5');
INSERT INTO book (id, author_id, title, isbn) VALUES (6, 2, 'The Canterville Ghost', 'XYZ-6');
INSERT INTO book (id, author_id, title, isbn) VALUES (7, 3, 'Animal Farm', 'XYZ-7');
""")
###################################################################################################
###################################################################################################


# EXEMPLOS DE EXERCIOCIOS

#1. Funcao que importa e imprime a base marvel
import sqlite3

# Database setup: Please don't change this
db = sqlite3.connect("file::memory:?cache=shared")
db.executescript("""
drop table if exists marvel;
create table marvel (
  id integer primary key autoincrement,
  title text not null,
  director text not null,
  tomatoes integer,
  metacritic integer
);

-- marvel
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (1, 'Iron Man', 'Jon Favreau', 94, 79);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (2, 'The Incredible Hulk', 'Louis Leterrier', 67, 61);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (3, 'Iron Man 2', 'Jon Favreau', 73, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (4, 'Thor', 'Kenneth Branagh', 77, 57);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (5, 'Captain America: The First Avenger', 'Joe Johnston', 80, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (6, 'Marvels The Avengers', 'Joss Whedon', 92, 69);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (7, 'Iron Man 3', 'Shane Black', 80, 62);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (8, 'Thor: The Dark World', 'Alan Taylor', 66, 54);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (9, 'Captain America: The Winter Soldier', 'Anthony and Joe Russo', 89, 70);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (10, 'Guardians of the Galaxy', 'James Gunn', 91, 76);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (11, 'Avengers: Age of Ultron', 'Joss Whedon', 75, 66);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (12, 'Ant-Man', 'Peyton Reed', 82, 64);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (13, 'Captain America: Civil War', 'Anthony and Joe Russo', 91, 75);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (14, 'Doctor Strange', 'Scott Derrickson', 89, 72);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (15, 'Guardians of the Galaxy Vol. 2', 'James Gunn', 83, 67);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (16, 'Spider-Man: Homecoming', 'Jon Watts', 92, 73);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (17, 'Thor: Ragnarok', 'Taika Waititi', 92, 74);
INSERT INTO marvel (id, title, director, tomatoes, metacritic) VALUES (18, 'Black Panther', 'Ryan Coogler', 97, 88);
""")
# Finish Database Setup

def get_all_movies(db_connection):
    cursor = db_connection.execute('SELECT * FROM  marvel;')
    return cursor.fetchall()


#2. limitando o numero de dados improtados
def get_movies_and_directors(db_connection, limit=5):
    cursor = db_connection.execute('SELECT title, director FROM  marvel;')
    return cursor.fetchmany(limit)


#3. funcao que ordena o filme por uma das ratings de filmes e em ordem descendente ou ascendente
def get_best_and_worst_movies(db_connection, rating_type, order_dir, limit=5):
    query = ('SELECT title, {rating_type} FROM marvel ORDER BY '
             '{rating_type} {direction} LIMIT :limit').format(
                rating_type=rating_type, direction=order_dir)

    cursor = db_connection.execute(query, {
      'limit': limit })
    return cursor.fetchall()















