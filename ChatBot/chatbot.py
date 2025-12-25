print("Hello! My name is Bot_mk1")
print("I was created in 2025")
print("Please, remind me your name.")
user_name=input()
print("What a great name you have, ", user_name, "!", sep="")
print("Let me guess your age")
print("Enter remainders of dividing your age by 3,5 and 7")
remainder3=int(input())
remainder5=int(input())
remainder7=int(input())
age=(remainder3*70+remainder5*21+remainder7*15)%105
print("Your age is ", age, "; that's a good time to start programming!", sep="")
print("Now I will prove to you that I can count to any number you want")
count_number=int(input())
a=0
for i in range(count_number+1):
    print(a, "!")
    a=a+1
print("Let's test your programming knowledge.")
print("Why do we use methods?")
answer=0
print("1.To repeat a statement multiple times")
print("2.To decompose a program into several small subroutines.")
print("3.To determine the execution time of a program.")
print("4.To interrupt the execution of a program.")
while answer==0:
    user_answer=input()
    if user_answer=="2":
        print("Completed, have a nice day!")
        answer=1
    else:
        print("Please, try again.")
print("Congratulations, have a nice day!")