#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo:')
print('Só tem espaço? ', a.isspace()) # exemplo: "       "
print('É um número?', a.isnumeric()) # exemplo: Números
print('É alfabético?', a.isalpha()) # exemplo: letras
print('Está em letra maiúscula?', a.isupper()) # exemplo: PYTHON
print('Está em letra minúscula?', a.islower()) # exemplo: python
print('Está capitalizada?', a.istitle()) # exemplo: Python