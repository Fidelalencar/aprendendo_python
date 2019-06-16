#####################################################
#### AULAS 9 e 10 : Object Oriented Programming  ####
#####################################################

# Alan Kay foi uma dos pioneiros da ideia de OOP.
# Tem a ver com encapsular formas de interagir com o codigo sem  precisar entender exatamente como ele funciona.
# Portanto, exige uma interface claramente definida.
# O objeto e' a 'abstracao' que nos permite encapsular dados e ??comportamentos??


# Objetos sao criados a partir de "templates", chamados classes.

class BiscoitoLanche(objeto):  # phyton 2 e 3
    pass
class BiscoitoLanche:         # phyton 3
    pass

# As instancias de uma classe sao seus objetos criados. Esses objetos se tornam independentes

# Criando instancias e atribuindo (set) atributos aos objetos/instancias

BiscoitoLanche1 = BiscoitoLanche() 
BiscoitoLanche1.recheio = 'morango'
BiscoitoLanche1.massa = 'leite'

BiscoitoLanche2 = BiscoitoLanche()
BiscoitoLanche2.recheio = 'chocolate'
BiscoitoLanche2.massa = 'cafe'
BiscoitoLanche2.formato = 'redondo'


# Criando acoes (methods) para os objetos

def sabor(um_biscoito):   # Primeiro ... e' como uma funcao
    return '{} {}'.format(um_biscoito.recheio, um_biscoito.massa)
# Se vc chamar sabor(BiscoitoLanche1) => Ele retorna "morango leite"

# QUANDO VC IDENTA UMA FUNCAO EM UMA CLASSE, VC TEM UM METODO . Assim:
class BiscoitoLanche(objeto):  # phyton 2 e 3
    def sabor(um_biscoito):
        return '{} {}'.format(um_biscoito.recheio, um_biscoito.massa)

BiscoitoLanche1.sabor()  # Chamando o metodo
# A diferenca é que para chamar o 'metodo', vc comeca indicando o objeto para o qual o metodo vai rodar.
# Ou seja, o objeto 'e como um parametro, mas colocado fora dos parenteses. 

class BiscoitoLanche(objeto):  # phyton 2 e 3
    def sabor(self):   # recomenda sempre usar o termo self
        return '{} {}'.format(self.recheio, self.massa)

#######################################
###### EXPLICANDO PARA MIM MESMO ######

# A ideia e' que criar uma classe e' criar um "tipo" de objeto. 
# Quando uma classe e' criada, isso significa que sera' possivel criar varios objetos que serao considerados daquele 'tipo'.
class Country(object):  # E' convencao que Classes comecam com letra maiuscula
    pass
# Grosseiramente, esses objetos (instancias) nao precisam ter uma forma fixa, sendo definidos como tal apenas pela atribuicao inicial
usa = Country()  # Cria um objeto da classe (pre-definida acima) Countrye o nomeia 'usa'
# Nesse caso ("classes pouco definidas"), os objetos podem ser criadas pelo usuario atribuindo os atributos que ele desejar.
usa.name = 'United States of America'
usa.population = 325719178  
usa.area_in_km2 = 9833520 

# MAS HA' OUTRA FORMA "MAIS CONSISTENTE" DE CRIAR CLASSES, que e' como mais interessa:
# Nesse segundo caso, o programador ao criar uma classe, da forma fixa a ser exigida para a criacao de objetos daquela classe. 
class Car(object):
    def __init__(self, color, make, model, doors=4): # __init__ e' a convencao para metodos de inicializacao e self e' a convencao para referir-se ao novo objeto
        self.color = color  #significa: atribua o parametro cor (da funcao/metodo) ao atributo cor(do objeto a ser criado)
        self.make = make
        self.model = model
        self.doors = doors  # atributo opcional: valor padra ja' foi indicado 
# Nesse segundo caso, o usuario so' conseguirar inicializar o objeto atribuindo valores aos atributos pre-fixados.
car1 = Car(color = 'blue', make = 'Tesla', model = 'Model S')

