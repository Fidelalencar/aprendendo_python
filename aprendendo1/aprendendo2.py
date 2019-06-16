#####################################
#### AULA 5 : Nested Collections ####
#####################################

# Nested Collections
# Formas de conectar  collections:
# P. exemplo.: Uma lista (list) de produtos de uma loja, sendo cada produto um dict, com alguns elementos
# Eles chamam isso de "mapping types" 
products = [{'id': 'w-101',   # lembrar DESSE ESTILO de organizacao de dicts, esse e' o modelo padrao
             'name': 'arakh,
             'price': 250,
             'category': 'weapons'
          },{
             'id': 'w-90',
             'name': 'damascus',
             'price': 960,
             'category': 'weapons' 
          },{
             'id': 's-81',
             'name': 'lannister',
             'price': 310,
             'category': 'shields' }]


# EXEMPLOS DE OPERAÇÕES: 
# encontrando o objeto mais caro.
most_expensive = {}
for product in products:
    price = product['price']
    if price >= most_expensive.get('price', 0):
        most_expensive = product
most_expensive
# encontrando o weapons mais caro.
most_expensive = {}
for product in products:
    price = product['price']
    cat = product['category']
    if price >= most_expensive.get('price', 0) and cat == 'weapons': # aparentemente o 0 é o que ele retorna quando o valor n existe
        most_expensive = product
most_expensive
# encontrando uma lista de objetos mais caros de cada categoria.
weapons = []
for product in products:
    cat = product['category']
    if cat == 'weapons':
        weapons.append(product)
weapons
## 'List comprehension' é o assunto que trata esse tipo de listas de forma mais direta.
# Encontrando a soma dos preços dos produtos.
total_sum = 0
for product in products:
    total_sum += product['price']
total_sum
# Quantos objetos de cada categoria.
result = {}
for product in products:
        cat = product['category'] 
        if cat not in result:
            result[cat] = 1
        else:
            result[cat] += 1
result
    # OU
result = {}
for product in products:
        cat = product['category']
        if cat not in result:
            result[cat] = 0
        result[cat] += 1
result
    # OU
result = {}
for product in products:
        cat = product['category'] 
        result.setdefault(cat, 0)  # Estabelece um valor default, para caso nenhum valor seja atribuido ao parametro.
        result[cat] += 1
result
    # OU
result = {}
for product in products:
        cat = product['category'] 
        result[cat] = result.get(cat, 0) + 1
result

# Imagine ainda que é possível colocar listas dentro dos dicts. Isso é o 'nesting'
Personagem = {'name': 'The Hound',
             'weapons': ['w-101', 'w-390'],
             'shields': ['s-13', 's-98']
          }, {
             'name': 'The Xephis',
             'weapons': ['w-101', 'w-390', 'w-300'],
             'shields': ['s-10', 's-98'] 
             }

# interação feita dentro desses níveis é feita através de for-loops dentro de for-loops. São NESTED LOOPS


 
############
## explicou ainda break (encerra loops imediatamente) e continue (serve, na vdd, como um "pule")
## usou \n (enter para str) e \t (tab para str)
############
############ Nesse exemplo do exercício, usa-se o continue com o else (e a condição e' invertida 'com not').
# Imagine uma lista de dicts, cada um contendo nomes alternativos para um animal. Assim:
animals = [{"animal_type": "Raccoon", "street_name": "Trash Panda", "given_name": "Gizmo"},
    {"animal_type": "Snake", "street_name": "Danger Noodle", "given_name": "Spaghetti"}]
