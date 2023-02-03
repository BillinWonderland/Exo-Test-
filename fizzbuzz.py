



def fonction_fizzbuzz(user_value):
    if user_value:
        if user_value%3 == 0:
            print ("fizz")
        elif user_value%5 == 0:
            print ("buzz")
        elif user_value%3 == 0 and user_value%5 == 0:
            print ("fizz buzz")
        else: print(str(user_value) +" ne se divise pas sans avoir de decimale")

print("")
print("")

user_value = int(input("Bienvenue dans le FizzBuzz veillez rentrer un nombre : " ))

fonction_fizzbuzz(user_value)