name=input("Enter your name, please: ")
print(name, "Welcome to NCBA ATM cash dispenser program")
balance=10000
while True:# as long as your code is running
    print("Atm menu")
    print("deposit")
    print("withdraw")
    print("check balance")
    print("exit")
    choice=input("Select one of the above: ").lower()
    if choice=="deposit":
        depos=int(input("How much would you like to deposit: "))
        balance+=depos
        print("Your depsoit has been successful")
        print("Reciept")
        print("The person who deposited: ",name)
        print("deposit amount: ", depos )
        print("Current balance: ", balance)
    if choice=="withdraw":
        draw=int(input("How much would you like to withdraw? "))
        balance-=draw
        print("Your withdrawal has been successful")
        print("Reciept")
        print("The person who withdrawed: ",name)
        print("withdrawal amount: ", draw)
        print("Current balance: ", balance)
    if choice=="check balance":
        print(name,"s balance is: ", balance)
    if choice=="exit":
        print("Goodbye, and thank you for using NCBA bank!")
        break