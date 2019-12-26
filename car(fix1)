import time

def main():
    print("welcome to parking")
    try:
        T= input("do you want parking Y or N: ")
        if T == "y" or T == "Y":
            date()
        elif T == "n" or T == "N":
            exit()
        else:
            print("Do not enter characters that do not use Y and N.")
            main()
    except:
      print("Do not enter characters")
      main()

def date():
   timeis = time.localtime()
   a = time.strftime('%d', timeis)
   #def time.strftime %d = day 
   date =int(a)
   #date = day 
   if date % 2 == 0:
    print("Invited to the left")
   else: 
    print("Invited to the right")


main()    