# Voce quer que o usuario possa inserir um dos parametros na funcao e ela buscar esse parametro entre os dicts da lista
# a funcao deve retornar uma lista com os dicts encontrados
# Como foi resolvido:
# se o parâmetro given_name for inserido e se ele nao constar no dict, continue, 
# caso contrario (ou seja, se constar) adicione o elemento do dict 'a nova lista criada.
# procedimento semelhante, mas mais complexo, tambem e' realizado para o outro parametro animal_type
def search_animals(list_of_animals, given_name=None, animal_type=None):
    result_animals = []
    for animal in animals:
        if given_name and given_name not in animal['given_name']:
            continue
        if animal_type and animal_type not in animal['animal_type'] and animal_type not in animal['street_name']:
            continue
        result_animals.append(animal)

    return result_animals
############

#### 'ITERTOOLS MODULE'  é como um pacote para trabalhar com interações e collections
# Essa parte da aula tem a ver com saber que existe. Pois poderão ser usadas no futuro.
# Muitas dessas funções podem ser feitas sem o pacote, mas processam mais rápido com ele.

# itertools.chain() é uma função que trata diferentes objetos com o mesmo processo. Encadeia-os
d1 = ['A', 'B', 'C']
d2 = 'DEF'
for letter in itertools.chain(d1, d2, 'XYZ'):
    print (letter)

# itertools.compress() é uma função interessante para filtrar
users = ['mario@gmail.com', 
         'rita@hotmail.com', 
         'roberta@gmail.com', 
         'antonio@gmail.com'
         ]
women = [0,1,1,0]    # é chamado de filtering array ou Musk array
men = [1,0,0,1]
print("Women:")
for user in itertools.compress(users, women):   
    print(user)

# itertools.chaim.from_iterable() serve para "achatar" (flatten)
it = [['A', 'B', 'C'], 'DEF', ('G', 'H', 'I')]
for elem in itertools.chain.from_iterable(it):
    print(elem)

# itertools.repeat() Simplesmente serve para repetir   
for e in itertools.repeat('john@example.com', 5):
    print(e)

# itertools.cycle() serve para interações infinitas 
# ... não anotei

# Esse é dos exercícios: Instala o pacote (module) random e cria uma matrix (m,n) de números aleatórios
import random  # importando module
def random_matrix(m, n):
    matriz = []
    for i in range(m):
        lista = []
        for j in range(n):
            number = random.randint(0, 100) #gerando 1 número aleatório entre 0 e 100 com o random module
            lista.append(number)
        matriz.append(lista)          
    return matriz
random_matrix(4, 5)

# também do exercício: Alinhando 2 coleções assim:
# zip(['A', 'B', 'C'], [1, 2, 3])  => result = [('A', 1),('B', 2),('C', 3),]
# zip() é a função que faz exatamente a mesma coisa 
def rmotr_zip(collection_a, collection_b):
    if len(collection_a) != len(collection_b):
        return None       # retorna None quando não da pra fazer
    result = []
    for i in range(len(collection_a)):
        result.append((collection_a[i], collection_b[i]))
    return result

# também dos exercício: retornar um dict com apenas o consumidor mais velho de cada estado
def eldest_customer_per_state(customers_dict):
    result = {}
    for estado, values in customers_dict.items():
        eldest = None
        for dict_pessoas in values:
            if eldest is None or dict_pessoas['age'] > eldest['age']:
                eldest = dict_pessoas
        result[estado] =eldest
    print(result)
    return result
    
customers_dict = {
    'UT': [{
        'name': 'Mary',
        'age': 28
    }, {
        'name': 'John',  # Eldest
        'age': 31
    }, {
        'name': 'Robert',
        'age': 16
    }],
    'NY': [{
        'name': 'Linda', # Eldest 
        'age': 71
    }, {
        'name': 'Londa',  
        'age': 70        
    }],
    'CA': [{
        'name': 'Barbara',
        'age': 15
    }, {
        'name': 'Paul',
        'age': 18
    }, {
        'name': 'Helen',  # Eldest
        'age': 29
    }]
}

eldest_customer_per_state(customers_dict)



###############################################
#### AULA 6 : Advanced function arguments  ####
###############################################

funcao_idade(nome='jose', nascimento=1983) # quando criar uma função é possível nomear os parâmetros para fins de compreensao

