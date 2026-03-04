import random

print('Bem-vindo ao gerador de senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789'

numero = int(input('Quantidade de senhas para gerar: '))
tamanho = int(input('Digite o tamanho da(s) senha(s): '))

print('\nAqui está(ão) sua(s) senha(s): ')

for sen in range(numero):
    senha = ''
    for i in range(tamanho):
        senha += random.choice(chars)
    print(senha)