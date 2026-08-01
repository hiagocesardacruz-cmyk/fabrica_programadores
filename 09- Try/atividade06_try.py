#Autor: Hiago Cesar

try:
   celcius =float(input("Digite seu nome: "))
   fahrenheit = (celcius*(9/5))+32
   print(f'A soma é {fahrenheit:.2f}')

except:
     print("Digite um número!")