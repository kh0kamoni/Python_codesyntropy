while True:
    print("0. Exit")
    dial = input("Dial *247# to go to mobile menu: ")
    if dial == "*247#":
            print("bKash\n1. Send Money\n2. Buy Airtime\n3. Payment\n4. Cash Out\n5. Pay Bill\n6. Remittance\n7. My bKash\n8. Helpline")
            payment = int(input("Enter \"3\" to select Payment: "))
            if payment == 3:
                number = input("Enter Merchant bKash Account No: ")
                if len(number) == 11:
                    amount = int(input("Enter Amount: "))
                    if amount > 0:
                         reference = int(input("Enter Reference: "))
                         if reference >= 0:
                              counter = int(input("Counter: "))
                              if counter >= 0:
                                   print(f"Payment\n To: {number}\n Amount: Tk {amount}\n Reference: {reference}\n Counter: {counter}")
                                   pin = int(input("Enter Menu PIN to Confirm: "))
                                   print(f"Payment\n Tk {amount}\n to: {number}\n Ref {reference}\n Counter: {counter}. Fee Tk 0.00. Balance Tk XXXXXX. TxrID SKJ33H39 at 15/09/2018 15:12")
                                   break
                         
                else:
                        print("Invalid number.")
            else:
                break
    elif dial == '0':
        break
    else:
         break
    


