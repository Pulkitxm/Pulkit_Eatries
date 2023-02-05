try:
  import Main
  Email=True
  Pass=True
  print("                           o-x-o-x-o-x-o-x-o-x-o-x-o-x-o-x")
  print("                             Welcome To Pulkit Eatries")
  print("                             Take away n Dine")
  print("                           o-x-o-x-o-x-o-x-o-x-o-x-o-x-o-x")
  print("                             Mobile Number-9087654321")
  print()
  print('Hello i am a robo and i am here to help you out')
  print('Please sign in to place an order')
  Email=False
  import random
  print()
  print('                              Welcome To Google sign in')
  print('                              Sign in into Pulkit Eatries')
  print()
  print()
  print()
  print()
  a=input('Sign-in(i) or Sign-up(u) - ')
  if a=='i':
    email=input('Enter  you gmail id - ')
    if email.count('@')==1 and  email.split('@')[1]=='gmail.com':
          password=input('Enter your passowrd (If you have forgot your Password , then enter "Forgot") - ')
          if password=='Forgot':
              ap=True
              while ap:
                captcha=''
                for i in range(10):
                  captcha+=chr(random.randint(49,97+27))
                print('Captcha code-'+captcha)
                Captcha=input('Enter the captcha code displayed above - ')
                if captcha==Captcha:
                  password=input("Enter a new password - ")
                  re=input('Reenter your password-')
                  if password==re:
                    print('Signed in Successflully')
                    confirm=input('Do you want to allow Pulkit Eatries to acces your email (yes/no)-')
                    if confirm=='yes':
                              Email=True
                              Pass=True
                              print('Signed in Successfully')
                              print('Now you are returning back to Pulkit Eatries page')
                              ap=False
                else:
                  print('Iincoreect code please try again')
          else:
            if len(password)>6:
              print('Signed in Successflully')
              choice_signin=input('Do you want to sign in into Pulkit Eatries with '+email+' (yes/no) - ')
              if choice_signin=='yes':
                print('Signed in Succesfully and your are returning back to Pulkit Eatries')
                Email=True
                Pass=True
            else:
              print('Invalid Password')
    else:
      print('User not found')
  elif a=='u':
    user_name=input('''Enter your Full Name (Don't leave space between words) -''')
    email_name=input('Enter an Email id (to use '+user_name+'@gmail.com enter use) - ')
    if email_name=='use':
      email_name=user_name+'@gmail.com'
    print('So now your email id is - '+email_name)
    password=input('Enter a strong password (to let google create a password for you enter create) -')
    if password=='create':
      p=''
      for i in range(10):
        p+=chr(random.randint(49,97+27))
      print('Now you password is - '+p)
      choice_signin=input('Do you want to sign in into Pulkit Eatries with '+email_name+' (yes/no) - ')
      if choice_signin=='yes':
        print('Signed in Succesfully and your are returning back to Pulkit Eatries')
        Email=True
        Pass=True
    else:
      Email=True
      Pass=True
  if Pass==True and Email==True:
    Main.Menu()
    Main.Order()
  else:
    print('Please check your email')
except:
  print('Enter a valid Input , I am getting Some errors ❁´◡`❁ .')
