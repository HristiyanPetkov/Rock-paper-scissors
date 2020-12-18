from rock import check

while True:
    print("Player one")
    choice1 = input("Choose between rock(r), paper(p) and scissors(s): ")
    print("Player two")
    choice2 = input("Choose between rock(r), paper(p) and scissors(s): ")
        
        
    print(check(choice1, choice2))
        
    print()
    
    if input("Do you wich to continue? ") == 'e':
        break