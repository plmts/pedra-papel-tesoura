import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

opcoesString = [rock, paper, scissors]
opcoesLen = len(opcoesString)
opcoes = opcoesLen - 1
pc = random.randint(0, opcoes)

escolha = int(input("Qual a sua escolha? Digite 0 para pedra, 1 para papel e 2 para tesoura. "))

if escolha == 0:
    print("Você escolheu " + rock)
elif escolha == 1:
    print("Você escolheu " + paper)
elif escolha == 2:
    print("Você escolheu " + scissors)


if pc == 0:
    print("O computador escolheu " + rock)
elif pc == 1:
    print("O computador escolheu" + paper)
elif pc == 2:
    print("O computador escolheu " + scissors)



if escolha == pc:
    print("Deu empate!")
elif escolha == 0 and pc == 1:
    print("Papel ganha de pedra. Você perdeu!")
elif escolha == 1 and pc == 0:
    print("Papel ganha de pedra. Você ganhou!")
elif escolha == 0 and pc == 2:
    print("Pedra ganha de tesoura. Você ganhou!")
elif escolha == 2 and pc == 0:
    print("Pedra ganha de tesoura. Você perdeu!")
elif escolha == 1 and pc == 2:
    print("Tesoura ganha de papel. Você perdeu!")
elif escolha == 2 and pc == 1:
    print("Tesoura ganha de papel. Você ganhou!")
else:
    print("Tente novamente")