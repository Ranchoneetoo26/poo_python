numero_1 = 8
numero_2 = 3

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteiro = numero_1 // numero_2
modulo = numero_1 % numero_2
exponeciacao = numero_1 ** numero_2

print('Soma:', soma) #11
print('Subtracao:', subtracao) #5
print('Multiplicacão:', multiplicacao) #24
print('Divisao:', divisao) #2.66666
print('Divisão inteira:', divisao_inteiro) #2
print('Modulo:', modulo) #2
print('Exponeciação:', exponeciacao) #512


#atribuicoes
x = 5

#atribuicao simples
print('Valor inicial de x:', x)

#atribuicao com adicao
x += 2
print('Apos x += 2:', x)

#atribuicao de subtracao
x -= 2
print('Apos x -= 2:', x)

#atribuicao com multiplicacao
x *= 2
print('Apos x *= 2:', x)

#atribuicao com divisao
x /= 2
print('Apos x /= 2:', x)

#atribuicao com modulo
x %= 2
print("Apos x %= 2:", x)

# if / else
soma = numero_1 + numero_2
if soma < 10:
    print('Soma não e maior que 10')
else:
    print('Soma é maior ou igual a 10')
"""
and == retorna true se todas as condicoes forem verdadeira caso contrario retorna false

 or ==  
"""
idade_tio_paulo = 18
idade_tia_maria = 18
if idade_tio_paulo >= 15 or idade_tia_maria >= 18:
    print('pelo menos um dos dois e maior de idade:')
else:
    print('tio paulo e maria sao menores de idade: ')
    


