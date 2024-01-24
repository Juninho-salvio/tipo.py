#Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possivel sobre ele.
p = input('Digite algo ')
print(type(p))

print('é um numerico: ', p.isnumeric())
print('é uma letra: ', p.isalpha())
print('é uma letra ou numero: ', p.isalnum())
print('é tudo letra maiuscula', p.isupper())
print('é tudo letra minuscula: ', p.islower())
print('so tem espaços: ', p.isspace())
print('esta capitalizada: ', p.istitle())
