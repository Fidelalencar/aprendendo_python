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