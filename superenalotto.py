import random

def generate_numbers():
    numeri = random.sample(range(1, 91), 6)
    numeri.sort()
    return numeri

def generate_superstar():
    superstar = random.randint(1, 90)
    return superstar

def generate_jolly():
    jolly = random.randint(1, 90)
    return jolly

print("")
print("<< INIZIO PROGRAMMA >>")
print("")
print("")
print("Ciao, ora ti fornisco i numeri per una giocata al superenalotto:")

# Genera i 6 numeri del quadro gioco
numeri = generate_numbers()
superstar = generate_superstar()
jolly = generate_jolly()
while superstar in numeri:
    #ricalcola superstar perchè uguale a uno dei 6 numeri
    superstar = generate_superstar()
while jolly in numeri:
    #ricalcola jolly perchè uguale a uno dei 6 numeri
    jolly = generate_jolly()
tutti = numeri.copy()
tutti.append(jolly)
#tutti è numeri + jolly su cui verificare superstar
while superstar in tutti:
    #superstar già presente, ricalcola
    superstar = generate_superstar()
print("")
print("Numeri quadro gioco:", numeri)
print("Jolly:", jolly)
print("Superstar:", superstar)

# Chiedi se generare altri numeri
risposta = input("Vuoi completare un altro quadro? (y/n) ")
while risposta.lower() == "y":
    numeri = generate_numbers()
    superstar = generate_superstar()
    jolly = generate_jolly()
    while superstar in numeri:
        #ricalcola superstar perchè uguale a uno dei 6 numeri
        superstar = generate_superstar()
    while jolly in numeri:
        #ricalcola jolly perchè uguale a uno dei 6 numeri
        jolly = generate_jolly()
    tutti = numeri.copy()
    tutti.append(jolly)
    #tutti è numeri + jolly su cui verificare superstar
    while superstar in tutti:
        #superstar è già presente, ricalcola
        superstar = generate_superstar()
    print("")
    print("Numeri quadro gioco:", numeri)
    print("Jolly:", jolly)
    print("Superstar:", superstar)
    risposta = input("Vuoi completare un altro quadro? (y/n) ")

print("")
print("Buona fortuna!")
print("")
print("")
print("<< FINE PROGRAMMA >>")
