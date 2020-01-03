import time
import os

def main():
 timeis = time.localtime()
 a = time.strftime('%H''%M', timeis)
 t = input("do you want parking Y or N: ")
 if t == "Y" or t == "y":
     print("You start to park at :",a,)
     Time()
 elif t == "N" or t == "n":
     os.system("cls")
     print("Exit")
     exit()
 else:
   print("Do not enter characters that do not use Y and N.")
   main()

def Time():
  timeis = time.localtime()
  a = time.strftime('%H''%M', timeis)

  c2 = input("do you want out parking :")
  #ระบุเวลาออก
  total = (int(c2) - int(a))
  costPerHour = 20
  if total:
    os.system("cls") 
    hours = round(int(total/ 60)) 
    total2 = round(hours * costPerHour, 2)  
    print('Your parking for ' + str(hours) + ' hours or ' + str(total) + ' minutes')  
    print('Total cost is ' + str(total2) + ' baht')
    restart()
  else: 
    print('Error')

def restart():
  R = input("do you want Restrat parking Timer ?  Y or N: ")
  if R == "y" or R == "Y":
     os.system("cls")
     main()
  elif R == "n" or R == "N":
     os.system("cls")
     print("Exit")
     exit()
  else:
     os.system("cls")
     print("Do not enter characters that do not use Y and N.")
     restart()

main()
