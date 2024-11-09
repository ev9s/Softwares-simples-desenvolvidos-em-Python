numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite seu segundo valor: '))
print('Os números informados foram: "{}" e "{}"' .format(numero1, numero2))
print('A soma dessa conta é: {}\n'  'A subtração desse conta é: {}\n' 'A multiplicação dessa conta é: {} \n' 'A divisão dessa conta é: {:.2f} \n' 'A divisão inteira é: {}\n' 'O resto da divisão dessa conta é: {}' .format(numero1+numero2, numero1-numero2, numero1*numero2, numero1/numero2, numero1//numero2, numero1%numero2))