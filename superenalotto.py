import random

def generate_numbers():
    numeri = random.sample(range(1, 91), 88)
    numeri.sort()
    return numeri

def generate_superstar():
    superstar = random.randint(1, 90)
    return superstar

def generate_jolly():
    jolly = random.randint(1, 90)
    return jolly

# Genera i 6 numeri del quadro gioco
numeri = generate_numbers()
superstar = generate_superstar()
jolly = generate_jolly()
for contsup in numeri:
    while superstar == contsup:
        #ricalcola superstar perchè uguale a uno dei 6 numeri
        superstar = generate_superstar()
for contjo in numeri:
    while jolly == contjo:
        #ricalcola jolly perchè uguale a uno dei 6 numeri
        jolly = generate_jolly()
if jolly == superstar:
    for contjo in numeri:
            while jolly == contjo:
                #jolly e superstar coincidono, ricalcola
                jolly = generate_jolly()
print("")
print("Numeri quadro gioco:", numeri)
print("Jolly:", jolly)
print("Superstar:", superstar)

# Chiedi se generare altri numeri
risposta = input("Vuoi giocare ancora? (y/n) ")
while risposta.lower() == "y":
    numeri = generate_numbers()
    superstar = generate_superstar()
    jolly = generate_jolly()
    for contsup in numeri:
        while superstar == contsup:
            #ricalcola superstar perchè uguale a uno dei 6 numeri
            superstar = generate_superstar()
    for contjo in numeri:
        while jolly == contjo:
            #ricalcola jolly perchè uguale a uno dei 6 numeri
            jolly = generate_jolly()
    if jolly == superstar:
        for contjo in numeri:
            while jolly == contjo:
                #jolly e superstar coincidono, ricalcola
                jolly = generate_jolly()
    print("")
    print("Numeri quadro gioco:", numeri)
    print("Jolly:", jolly)
    print("Superstar:", superstar)
    risposta = input("Vuoi giocare ancora? (y/n) ")

print("")
print("Buona fortuna!")
print("  ")