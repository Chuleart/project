import time
  #import เวลา
def main():
  timeis = time.localtime()
  a = time.strftime('%H''%M', timeis)
  try:  
    t = input("do you want parking Y or N: ")
    if t == "Y" or t == "y":
        print("You start to park at :",a,)
        Time()
    elif t == "N" or t == "n":
        exit()
    else:
      print("Do not enter characters that do not use Y and N.")
      main()
  except:
    print("Do not enter characters")
    main()

def Time():
  timeis = time.localtime()
  a = time.strftime('%H''%M', timeis)

  c2 = input("do you want out parking :")
  #ระบุเวลาออก
  total = (int(c2) - int(a))
  costPerHour = 20
  if total: 
    hours = round(int(total/ 60)) 
    total2 = round(hours * costPerHour, 2)  
    print('Your parking for ' + str(hours) + ' hours or ' + str(total) + ' minutes')  
    print('Total cost is ' + str(total2) + ' baht')
  else: 
    print('Error')

main()
