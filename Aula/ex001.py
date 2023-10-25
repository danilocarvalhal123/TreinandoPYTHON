# Tipos primitivos
#Analisando o fluxo dos caracteres

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro número:'))
s = n1 + n2
print('A soma entre {} e {} somam {}'.format(n1, n2, s))
#resultado: 4 + 5 = 9

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro número:'))
s = n1 + n2
print('A soma entre {} e {} somam {}'.format(n1, n2, s))
#resultado: 4 + 5 = 9.0

n1 = str(input('Digite um valor: '))
n2 = str(input('Digite outro número:'))
s = n1 + n2
print('A soma entre {} e {} somam {}'.format(n1, n2, s))
#resultado: 4 + 5 = 45

n = input('Digite algo')
print(n.isnumeric())
#Este método irá dizer se é possível converter esse valor recebido em um número 

n = input('Digite algo')
print(n.isalpha())
#Este método irá dizer se é possível converter esse valor recebido em uma letra
