################################################ GAME ACERTE A PALAVRA ################################################
secreto = 'perfume'
digitadas = []
chances = 3


print('Você tem 3 chances de acerta a palavra correta.\n')


print('#' * 60)
while True:
    
    if chances <=0:
        print('Voce Perdeu!!!')
    letra = input('Digite uma letra: ')
    print()
    
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)
    
    
    if letra in secreto:
        print(f'Uhuuuuu, a letra "{letra}" existe na palavra secretra.\n')
        
    else:
        print(f'Afffzzzz: a letra "{letra}" NÃO EXISTE na palavra secretra.\n')
        
        digitadas.pop()
        
    
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    
    if secreto_temp == secreto:
        print(f'Parabéns, VOCÊ GANHOU O JOGO!!! A palavra era {secreto_temp}.\n')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}\n')
    
    
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.\n')
    
    print('#' * 60)
    
    if chances == 0:
        print('Você PERDEU, Acabou suas chances. :(')
        break