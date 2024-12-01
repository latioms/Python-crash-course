from random  import randint, choice

print("|================================================|")
print("|    Bienvenue dans le prgramme du juste Prix    |")
print("|================================================|")

print("|  vous avez ete selectionne pour participer au  |")
print("|_________________JUSTE PRIX_____________________|")

print("Demmarons : ")

possible_start_list = [25,50,75,100,150,200,300]

start = choice(possible_start_list)

end = start + 100

justePrix = randint(start, end)

print(" LE JUSTE PRIX SE TOUVE ENTRE ", start, "& ", end)

nbre = 0
while True:
    nbre = int(input("Entrer votre proposition..."))

    if nbre == justePrix:
        print("Vous avez trouvez le juste prix... felicitaions !!!!")
        break
    elif nbre > justePrix:
        print("C'est moins (-) ")
    else:
        print("C'est plus (+) !")

        