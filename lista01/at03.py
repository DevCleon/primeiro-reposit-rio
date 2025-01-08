num1 = int(input('entre com o primeiro numero'))
num2 = int(input('entre com o segundo numero'))

if num1 % num2 == 0 or  num2 % num1 == 0:
    print('os numeros são multiplos')
else:
    print ('os numeros não são multiplos')