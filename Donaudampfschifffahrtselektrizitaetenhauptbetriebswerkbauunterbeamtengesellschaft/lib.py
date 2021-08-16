import random

def try_me():
    print("You have to guess the secret number. You just have only 3 tries")
    counter=0
    number = random.randint(1,99)
    flag =True
    while(flag):
        counter+=1
        number_user = int(input("Pick a whole number between one and  one hundred. "))
        if number == number_user:
            print(f"Well done, you did it in {counter} tries")
            flag == False;
        elif counter==3:
            print("You haven´t guess the number!. That a REASON FOR EXCLUSION!")
            flag = False;
        else:
            print("Wrong number, keep trying!")