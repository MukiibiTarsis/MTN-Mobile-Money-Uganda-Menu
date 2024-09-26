code = input("Input the code")
if code == '*185#' or "*165#":
 print ("MTN Mobile Money:")
 print ("1) Send Money")
 print ("2) Airtime & Bundles")
 print ("3) Pay with MoMo")
 print ("4) Payments")
 print ("5) Savings & Loans")
 print ("6) Financial Services")
 print ("7) Insurance")
 print ("8) Account")
else : 
 print("Invalid Input")
  
choice = input("Select option")
if choice == '1':
    print("Send Money")
    print("1) Mobile User")
    print("2) Africa")
    print("3) Rest of the World")
    print("4) Donations")
    print("0) Back")
    smchoice = input("Select option")
    if smchoice == '1':
      smno = input("Input the number")
      smamount = input("Input amount to send")
      smpin = input("Input the PIN")
      print (f"You have successfully sent Ugx.{smamount} to {smno}")
    if smchoice == '2':
      print("Africa")
      print("1) Eastern Africa")
      print("2) Western Africa")
      print("3) Southern Africa")
      print("4) Central Africa")
      africachoice = input("Select option")
      if africachoice == '1':
        print("Eastern Africa")
        print("1) Kenya")
        print("2) Tanzania")
        print("3) Rwanda")
        eachoice = input("Select option")
        if eachoice == '1':
          print("1) M-Pesa")
          print("2) Safari.com")
          kenyachoice = input("Select option")
          if kenyachoice == '1':
            mpesano = input("Input M-Pesa number")
            mpesaamount = input("Enter Amount")
            mpesapin = input("Input your PIN")
            print(f"You have successfully sent {mpesaamount} to {mpesano}")

          if kenyachoice == '2':
            safarino = input("Input Safari number")
            safariamount = input("Enter Amount")
            safaripin = input("Input your PIN")
            print(f"You have successfully sent {safariamount} to {safarino}")

        if eachoice == '2':
            print("1) M-Pesa")
            print("2) Safari.com")
            kenyachoice = input("Select option")
            if kenyachoice == '1':
              mpesano = input("Input M-Pesa number")
              mpesaamount = input("Enter Amount")
              mpesapin = input("Input your PIN")
              print(f"You have successfully sent {mpesaamount} to {mpesano}")

            if kenyachoice == '2':
              safarino = input("Input Safari number")
              safariamount = input("Enter Amount")
              safaripin = input("Input your PIN")
              print(f"You have successfully sent {safariamount} to {safarino}")
          
        if eachoice == '3':
          print("1) MTN Rwanda")
          print("2) Airtel Rwanda")
          rwandachoice = input("Select option")
          if rwandachoice=='1':
            print("MTN Rwanda")
            rwandano = input("Input number")
            rwandaamount = input("Enter amount")
            rwandapin = input("Input PIN")
            print(f"You have successfully sent {rwandaamount} to {rwandano}.")

          if rwandachoice=='2':
            print("Airtel Rwanda")
            rwandano = input("Input number")
            rwandaamount = input("Enter amount")
            rwandapin = input("Input PIN")
            print(f"You have successfully sent {rwandaamount} to {rwandano}.") 

        else:
          print("Invalid input")  
                  
      

      if africachoice == '2':
        print("Western Africa")
        wano = input("Input the number")
        waamount = input("Enter Amount")
        wapin = input("Input PIN")
        print(f"You have successfully sent Ugx.{waamount} to {wano}.")

      if africachoice == '3':
        print ("Southern Africa")
        print("1) MTN South Africa")
        print("2) Airtel South Africa")
        sachoice = input("Select option")
        if sachoice == '1':
          samtnno = input("Input number")
          samtnamount = input("Enter Amount")
          samtnpin = input("Enter PIN")
          print(f"You have successfully sent {samtnamount} to {samtnno}")
      if africachoice == '4':
        print("Central Africa")
        print("1) Congo Brazaville")
        print("2) DRC")
        cachoice = input("Select option")
        if cachoice == '1':
          cano = input("Enter number")
          caamount = input("Enter amount")
          capin = input("Enter PIN")
          print(f"You have successfully sent {caamount} to {cano}.")
      if choice == '2':
        cano = input("Enter number")
        caamount = input("Enter amount")
        capin = input("Enter PIN")
        print(f"You have successfully sent {caamount} to {cano}.")

      if smchoice == '3':
        print 
      if smchoice == '4':
        print
      if smchoice == '5':
        print

if choice == '2':
    print("Airtime & Bundles")
    print("1) Airtime")
    print("2) Voice Bundles")
    print("3) Internet Bundles")
    print("4) Freedom Bundles")
    print("5) Special Bundles")
    print("6) WakaNet")
    print("7) SMS Bundles")
    print("0) Back")
    print("00) Next")

elif choice == '3':
  merchantcode = int(input("Please Enter Merchant Code or Invoice ID"))
  if merchantcode == '1902':
    amount = int(input("Enter Amount"))
    momopin = int(input(f"Enter your PIN to complete transaction of Ugx. {amount}"))
  else:
    amount = int(input("Enter Amount"))
    momopin = int(input(f"Enter your PIN to complete transaction of Ugx. {amount}"))
    print(f"You have successfully made a Ugx.{amount} transaction.")

elif choice == '4':
    print("Payments")
    print("1) Utilities")
    print("2) Pay TV")
    print("3) School Fees")
    print("4) Goods & Services")
    print("5) Fees & Taxes")
    print("6) Lotto & Sports Betting")
    print("7) Music & Video")
    print("0) Back")
    print("00) Next")

elif choice == '5':
 print("savings & Loans")
 print("1) MoKash")
 print("2) Phone Loans")
 print("3) MoMo Advance")
 print("4) MoPESA")
 print("5) MoSente")
 print("6) XtraCash")
 print("7) Xeno")
 print("0) Back")
 print("00) Next")

elif choice == '6':
 print("Financial Services")
 print("1) Send to Bank Account")
 print("2) Get Money from Bank")
 print("3) SACCO")
 print("4) Pension Schemes")
 print("5) MoMoCard")
 print("6) Uganda Securities Exchange")
 print("0) Back")
 print("00) Next")

elif choice == '7':
 print("Insurance")
 print("1) Insurance")
 print("2) Health")
 print("3) Cover by MoMo")
 print("0) Back")

elif choice == '8':
 print("Account")
 print("1) Check Balance")
 print("2) Fees Calculator")
 print("3) My Approvals")
 print("4) My Transactions")
 print("5) Change PIN")
 print("6) PIN reset")
 print("7) Initiate Reversal")
 print("0) Back")
 print("00) Next")
else :
  print("Invalid input")
