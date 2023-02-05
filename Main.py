import Function
import random
def Menu():
  print('Here is our menu-')
  print()
  print('Sancks')
  for i in range(1,len(Function.Price)+1):
    print(i,')',Function.item_name(i),'(₹',Function.item_price(i),')')    
    if i==10:
      print()
      print('a la carte')
    if i==20:
      print()
      print('Sweet dish')
    if i==30:
      print()
      print('Our Combos')
  print()
  print('Note to select an item please enter the  serial code of a single item only')

def Order():
  Bill=0
  l=[]
  Bill_List=[]
  Snack_ch=True
  while Snack_ch:
    Snack=input('Would you like to have some snacks (if yes then plz enter the serial number of the snack (between 1-10) , else enter any number(Between 1-40) and 0 in the next section) - ')
    freq=float(input('Please tell me how much quantity of '+Function.item_name(Snack)+' do you want (ie X 1,2,3.....) -  X'))
    Bill_List.append(freq)
    d=Function.item_price(Snack)
    l.append(Snack)
    Bill+=d*freq
    s=input('Would you like to have more snacks(yes/no) -')
    if s=='no':
      Snack_ch=False
    elif s=='yes':
      Snack_ch=True
    else:
      print('Enter yes/no')
  print()
  print("Remember the best things to fill up your tummy is chapati")
  Main_ch=True
  while Main_ch:
    Main=input('So what would you like to have in main course (if you want to have then plz enter the serial number of the item (between 11-20 , else enter any number(Between 1-40) and 0 in the next section - ')
    freq=float(input('Please tell me how much quantity of '+Function.item_name(Main)+' do you want (ie X 1,2,3.....) -  X'))
    Bill_List.append(freq)
    d=Function.item_price(Main)
    l.append(Main)
    Bill+=d*freq
    s=input("Won't you like to have some Breads from our Main Course(yes/no) - ")
    if s=='no':
      Main_ch=False
    elif s=='yes':
      Main_ch=True
    else:
      print('Enter yes/no')
  print()
  print('खाने के बाद कुछ मीठा हो जाए ')
  Sweet_ch=True
  while Sweet_ch:
    Sweet=input('So what would you like to have in Sweet (if you want to have then plz enter the serial number of the item  (between 21-30 , else enter any number(Between 1-40) and 0 in the next section - ')
    freq=float(input('Please tell me how much quantity of '+Function.item_name(Sweet)+' do you want (ie X 1,2,3.....) -  X'))
    Bill_List.append(freq)
    d=Function.item_price(Sweet)
    l.append(Sweet)
    Bill+=d*freq
    s=input('Would you like to have more Sweets(yes/no) -')
    if s=='no':
      Sweet_ch=False
    elif s=='yes':
      Sweet_ch=True
    else:
      print('Enter yes/no')
  Combo_ch=True
  while Combo_ch:
    Combo=input('So what would you like to have in Combos (if you want to have then plz enter the serial number of the item  (between 21-30 , else enter any number(Between 1-40) and 0 in the next section - ')
    freq=float(input('Please tell me how much quantity of '+Function.item_name(Combo)+' do you want (ie X 1,2,3.....) -  X'))
    Bill_List.append(freq)
    d=Function.item_price(Combo)
    l.append(Combo)
    Bill+=d*freq
    s=input('Would you like to have more Combo(yes/no) -')
    if s=='no':
      Combo_ch=False
    elif s=='yes':
      Combo_ch=True
    else:
      print('Enter yes/no')

  gst=0.05*Bill
  gst=int(gst)

      
  print('So buddy your bill is ready , please pay the amount to take your meal at the soonest')
  print('Items Selected -:',)
  for i in range(len(l)):
    print(i,')  ',int(l[i]),')  ',Bill_List[i],' X '+Function.item_name(l[i]),Function.item_price(l[i])*Bill_List[i])
  print('Total - ',int(Bill),'+',gst,'(gst) =',(int(Bill)+gst))
  Bill=Bill+gst
  Bill_1=Bill
  ch=input("Do you want to redeem a code(yes/no) - ")
  c=True
  if ch=='yes':
    while c:
      a=input('Please enter a redeem code(Enter your name) - ')
      if Bill>700:
        if a in ['Pulkit','SoniaDogramMam','Pulkit Eatries']:
          Bill-=500
          c=False
        else:
          print('''Try a name from ['Pulkit','Pulkit Eatries']''')
      else:
        print('Sorry your Code could not be redeemed since your bill is less than ₹700 (',Bill,')')
        c=False
      
    Bill=int(Bill)  
    print('So buddy your bill is ready , please pay the amount to take your meal at the soonest')
    print('Items Selected -:',)
    for i in range(len(l)):
      print(i,')  ',int(l[i]),')  ',Bill_List[i],' X '+Function.item_name(l[i]))
    print('Total - ',Bill_1,'-500 =',Bill)

  from datetime import date , timedelta
  today = date.today()
  td = timedelta(days=5)
  date = today + td


  number=(input('Enter your mobile number - +91'))
  Name=input('Enter your name-')
  if len(number)==10:
    print('How would you like to pay-:')
    print('1)Cash on Delivery')
    print('2)From our bank service(Suggested)')
    ch_pay=input('Enter your choice-')
    if ch_pay=='1':
          print("You will recieve your order within 45 minutes")
          print('Congratulations you also win a ₹1000 voucher(Note-Valid till',date,'date, ie 5 days from now)')
    if ch_pay=='2':
      print('Bank Id - a1b2c3d4e5')
      Id=(input('Enter your bank id no. - '))
      password=1234
      print('pin = 1234')
      pin = float(input("enter your atm pin - "))
      balance = random.randint(50000,100000)
      if pin == password and Id=='a1b2c3d4e5':
        Pay=True
        while Pay==True:
              print(""" 
      1 == Check balance
      2 == Pay balance
      """)
              try:    
                  option = float(input("Please enter your choise - "))
              except:
                  print("Please enter valid option")   
              if option == 1:
                  print("Your current balance is ",balance)                        
              if option == 2:
                  if input('Pulkit Eatries is asking to withdraw your bill amount from your account, do you want to pay them the amount -')=='yes':
                    balance = balance - Bill
                    print(Bill,' is debited from your account')
                    print('your updated balance is ',balance)
                    print('Order Successfully placed')
                    print('Will reach you within 45 minutes')
                    print('Congratulation you own a ₹1000 voucher as a privilage by our bank')
                    Pay=False
                  else:
                    print('Since you did not entered yes , we have proceed to place your order keeping in mind that you will pay us on delivery.')
                    Pay=False
      else:
          print("Check your Bank Id(a1b2c3d4e5) and Pin(1234)")
  else:
    print('Invalid Number')