funcao_idade(nome='jose', nascimento=1983) # esse formato tambem serve para atribuir valores default para parametros (que se tornanm opcionais)

funcao(a,b)
funcao(b,a) # Nunca invoque uma funcao com os parametros em ordem diferente da funcao.

# Conceito: scope, global scope (linhas fora da funcao), local scope (linhas dentro de uma funcao)
# Operacoes no local scope (de uma funcao) podem acessar objetos no global scope, mas o contrario nao e' possivel
# operacoes no local scope (de uma funcao) podem acessar objetos no global scope, mas nao os altera no global scope
    # mas e' possivel levar o objeto do local para o global scope, atraves da keyword: global (dentro da funcao)
    # mas isso nunca se faz


# NESTED FUNCTIONS
# para funcoes dentro de funcoes valem as mesmas regras de scope descritas acima
    # nonlocal é outra keyword que serve para avisar 'a funcao que vc se refere ao objeto nao local


 
 # DOS EXERCÍCIOS
 # 1. Imagine um dict q contem aquisições em andamento (purchase) em um site. Assim:
purchase = {'id': 99,
        'books': [{'title': 'The Raven', 'author': 'Edgar Allan Poe', 'price': 19.99}, {
            'title': 'Ulysses','author': 'James Joyce', 'price': 23.99}, {
            'title': 'The Odyssey', 'author': 'Homer', 'price': 7.99}],
        'total': 0  } 
 # Um de seus elementos é uma key 'books' cujo valor é uma lista de livros no carrinho.
 # Essa lista é composta de dicionários, cada um com 3 elementos: autor, titulo e preco
 # Outro key do dict purchase é 'total' que pode ser a soma dos prices, se set_to_dict = True
 # ou zero, se set_to_dict = False  
 def calculate_purchase_price(purchase, set_to_dict=False):
    livros = purchase['books']
    total = 0
    for livro in livros:
        total += livro['price'] # aqui ele soma todos os values da key price.
        # Importante: Perceber que nao precisa mandar ele procurar dict por dict da lista books
        # E' como se essas keys se comportassem como se estivessem em um u'nico dict.
        if set_to_dict == True: # aqui a soma só é salva com o parametro True
            purchase['total'] = total
    return total

# 2. 



#################################
#### AULA 7 : Using MODULES  ####
#################################

# Fala em como criar ambientes virtuais e como pular de um pra outro e etc. Não entendi

# MODULES
import datetime # importando/baixando module para trabalhar com datas
from datetime import datetime # importando 1 componente de um module (no caso, o componente tem o mesmo nome)
from datetime import datetime as dt # vc pode criar um apelido para o module ou um de seus componentes 

datetime.date() # para usar o componente do pacote, e' preciso mencionar o module no inicio
# quando se importa apenas um componente, nao e' preciso indicar o module para roda-lo

# MODULE DATETIME e TIMEDELTA
import datetime, timedelta 
datetime.now() # responde data e hora de agora
datetime.utcnow() # responde data e hora universal agora

def format_date(a_date):  
    return a_date.strftime("%A, %B %d %Y")  # pega a data retorna um string: "Weekday, Month Day Year"

from datetime import date, timedelta
def counting_the_days(start_date, end_date):
    return (end_date - start_date).days    # retorna o numero de dias contidos no intervalo

# MODULE RANDOM
import random
random.randint(0,100)  # gera numero aleatorio entre 0 e 100
random.choice(x)       # escolhe um item desse x (pode ser um string, p. ex.)
random.sample(x, 5)    # pega 5 do item x


# MODULE COLLECTIONS
from collections import namedtuple # importa a collecao namedtuple, que une vantagens de tuple (ser immutable) e de dict (nomear valores) 
from collections import orderedDict # importa orderedDict. Sao dicionarios com elementos numerados.

