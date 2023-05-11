import random

options = ('piedra','papel','tijera')

user_option = input('piedra, papel o tijera => ')
user_option = user_option.lower()

if not user_option in options:
    print('esa opcion es invalida')

computer_option = random.choice(options)

print('User option => ', user_option)
print('}computer option => ', computer_option)

if user_option == computer_option:
    print('Empate')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra gana a tijera')
        print('Usuario le gano a la maquina')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a la tijera')
        print('Usuario le gano a la maquina')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('Tijera le gana al papel')
        print('Usuario le gano a la maquina')
else:
    print('Gano maquina')
