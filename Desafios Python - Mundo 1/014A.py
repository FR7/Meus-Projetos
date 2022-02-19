#Converter a temperatura de Celcius para Fanenheight

celsius = float(input("Informe a temperatura atual em Celsius: "))
fahrenheit = celsius * (9/5) + 32

print("Transformando a temperatura de {} graus Celsius em Fahrenheit; teremos: {} Graus Fahrenheit".format(celsius, fahrenheit))