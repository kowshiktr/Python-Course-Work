data={
    12345:{'pin':123,'balance':5678,'history':[]},
    23456:{'pin':123,'balance':5678,'history':[]},
    67891:{'pin':123,'balance':5678,'history':[]},
    45674:{'pin':123,'balance':5678,'history':[]},
    36783:{'pin':123,'balance':5678,'history':[]},
}
acc_num=None
login_status=None
def Welcome():
    print('Welocome to the ATM'.center(50,'*'))
def Menu():
    print('\n[C]heck Balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')
def Login():
    account_number=int(input("Enter the account number:"))
    pin=int(input("Enter the pin:"))
    global login_status
    if account_number in data:
        if data[account_number]['pin']==pin:
            print("Login Succcessful")
            acc_num=account_number
            login_status=True
            return True
        else:
            print("Inavild pin")
            login_status=False
            return False
    else:
        print("Invalid acconut number")
        login_status=False
        return False
def Chcek_balance():
    if login_status and acc_num:
        print(f'\nCurrent Balance:{data[acc_num]["balance"]}')
    else:
        print("You need to login again")
def Withdraw():
    if login_status and acc_num:
        amount=int(input("Enter the amount to withdraw:"))
        if data[acc_num]['balance']>=amount:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdraw-${amount}')
        else:
            print("Insufficient Balance")
    else:
        print("You need to login again")
        def Deposit():
            if login_status and acc_num:
                amount=int(input("Enter the amount to deposit:"))
                data[acc_num]['balance']>=amount
                data[acc_num]['balance']-=amount
                data[acc_num]['history'].append(f'Withdraw-${amount}')
                print(f'${amount} is succesfully Withdraw')
            else:
                print("You need to login again")
        def Withdraw():
            if login_status and acc_num:
                amount=int(input("Enter the amount to withdraw:"))
                if data[acc_num]['balance']>=amount:
                    data[acc_num]['balance']-=amount
                    data[acc_num]['history'].append(f'Withdraw-${amount}')
                    print(f'${amount} is successfully Withdraw')
                else:
                    print("Insufficent Balance")
            else:
                print("You need to login again")
        def View_transaction():
            if login_status and acc_num:
                if data[acc_num]['history']:
                    print("Transactions History".center(50,'-'))
                    for i in data[acc_num]['history']:
                        print(i)
                    else:
                        print("End of the history".center(50,'_'))
                else:
                    print("No Transactions")
            else:
                print("you need to lofin again")