# MODULES e PACKAGES
# um module e' um arquivo com extensao .py
import my_module
res = my_module.my_function(3,4)

# agrupar modules em pastas forma pacotes

# navegandos em pacotes dentro de pacotes
from my_package.a_module import my_function # ou seja, a pasta(pacote) my_package tem um arquivo(module) com a funcao.
# os pontos serao usados tantas vezes quantas houverem pastas dentro de pastas
# mas cuidado!!! para uma pasta virar o pacote 'e preciso criar um arquivo inicializavel dentro dela.


##############################
#### AULA 8 : Exceptions  ####
##############################

# Exceptions é quando algo da errado no codigo: (i) pode ser uma falha do programador; 
# (ii) ou um erro no ambiente, como uma limitação no processamento.

# Como lidar com exceptions?: 
# Deve-se Criar um bloco chamado "try/except clause", assim:
try:
    #bloco de codigo onde ha o erro
    2 / 0
except nomeia_o_erro:  # vc deve tipificar o erro 
    # se possivel, adicionar o codigo ou a soluçao para o caso
    print("algo deu errado")

# quando mais de um erro pode acontecer no mesmo codigo, e' posivel colocar 2 erros no mesmo bloco.
try:
    2 / 0
    l[1]
except ZeroDivisionError:
    print("Tried to divide by zero")
except IndexError:
    print("Invalid index")
# Mas o melhor e' fazer um bloco para cada erro.


# As vezes você quer 'criar' um erro, ou avisar que esta tudo indo corretamente ate' ali. 
# Nao e' um erro para o codigo, mas vc precisa que o codigo "simule" um erro.
# Lida-se assim: O if tambem pode ser usado
def search_users_by(username=None, email=None, country=None):
    if username is None and email is None and country is None:
        raise ValueError("Please provide at least 1 serch term")
    # ... rest of the code ...


# EXEMPLOS DOS EXERCICIOS:
# 1. 
def divide(a, b):
    if b == 0:   #if tambem pode ser usado
        raise ValueError()
    return a / b

# 2. O numero entra no parametro como str, vc tenta transforma-lo em int e float. Se não funcionar, o codigo da o aviso ao usuario.
def parse_number(number):
    try:
        return int(number)
    except ValueError:
        pass
    try:
        return float(number)
    except ValueError:
        pass
    raise ValueError("Invalid number")

# 3. recriar um pop() com o erro de indicar elemento que nao esta no dict
def pop(dictionary, key, default_value=None):
    try:
        val = dictionary[key]
        del dictionary[key]
        return val
    except KeyError as e:  # Usa-se o "as" para criar um objeto referente ao erro, no caso, nomeado 'e' 
        if default_value:
            return default_value
        raise e            # Mostrar ao usuario o "objeto-erro" pode ser uma boa forma de dar mais informacoes sobre o ocorrido.

# 4. criando uma calculadora de calorias ou acucar nos alimentos 
class TooSweetException(Exception):     # aqui vc cria o erro que lhe interessa
    pass
class TooManyCalsException(Exception):  # aqui vc cria o erro que lhe interessa
    pass
def recipe_calculator(ingredients):     # ingredients e' um dict com ingredientes e seu valor calorico e de acucar
    acucar = 0
    calorias = 0
    for ingred in ingredients:
        calorias += ingred['calories'] 
        acucar += ingred['sweetness']
        if acucar > 8:
            raise TooSweetException
        if calorias > 800:
            raise  TooManyCalsException 
    return (acucar, calorias)    # se os ingredientes estao ok, a funcao responde um tuple com acucar e calorias

UNIT_OF_CHOCOLATE = {'name': 'Chocolate', 'calories': 300, 'sweetness': 2}
UNIT_OF_SUGAR = {'name': 'Sugar', 'calories': 200, 'sweetness': 4}
recipe_calculator([UNIT_OF_CHOCOLATE, UNIT_OF_SUGAR, UNIT_OF_SUGAR])




