

# Em Python, não há a necessidade de declarar o tipo de variável. Portanto basta apenas declarar o valor da mesma
# o proprio compilador irá gravar.
#########################################################################################################################################################
# declaração de variáveis

from typing import NoReturn


nome = 'Math'  # Variavel nome, com valor: Math
idade = 22
altura = 1.81

#########################################################################################################################################################

# Print:

# Comando Print, para mostrar ao usuário alguma string ou caracter inserido na mesma
print('Hello World!')
# comando para mostrar ao usuário o tipo da variável nome. Muito útil para debugar programa a
print(type(nome))
# a procura de erros...

# Esse exemplo é para a inserção de diversas variáveis dentro de um texto
print(nome, 'tem', idade, 'anos e', altura, '.')
# e mixagem de texto tb. Utilizamos Vírgula.

# Outro exemplo de inseção de variáveis + texto utilizando + ao invés de virgula
# print(nome +'tem'+ idade +'anos e' + altura +'.' ) #Para imprimir isso, deve-se utilizar uma função de
# conversão de variável, de INT para String
# str(idade)

# Aqui é um exemplo de utilização de diversas variaveis
print(nome + ' tem ' + str(idade)+' anos e ' + str(altura)+' . ')
# numa mesma linha utilizando o '+', porém se-faz necessário
# a conversão de INT/FLOAT para string

frase = nome, 'tem', str(idade), 'anos e', altura, ' . '
#########################################################################################################################################################
# Input
# Para pedir a entrada de dados, utiliza-se o comando input da seguinte maneira:

# declaramos o nome um como uma entrada de dados. sera executada antes
nome1 = input('Escreva seu nome por favor: ')
idade1 = input('Escreva sua idade por favor: ')
altura1 = input('Escreva sua altura por favor: ')
print(nome1, ' tem:', idade1, ' anos e:', altura1, 'de altura.')

#########################################################################################################################################################

# Calculadora

numero1 = input('Insira o primeiro numero: ')
numero2 = input('Insira o segundo numero: ')
resultado = (numero1+numero2)

print(resultado)
#########################################################################################################################################################
