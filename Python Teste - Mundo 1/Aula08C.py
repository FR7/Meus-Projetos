import math
import random

num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print("A raiz de {} é igual a {:.3f}".format(num, raiz))
print("A raiz de {} é igual a {:.3f}".format(num, math.ceil(raiz)))
print("A raiz de {} é igual a {:.3f}".format(num, math.floor(raiz)))

numrandom = random.random()
numranint = random.randint(1, 3)
print("{:.2f},  {:.2f}".format(numrandom * 10, numranint))
import emoji
print(emoji.emojize("Olá Mundo!!!!! :full_moon:", use_aliases=True))
