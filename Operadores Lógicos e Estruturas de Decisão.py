# Comparações : == Igual
#              != Diferente
#               > Maior
#               < Menor
#               >= Maior Igual
#               <= Menor Igual
#               and significa E
#               or significa OU
#               not significa NÃO
# Utilizando um comparador atravez do IF


var_verdade = True  # Definindo variáveis com valores BOOLEANOS
var_falso = False

a = 50
b = 20


# para comandos específicos utiliza-se Dois pontos no fim dos mesmos.
if var_verdade == True:

    print('Var_verdade é verdadeiro')


if (a > b):
    print(a, 'é maior que', b)

else:
    print(a, 'não é maior que', b)


if ((a > b) and ('João' > 'Maria')):

    print(a, 'é maior que ', b)


###################################################################################################################################


print('Opções Disponíveis:\n 1 = Escreve Guilherme\n 2 = Escreve João\n 3 = Escreve Matheus ')
opção = input(' Escolha uma opção abaixo:')

if opção == '1':
    print('Guilherme')
elif opção == '2':
    print('João')
elif opção == '2':
    print('Matheus')

###################################################################################################################################
####################### FIM AULA ###################################################################################################################################


