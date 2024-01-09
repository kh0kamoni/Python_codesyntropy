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
                else:
                    print("Invalid number.")
            else:
                break
    elif dial == '0':
        break
    else:
         break
    