# Por fim, ha' as definicoes de metodos, que servirao como acoes de uma dada classe
class Country(object): 
    def gdp_per_capita(self):  # Ou seja, permite que o usuario incira o comando e o objeto referente
        return float(self.total_gdp) / self.population  # e obtenha um atributo, salvo, daquele objeto

##########################################################################################
#####################  #####################  #####################  #####################
# EXEMPLOS

#1. Criar 3 methods que retornam os dados referentes ao pais(objeto)
class InvalidAreaUnitException(Exception):
    pass

class Country(object):
    def population_density(self):
        return float(self.population) / self.area_in_km2

    def gdp_per_capita(self):
        return float(self.total_gdp) / self.population

    def area(self, unit='km2'):
        if unit == 'km2':
            return self.area_in_km2
        elif unit == 'mi2':
            return self.area_in_km2 * 0.3861
        elif unit == 'acres':
            return self.area_in_km2 * 247
        elif unit == 'hectares':
            return self.area_in_km2 * 100
        else:
            raise InvalidAreaUnitException()

# vv Don't change these objects vv
usa = Country()
usa.name = 'United States of America'
usa.population = 325719178  # 325,719,178
usa.area_in_km2 = 9833520  # 9,833,520 km2
usa.total_gdp = 20199000000000  # 20.199 trillion

canada = Country()
canada.name = 'Canada'
canada.population = 35151728  # 35,151,728
canada.area_in_km2 = 9984670  # 9,984,670 km2
canada.total_gdp = 1836000000000  # 1.836 trillion
# ^^ Don't change these objects ^^



#2. 
class Car(object):
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model

car1 = Car(color = 'blue', make = 'Tesla', model = 'Model S')
car2 = Car(color = 'red', make = 'Chevy', model = "Camaro")



#3. Inicializar o objeto e criar um metodo
class Car(object):
    def __init__(self, electric):
        self.electric = electric
    
    def drive(self):
        if self.electric:
            return 'WHIRRRRRRR'
        else:
            return 'VROOOOM'



#4. Criando um programinha que permite responder dados de uma funcao de 1o grau a partir de dados de 2 pontos
# Para isso se cria 2 classes: Uma de pontos e uma de linhas. E define-se alguns metodos para esta segunda:

class Point(object):      # Define a classe pontos, que exige duas cordenadas para se criar um ponto
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):       # Define a classe linhas, que exige dois pontos para se criar uma linha
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def slope(self):        # Um metodo que retorna a inclinacao da linha definida
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        
    def y_intercept(self):  # Um metodo que retorna o intercepto da equacao de primeiro grau correspondente a linha
        m = self.slope()
        return self.p1.y - (m * self.p1.x)
    
    def formula(self):     # Um metodo que retorna a equacao de primeiro grau referente a linha definida
        tpl = 'y = {m}x + {b:g}'
        m = self.slope()
        if m == 1:
            m = ''
        return tpl.format(m=m, b=self.y_intercept())


####################################################################
#### AULA 11 : Licoes avancadas de Object Oriented Programming  ####
####################################################################

# Atributos das classes. E' possivel criar Classes com atributos proprios 

class Country(object):
    GOVERNO = ''     # Convenciona-se que atributos das classes estao em maiusculas
    TERRITORIO = ''
    MOEDA = ''


Country.GOVERNO   # retorna o valor do atributo GOVERNO da classe Country

##############
# Criando uma Classe com atributo fixo e com valor padrao, que sera' "transmitido" aos objetos que forem criados
class Cookie(object):
    DEFAULT_SCARF_COLOR = 'green'

    def __init__(self, buttons, scarf=None):
        self.buttons = buttons
        if scarf:    # scarf e' opcional, dessa forma, ele atribui o valor padrao do atributo da classe aos objetos a serem criados
            self.scarf = scarf
        else:
            self.scarf = self.DEFAULT_SCARF_COLOR 
            # Serve tb: self.scarf = Cookie.DEFAULT_SCARF_COLOR
# Esse faz a mesma coisa que o anterior: todo objeto q ser criado tera' o atributo com o valor padrao dado pela classe
class Cookie(object):
    DEFAULT_SCARF_COLOR = 'green'

    def __init__(self, buttons, scarf=DEFAULT_SCARF_COLOR):
        self.buttons = buttons
        self.scarf = scarf

