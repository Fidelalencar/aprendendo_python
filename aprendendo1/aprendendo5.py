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