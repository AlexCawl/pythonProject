surname, name, group = input().split()
print("Привет, %s %s из группы %s!" % (surname, name, group))
mail = input("Введи свою электронную почту?\n")
print(surname[:5].lower() + name[:5].lower()*2 + mail[:5].lower()*3)