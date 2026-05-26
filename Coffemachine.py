class CoffeeMachine:
    def __init__(self):
        self.w=400
        self.m=540
        self.b=120
        self.c=9
        self.mon=550
        self.state="main"
        self.exit=0
        print("Write action (buy, fill, take, remaining, exit):")
    def process_input(self,action):
        if self.state=="main":
            if action=="buy":
                self.state="buy"
                print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            elif action=="fill":
                self.state="fill_w"
                print("\nWrite how many ml of water you want to add:")
            elif action=="take":
                print("\nI gave you", self.mon, "\n")
                self.mon=0
                print("Write action (buy, fill, take, remaining, exit):")
            elif action=="remaining":
                print("\nThe coffee machine has:")
                print(self.w, "of water")
                print(self.m, "of milk")
                print(self.b, "of beans")
                print(self.c, "of disposable cups")
                print(self.mon, "of money\n")
                print("Write action (buy, fill, take, remaining, exit):")
            else:
                self.exit=1
        elif self.state=="buy":
            if action=="1":
                if self.w<250:
                    print("Sorry, not enough water!\n")
                elif self.b<16:
                    print("Sorry, not enough coffee beans!\n")
                elif self.c==0:
                    print("Sorry, not enough disposable cups!\n")
                else:
                    print("I have enough resources, making you a coffee!\n")
                    self.w=self.w-250
                    self.b=self.b-16
                    self.c=self.c-1
                    self.mon=self.mon+4
            elif action=="2":
                if self.w<350:
                    print("Sorry, not enough water!\n")
                elif self.m<75:
                    print("Sorry, not enough milk!\n")
                elif self.b<20:
                    print("Sorry, not enough coffee beans!\n")
                elif self.c==0:
                    print("Sorry, not enough disposable cups!\n")
                else:
                    print("I have enough resources, making you a coffee!\n")
                    self.w=self.w-350
                    self.m=self.m-75
                    self.b=self.b-20
                    self.c=self.c-1
                    self.mon=self.mon+7
            else:
                if self.w<200:
                    print("Sorry, not enough water!\n")
                elif self.m<100:
                    print("Sorry, not enough milk!\n")
                elif self.b<12:
                    print("Sorry, not enough coffee beans!\n")
                elif self.c==0:
                    print("Sorry, not enough disposable cups!\n")
                else:
                    print("I have enough resources, making you a coffee!\n")
                    self.w=self.w-200
                    self.m=self.m-100
                    self.b=self.b-12
                    self.c=self.c-1
                    self.mon=self.mon+6
            self.state="main"
            print("Write action (buy, fill, take, remaining, exit):")
        elif self.state=="fill_w":
            self.w=self.w+int(action)
            self.state="fill_m"
            print("Write how many ml of milk you want to add:")
        elif self.state=="fill_m":
            self.m=self.m+int(action)
            self.state="fill_b"
            print("Write how many grams of coffee beans you want to add:")
        elif self.state=="fill_b":
            self.b=self.b+int(action)
            self.state="fill_c"
            print("Write how many disposable cups you want to add:")
        elif self.state=="fill_c":
            self.c=self.c+int(action)
            print("")
            self.state="main"
            print("Write action (buy, fill, take, remaining, exit):")
machine=CoffeeMachine()
while machine.exit==0:
    user_input=input("> ")
    machine.process_input(user_input)