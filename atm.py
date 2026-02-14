bal = 0
while True:
    
    print( '\nWelcome to the atm ')
    print('1). Deposit ')
    print('2). Withdraw ')
    print('3). Check balance')
    print('4). Exit')

    choices = int(input('Choose a function you want to use (1-6): '))
  
    if choices == 1:
        try:
            deposit = int(input('\nEnter how much you want to deposit? '))
            bal = bal + deposit
        except ValueError:
            print('Invalid action')

    elif choices == 2:
        try:
            if bal == 0:
                print('You dont have any balance on your bank. ')
                continue
            else:
                    withdraw = int(input('How much you want to withdraw? '))
                    
                    if withdraw > bal:
                        print("\nYou dont have enough balance. ")
                        continue
                    else:
                        
                        bal = bal - withdraw
                    
                        print('\nYou withdraw:' , withdraw)
                        print('1) Yes')
                        print('2) No')
                        reciept = int(input('Do want a reciept? '))
            
            if reciept == 1:
                print(f"""
                Here is your reciept:
                Your balance: {bal}
                """) 
            else:
                print("\n Thank you for using our bank")
        except ValueError:
            print('Invalid action')
            
    elif choices == 3:
        print(f'\nBalance: {bal}')
        print('1) Yes')
        print('2) No')
        reciept = int(input('Do want a reciept? '))
            
        if reciept == 1:
                print(f"""
                Here is your reciept:
                Your balance: {bal}

                """) 
        else:
                print("Thank you for using our bank")

    elif choices == 4:
        print('Thank you for using our Bank! ')
        break


    else:
        print('Invalid choices')