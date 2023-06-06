from random import choice #Pobiera lista lub krotkę i losuje jeden losowy element

litery = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
losowanie1 = choice(litery)
losowanie2 = choice(litery)
losowanie3 = choice(litery)

wynik_loterii = losowanie1+losowanie2+losowanie3
print(f"Wygrany kupont to {wynik_loterii}")

coutn = 0

while True: 
    a = choice(litery)
    b = choice(litery)
    c = choice(litery)
    x = a+b+c
    
    if x == wynik_loterii:
        print(f"\nBrawo zgadłeś wygrywający kupon którym był {wynik_loterii} zajeło ci to {coutn} ruchów")
        print("\nSzansa na to to że trafisz za pierwszym podejściem to 0.00002782647%")
        if coutn / 35937 < 1:
            print(f"\nMiałeś szczęscię bo byłeś w {coutn/35937} najlepszych procent")
        else:
            print(f"\nMiałeś pecha bo byłeś w {coutn/35937} najgorszych procent") 
        break
    elif x != wynik_loterii:
        print(f"Podjeście numer {coutn}: {a+b+c}")
        coutn += 1
        
   
