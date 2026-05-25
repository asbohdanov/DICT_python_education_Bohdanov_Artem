import random
print("How many pencils would you like to use:")
game=1
while game==1:
    a=input("> ")
    if a.isnumeric()==False:
        print("The number of pencils should be numeric")
    elif int(a)==0:
        print("The number of pencils should be positive")
    else:
        a=int(a)
        print("Who will be first (Alex, Artem) :")
        name2="0"
        while  name2=="0":
            name1=input("> ")
            if name1=="Alex":
                name2="Artem"
            elif name1=="Artem":
                name2="Alex"
            else:
                print("Choose between 'Alex' and 'Artem'")
        names=[name1,name2]
        number=0
        print("|" * a)
        print(names[number], "'s turn:", sep="")
        while a>0:
            if names[number]=="Artem":
                if a%4==0:
                    b=3
                elif a%4==1:
                    bot=0
                    while bot==0:
                        b=random.randint(1,3)
                        if b>a:
                            bot=0
                        else:
                            bot=1
                elif a%4==2:
                    b=1
                else:
                    b=2
                print(b)
                a=a-b
                if number==1:
                    number=0
                else:
                    number=1
                if a==0:
                    print(names[number], "won!")
                else:
                    print("|" * a)
                    print(names[number], "'s turn:", sep="")
            else:
                b=int(input("> "))
                if b>3:
                    print("Possible values: '1','2' or '3'")
                elif b>a:
                    print("Too many pencils were taken")
                else:
                    a=a-b
                    if number==1:
                        number=0
                    else:
                        number=1
                    if a==0:
                        print(names[number], "won!")
                    else:
                        print("|" * a)
                        print(names[number], "'s turn:", sep="")
            game=0