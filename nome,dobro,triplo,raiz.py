nome = input('Qual o seu nome?')
print ('Prazer em te conhecer {:^}!'.format(nome))
n = int(input('Digite um número:'))
print ('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1), (n+1)))
n = int(input('Digite um número:'))
d = n*2
t = n*3
r = n**(1/2)
print ('O dobro de {} vale {}.'.format (n, d))
print ('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {}.'.format(n, t, n, r))
n = int(input('Digite um número:'))
print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, (n**(1/2))))









