import random
guests={}
print("Enter the number of friends joining (including you):")
number=int(input())
print("")
if number>0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(0,number):
        name=input()
        guests[name]=0
    print("")
    print("Enter the total amount:")
    amount=int(input())
    print("")
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky=input()
    if lucky=="Yes":
        lucky_one=random.randint(0,number-1)
        print("")
        print(list(guests)[lucky_one], "is the lucky one!")
        number=number-1
        check=amount/number
        check=round(check,2)
        guests1={}
        guests1[list(guests)[lucky_one]]=0
        for key in guests:
            guests[key] = guests[key] + check
        guests.update(guests1)
        print("")
        print(guests)
    else:
        print("No one is going to be lucky")
        check=amount/number
        check=round(check,2)
        for key in guests:
            guests[key]=guests[key]+check
        print("")
        print(guests)
else:
    print("No one is joining for the party")