# E' possivel ainda criar um atributo para a classe, cujo valor se atualiza
class Cookie(object):
    ID = 1
    def __init__(self):
        self.ident = Cookie.ID
        Cookie.ID += 1


##############

# Metodos das classes. E' possivel criar metodos no nivel das classes, 
# No entanto, esses metodos nao sao de uso tao comum. 

class Cookie(object):       # Metodos das classes são criados do mesmo jeito dos metodos dos objetos,
    @classmethod            # a diferenca e' que se usa essa convencao antes. Chama-se 'anotacao'
    def dummy_method(cls):  # e que aos inves de self, a convencao nesse caso e' cls
        return "Hello World"

# E'xistem tambe'm os 'metodos de classe estaticos', mas que podem ser substituidos pelos metodos normais. 

##############

# EXEMPLOS ODS EXERCICIOS

#1. Criar um metodo que permite criar varios objetos daquela classe
class Country(object):
    @classmethod
    def create_countries(cls, n):
        lista = []
        for _ in range(n):
            # lista += [cls(),]    # essa linha e' uma alternativa a prxm
            lista += [Country(),]
        return lista

Country.create_countries(5)  # chamando a funcao


#2. Criar a mesma coisa do exemplo anterior, mas os objetos devem ter parametros opcionais
class Cookie(object):
    DEFAULT_SCARF_COLOR = 'red'
    DEFAULT_BUTTON_COLOR = 'Blue'
    
    def __init__(self, scarf_color=DEFAULT_SCARF_COLOR, buttons_color=DEFAULT_BUTTON_COLOR):
        self.scarf_color = scarf_color
        self.buttons_color = buttons_color
        
    @classmethod
    def create_cookies(cls, n, scarf_color=DEFAULT_SCARF_COLOR, buttons_color=DEFAULT_BUTTON_COLOR):
        lista = []
        for _ in range(n):
            # lista += [cls(scarf_color, buttons_color),]    # essa linha e' uma alternativa a prxm
            lista += [Cookie(scarf_color, buttons_color),]
        return lista


############################



# 3 + 1 funcoes para trabalhar com objetos:

# primeira)
getattr(jane, 'name')  # responde o valor de um atributo de um objeto, dinamicamente -> e' o mesmo que jane.name
getattr(jane, 'name', 'no') # se o atributo nao existir, ele responde o terceiro parametro
# segunda)
hasattr(jane, 'name')  # responde T ou F se o objeto tem o atributo
# terceira)
setattr(jane, 'age', '30')  # atribui ao objeto jane um atributo 'age' com valor '30'
# quarta)
isinstance() # permite verificar se um objeto e' de uma determinada classe.
# No enatnto, em phyton, costuma-se usar hasattr() em seu lugar, 
# pois frequentemente basta checar se um objeto tem certos atributos para saber se ele e' daquela classe
# ao inve's de checar se ele e' de uma classe. 
# P. exemplo, as classes a seguir podem ser identificadas pelos atributos: Pois, 'persons' tem 'names' e 'books' tem 'titles'

class Person(object):
    def __init__(self, name):
        self.name = name

class Book(object): 
    def __init__(self, title)
        self.title = title


#####

# EXEMPLOS DOS EXERCICIOS

#1. Transformando dicts em objetos.
# Imagine uma lista de dicts em que os dicts sao filmes, seus keys sao caracterisitcas, e os valores seus conteudos.
# Transforme essa lista em uma classe, os dics em objetos, e os pares key-value em atributos-valores.

class Commercial(object): 
    def __init__(self, diction_filmes):
        for key, value in diction_filmes.items():
            setattr(self, key, value)


#2. Transformando dicts em objetos e usando uma lista para verificar se o objeto tem o conteudo da lista
# Imagine um dict cujos keys sao lugares e seus valores sao riquezas(premios) ali escondidas.
# Crie um metodo de busca em que se insere uma lista de lugares e retorna uma lista de riquezas para cada lugar que as possuam
class Location(object):
    def __init__(self, dicion_lugar_premio):
        for lugar, premio in dicion_lugar_premio.items():
            setattr(self, lugar, premio)
    
    def search(self, list_tentativ):
        recebidos = list()
        for tentativ in list_tentativ:
            if hasattr(self, tentativ):
                recebidos.append(getattr(self, tentativ))
        return recebidos

