import time
import os

def main():
    print("welcome to parking")
    T= input("do you want parking Y or N: ")
    if T == "y" or T == "Y":
        os.system("cls")
        date()
    elif T == "n" or T == "N":
        os.system("cls")
        print("Exit")
        exit()
    else:
        os.system("cls")
        print("Do not enter characters that do not use Y and N.")
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
