# # repète et pepete
# reponse = input("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste? ")
# while reponse != "tu es lourd":
#     if reponse == "repete":
#         reponse = input("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste? ")
#     else:
#         reponse = input("Mais non tu comprends pas, si repete et pepete sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste? ")
    


# # repète et pepete with a break
# reponse = "repete"
# while reponse:
#     if reponse == "repete":
#         reponse = input("Si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste? ")
#     elif reponse == "tu es lourd":
#         break
#     else:
#         reponse = input("Mais non tu comprends pas, si repete et pepete  sont dans un bateau, pepete tombe à l'eau, qu'est ce qui reste? ")


# Sum of numbers

# def isNumber(str):
#     if str.count("-") > 1:
#         return False
#     if str.count(".") > 1:
#         return False
#     result = str.strip(". -")
#     return result.isnumeric()

# a = input("a= ? ")
# while not isNumber(a):
#     a = input("Please enter a number for a ")

# b = input("b = ?")
# while not isNumber(b):
#     b = input("Please enter a number for b ")

# print(float(a) + float(b))


courses = []
while True:
    choice = input("Sélectionnez une option:\n1: Ajoutez un élément à la liste\n2: Retirer un élément de la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter\n")
    if choice == "1":
        to_add = input("Qu'est-ce qu'on ajoute à la lise?")
        courses.append(to_add)
    if choice == "2":
        courses.remove(input("Quel élément retire-t-on?"))
    if choice == "3":
        print(courses,"\n")
    if choice == "4":
        courses = []
    if choice == "5":
        break
