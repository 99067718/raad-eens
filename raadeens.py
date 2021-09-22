from math import trunc
import random
Rounds = 0
Guesses = 0
correctAnswer = False
score = 0
print("""
Hallo, we spelen vandaag het spel, 'Raad het getal'.
In dit spel moet je een getal tussen de 1 en 1000 raden
""")
while Rounds <= 20:
    number = random.randint(1, 1000)
    correctAnswer = False
    Guesses = 0
    r = range(int(number - 20), int(number + 20))
    print("raad het nummer!!!")
    while Guesses != 10:
        print("Aantal keer gegokt: ",Guesses)
        gegoktnummer = int(input("Nummer: "))
        Guesses = Guesses + 1
        if gegoktnummer > number:
            print("Het getal is lager.")
        if gegoktnummer < number:
            print("Het getal is hoger.")
        print(number)

        Close = gegoktnummer in r
        if Close == True: #checkt of je getal in de buurt ligt#
            print("Je bent heel dicht in de buurt.")

        if gegoktnummer == number:
            print("Goed gedaan, je hebt het juiste antwoord!!!")
            score = score + 1
            print("je hebt nu",score, "punt(en)")
            correctAnswer = True
            break
        else:
            print("")
    if correctAnswer == False:
        print("The correct answer was:", number)
    Rounds = Rounds + 1
    if Rounds != 20:
        print("Wilt U verder spelen???")
        doesContinue = input("typ 'quit' om te stoppen, vul niks in om door te gaan: ").upper()
    else:
        print("Bedankt voor het spelen.")
    if doesContinue == "QUIT":
        break

print("Uw eindscore is:", score, "punt(en)")


