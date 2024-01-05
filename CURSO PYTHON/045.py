from random import randint
from time import sleep
from emoji import emojize
print('-='*35)
print('E AÍ MEU NOOOOBRE!! QUE TAL UM PEDRA PAPEL TESOURA PARA ESQUENTAR NOSSO CLIMA?')
pc=randint(1,3)
player=int(input(emojize('''\nJÁ PENSEI NA MINHA JOGADA, AGORA É A SUA VEZ!! DIGITE UM OS TRÊS NÚMEROS ABAIXO!!
[1] Pedra
[2] Papel
[3] Tesoura
Qual você escolhe? ''')))
print('\nPROCESSANDO...')
sleep(2)

if  pc == 1 and player == 2:
    print(emojize('\n:memo: :collision: :collision: :moai:'))
    print('\nDROGA EU PERDI!!! É como dizem... Não importa o quão duro seja o seu coração, um dia ele será coberto por algo macio e branco. (QUE PORRA QUE TO FAZENDO KKKKK)')
elif pc == 1 and player == 3:
    print(emojize('\n:moai: :collision: :collision: :scissors:'))
    print('\nHÁ EU VENCI!! Já dizia Sócrates... Somos como pedras, vazias e duras. E as tesouras são os insetos que esmagamos no caminho.')
elif pc == 1 and player == 1:
    print(emojize('\n:moai: :collision: :collision: :moai:'))
    print('\nEMPATAMOS!! Somos como os dois ferozes gigantes de Elbaf. Não importa o quanto lutarmos, sempre chegaremos ao mesmo resultado.')
elif pc == 2 and player == 1:
    print(emojize('\n:memo: :collision: :collision: :moai:'))
    print('\nHÁ EU VENCI!!! É como dizem... Não importa o quão duro seja o seu coração, um dia ele será coberto por algo macio e branco. (QUE PORRA QUE TO FAZENDO KKKKK)')
elif pc == 2 and player == 3:
    print(emojize('\n:scissors: :collision: :collision: :memo:'))
    print('\nDROGA EU PERDI!! Bom, é oq dizem né... Não importa o quão brilhante e comfortante você seja. Sempre haverá uma lâmina fria e gelada para cortar seu coração.')
elif pc == 2 and player == 2:
    print(emojize('\n:memo: :collision: :collision: :memo:'))
    print('\nEMPATAMOS!! Somos como os dois ferozes gigantes de Elbaf. Não importa o quanto lutarmos, sempre chegaremos ao mesmo resultado.')
elif pc == 3 and player == 1:
    print(emojize('\n:moai: :collision: :collision: :scissors:'))
    print('\nDROGA EU PERDI!! Já dizia Sócrates... Somos como pedras, vazias e duras. E as tesouras são os insetos que esmagamos no caminho.')
elif pc == 3 and player == 2:
    print('\n:scissors: :collision: :collision: :memo:')
    print('\nHÁ EU VENCI!! Bom, é oq dizem né... Não importa o quão brilhante e comfortante você seja. Sempre haverá uma lâmina fria e gelada para cortar seu coração.')
elif pc == 3 and player == 3:
    print(emojize('\n:scissors: :collision: :collision: :scissors:'))
    print('\nEMPATAMOS!! Somos como os dois ferozes gigantes de Elbaf. Não importa o quanto lutarmos, sempre chegaremos ao mesmo resultado.')
else:
    print('\nDigite um dos três números seu estúpido!')
    
    
    
    
    
    