#3. 
# Imagine 3 classes de objetos, cujos valores sao considerados atributos diferentes:
# Alugueis tem valores, filmes tem precos e leites tem custos
# Crie um metodo que permita inserir dois objetos e retorne a soma de seus valores independente de como sao chamados os atributos

class Loan(object):
    def __init__(self, value):
        self.value = value

class Movie(object):
    def __init__(self, price):
        self.price = price

class Milk(object):
    def __init__(self, cost):
        self.cost = cost

def calculate(p1, p2):
    total = 0
    for product in [p1, p2]:
        for attr in ['cost', 'price', 'value']:
            if hasattr(product, attr):
                total += getattr(product, attr)
    return total    


############################



# MAGIC METHODS
# sao methods que vc nao os invoca manualmente. 
# Existe uma lista deles: https://rszalski.github.io/magicmethods/
# eles sempre comecam e terminam com dois underlines
__init__ # e' o mais conhecido 

__str__ # chama o endereco (string representation) 'human-readable' dos objetos
# funciona como o print(), mas esse retorna o endereco no formato 'machine-readable'
# a funcao referente e' str()

__repr__ # chama o endereco human-readable dos objetos (de uma forma um pouco mais tecnica que o __init__)
# mas esse serve tambem para a maquina!!!
# a funcao referente e' repr()



# Os MAGIC METHODS tem a utilidade de proporcionar interfaces mais operativas

# +
1 + 4
[1, 3, 4] + ['h', 'i']
'asd' + 'ret'

# Para levar a operacao + para o seu codigo/class, vc vai usar o method __add__


# Equality AND MAGIC METHODS
# quando se testa uma igualdade ==, o phyton esta buscando se as duas coisas tem o mesmo endereco na memoria
# o que o phyton esta fazendo e': 
A.__eq__B (self, ...): # dentro de uma classe

__eq__ # e' o metodo para criar igualdade



# EXEMPLOS DOS EXERCICIOS

#1. Crie uma representacao computacional de cavalos cujos objetos tem nome e raca
# Seus metodos basicos sao: criar instancia, e checar seu endereco com str() e repr() 

class Horse(object):

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed  
        
    def __str__(self):
        return "{} the {}".format(name=self.name, breed=self.breed)
        
    def __repr__(self):
        return "Horse: {}, {}".format(name=self.name, breed=self.breed)


#2. 

class Distance(object):
    METER_CONVERSIONS = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.344
    }

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def convert_to_meters(self):
        return self.value * self.METER_CONVERSIONS[self.unit]

    def __str__(self):
        return "{}{}".format(self.value, self.unit)

    def __repr__(self):
        return "Distance: {}{}".format(self.value, self.unit)

    def __eq__(self, other):
        if self.convert_to_meters() == other.convert_to_meters():
            return True
        return False

    def __ne__(self, other):
        if self.convert_to_meters() != other.convert_to_meters():
            return True
        return False

    def __lt__(self, other):
        if self.convert_to_meters() < other.convert_to_meters():
            return True
        return False

    def __le__(self, other):
        if self.convert_to_meters() <= other.convert_to_meters():
            return True
        return False

    def __gt__(self, other):
        if self.convert_to_meters() > other.convert_to_meters():
            return True
        return False

    def __ge__(self, other):
        if self.convert_to_meters() >= other.convert_to_meters():
            return True
        return False



####################################################################
#### AULA 12 : Inheritance   #######################################
####################################################################

# Criando hierarquias de classes (heranca simples)
class Veiculo(object):
    pass

class Carro(Veiculo):
    pass

class Aviao(Veiculo):
    pass

a = Aviao() # criando um objeto a -> ele e' um Aviao, mas tambem e' um Veiculo

