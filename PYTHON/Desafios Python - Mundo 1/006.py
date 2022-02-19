#Crie um algoritimo que leia um número e mostre seu dobro; seu triplo e raiz quadrada.

n = float(input('Digite um valor: '))

d = n * 2
t = n * 3
rq = pow(n,(1/2))

print('O dobro de {} é: {}.\nO tripo de {} é: {}.\nE a raiz quadrada de {} é {:.2f}.'.format(n,d,n,t,n,rq))