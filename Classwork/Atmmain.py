import Atmlogic as atm
atm.welcome()
if atm.Login():
    while True:
        atm.Menu()
        ch=input("Enter the choice:").upper()
        if ch=='c':
            atm.Check_balance()
        elif ch=='D':
            atm.Deposit()
        elif ch=='W':
            atm.Withdraw()
        elif ch=='V':
            atm.View_transaction()
        elif ch=='E':
            print("Thankyou".center(50,'_'))
            break
        else:
            print("Invaild Choice")