isinstance(a, Aviao)   # True
isinstance(a, Veiculo) # True
# Nessa mesma logica, uma classe inferior na hierarquia herda atributos e methods das classes superiores.
# Pelo que entendi, herda e' uma boa palavra pq o method/atributo 'fica disponivel' ao objeto criado na classe inferior


# POLYMORPHISM e' o conceito que se refere ao fato de os objetos poderem ser formados por methodos e atributos
# de muitos niveis hierarquicos

# SUPER FUNCOES servem justamente para que um objeto acesse um methodo de uma classe superior (super-classe)
# e opere conjuntamente com um methodo da propria classe (sub-classe)



# EXEMPLOS DOS EXERCICIOS

#1. HERANCA COM POLIMORFISMO: Imagine uma classe Animal com subclasses. E um metodo que esta na classe superior 
# Mas pode ser chamada e roda com os dados das subclasses.
class Animal(object):
    def talk(self):   # o metodo esta em cima, mas busca informacoes (atributos) em baixo
        return "{} says {}".format(self.name, self.sound)

class Cow(Animal):
    sound = 'moo'
    def __init__(self, name):
        self.name = name
    
class Sheep(Animal):
    sound = 'baaaaa'
    def __init__(self, name):
        self.name = name   
        
class Fox(Animal):
    sound = 'Ring-ding-ding-ding-dingeringeding'    
    def __init__(self, name):
        self.name = name


#2. HERANCA COM POLIMORFISMO : "OVERRIDING" (spbreposicao de metodo)
class Vehicle(object):
    def move(self):    # o metodo comeca em cima, mas busca informacoes (continuacao do metodo) em baixo
        my_sound = self.sound()
        print("I'm moving, and I sound: {}".format(my_sound))

class Car(Vehicle):
    def sound(self):
        return "Brooooom"
    
class Airplane(Vehicle):
    def sound(self):
        return "Nnneeaoowww"


#3. HERANCA COM POLIMORFISMO: 
class Computer():
    def _init_(self, computer, ram, ssd):  # o metodo comeca em cima e continua em baixo
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):
    def _init_(self, computer, ram, ssd, model):
        super()._init_(computer, ram, ssd) # recupera parametros ja passados super().
        self.model = model

lenovo = Laptop('lenovo', 2, 512, 'l420')
print('This computer is:', lenovo.computer)
print('This computer has ram of', lenovo.ram)
print('This computer has ssd of', lenovo.ssd)
print('This computer has this model:', lenovo.model)


#4. HERANCA COM POLIMORFISMO: (POLIMORFISMO + SUPER() )
class Employee:
    BONUS_PER_YEAR = 1_000
    def __init__(self, name, base_salary, years):
        self.name = name
        self.base_salary = base_salary
        self.years = years  
    def salary(self):
        return self.base_salary + (self.years * self.BONUS_PER_YEAR)

class Developer(Employee):
    pass

class Manager(Employee):
    BONUS_PER_YEAR = 1_500  # alem do bonus anual maior
    def salary(self):
        return super().salary() * 1.1  # um acrescimo de 10% sobre tudo

#4. Resultado: 
mary = Developer('Mary Smith', 70_000, 6)
mary.salary() # ganha 76000
jane = Manager('Jane Sanchez', 70_000, 6)
jane.salary() # ganha 86900  (3 mil do bonus + 7900 dos 10%)


#5. 
class Payroll(object):
    def __init__(self, company, employee_list=[]): #pode receber uma lista vazia
        self.company=company
        if employee_list == []:  # nem sei se precisa
            self.employee_list=employee_list
    def add_employee(self, emp):
        self.employee_list.append(emp)   
    def get_annual_payroll_cost(self):
        total = 0        
        for employee in self.employee_list:
            total += employee.calculate_annual_income()
        return total
    
class Employee(object):
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return "{} makes {} annually".format(self.name, self.calculate_annual_income())

class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super(SalariedEmployee, self).__init__(name) # Nao ficou claro essa sintaxe do super()
        self.salary=salary   
    def calculate_annual_income(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage):
        super(HourlyEmployee, self).__init__(name) # Nao ficou claro essa sintaxe do super()
        self.hourly_wage=hourly_wage  
    def calculate_annual_income(self):
        return self.hourly_wage * 40 * 52

