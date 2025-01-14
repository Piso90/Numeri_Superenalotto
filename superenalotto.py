import random
import time

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
print("----LOADING_PROGRAM----")
print("")
time.sleep(1)
print("----CONNECTION_ESTABLISHED----")
print("")
time.sleep(1)
print("----STARTING----")
time.sleep(1)
print("")
nome = input("Dimmi il tuo nome per procedere: ")
print("")
print("Benvenuto",nome)
print("")
time.sleep(1)
print("<< INIZIO PROGRAMMA >>")
print("")
print("")
time.sleep(1)
print("Ciao ", nome, ", ora ti fornirò i numeri per una giocata al superenalotto:")
time.sleep(1)
conta = 0

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
    time.sleep(1)
print("")
print("Numeri quadro gioco:", numeri)
print("Jolly:", jolly)
print("Superstar:", superstar)
time.sleep(1)
conta = conta + 1
# Conta quanti quadri forniti

# Chiedi se generare altri numeri
risposta = input("Vuoi completare un altro quadro? (y/n) ")
time.sleep(1)
if risposta.lower() != "y" and risposta.lower() != "n":
    print('Premere tasto Y per confermare o tasto N per negare. Altri input errati termineranno il programma')
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
        time.sleep(1)
    print("")
    print("Numeri quadro gioco:", numeri)
    print("Jolly:", jolly)
    print("Superstar:", superstar)
    conta = conta + 1
    # Conta quanti quadri forniti
    time.sleep(1)
    risposta = input("Vuoi completare un altro quadro? (y/n) ")
    time.sleep(1)
    if risposta.lower() != "y" and risposta.lower() != "n":
        print('Premere tasto Y per confermare o tasto N per negare. Altri input errati termineranno il programma')
        risposta = input("Vuoi completare un altro quadro? (y/n) ")

print("")
print("")
print("")
if conta == 1:
    print(nome,", ti ho fornito", conta ,"quadro di gioco. Buona fortuna!")
else: print(nome,", ti ho fornito", conta ,"quadri di gioco. Buona fortuna!")
time.sleep(1)
print("")
print("")
print("<< TERMINE PROGRAMMA >>")
