def menu():
    print("**********Menu*********")
    print("*a.Deposite           *")
    print("*b.Withdraw           *")
    print("*c.Exit               *")
    print("***********************")

balance = 0
choose = ''

while choose.lower() != 'c':
    menu()
    choose = input('Enter your choice: ')
    if choose.lower() == 'a':
        amount = float(input("Enter depostie amount: "))
        if balance > 1000:
            balance = (balance + amount) + (balance * 0.03)
            print('Balance=',balance)
        else:
            balance = balance + amount
            print('Balance=',balance)
    elif choose.lower() == 'b':
        withdraw = float(input('Enter withdraw amount: '))
        if balance<500:
            penality = balance * 0.03
            balance = balance - withdraw - penality
            
            print('Balance=',balance)
            print('penality=', penality)
        else:
            balance = balance - withdraw
            print('Balance=',balance)
    elif choose.lower() == 'c':
        break
    else: 
        print('Wrong choice!')