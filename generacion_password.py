import random

minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "#@$%&/=?¡*"

base = minus+mayus+numeros+simbolos
longitud = 8

for _ in range(100):

    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    print(password)