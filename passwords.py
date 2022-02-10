#!/usr/bin/env python

# Generador de contraseñas seguras by akil3s

import string
import random

def contra(p):
    caracteres = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    password = []

    for culo in range(p):
        teta = random.choice(caracteres)
        password.append(teta)

    res ="".join(password)
    return res

p = int(input("Dime la longitud de la password: "))
cola = contra(p)

try:
    print(cola)
    
except:
    print("Que me digas la longitud de la password!")
