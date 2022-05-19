import os
import random 

nome = input('Digite seu nome: ')
print(f'Olá seja bem-vindo {nome} ! Vamos começar a jogar?')
input('\nPresione enter para começar')
os.system('cls')

lista_de_palavras = ['visitante', 'banana', 'sucesso', 'terminal']
palavra_selecionada = random.choice (lista_de_palavras).upper()
tamanho_palavra = len(palavra_selecionada)
palavra_codificada = ['_']*tamanho_palavra
jogo_em_curso = True
quantidade_de_erros = 0

while '_' in palavra_codificada and quantidade_de_erros <= 6:
    print(f'\nSua palavra tem {tamanho_palavra} letras')
    print(f'Erros: {quantidade_de_erros} de 6')
    for letra in palavra_codificada:
        print(letra , end = ' ')
    print()

    letra_escolhida = input('Digite uma letra: ').upper()
    acertou = False
    for i in range(len(palavra_selecionada)):
        if letra_escolhida == palavra_selecionada[i]:
            palavra_codificada [i] = letra_escolhida
            acertou = True

    if acertou == True:
        print('Parabens! Acertou!')
    else:
        quantidade_de_erros = quantidade_de_erros + 1 
        print('Errou, essa letra não existe na palavra')

if quantidade_de_erros == 6:
    print('Você perdeu')
else: print('Parabens! Você ganhou!')

print(f'A palavra era {palavra_selecionada}')

