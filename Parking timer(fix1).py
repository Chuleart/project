import time
timeis = time.localtime()
a = time.strftime('%H''%M', timeis)
#import เวลา
Y = input("do you want parking Y or N")
# ต้องการที่จอดรถไหม
if Y <= Y:
    print("start",a)
else :
    print("ok")
c2 = input("do you want out parking :")
#ออกและระบุเวลา
total = (int(c2) - int(a))
costPerHour = 20
if total:
  
  hours = round(int(total/ 60))

  total2 = round(hours * costPerHour, 2)

  print('Your parking for ' + str(hours) + ' hours or ' + str(total) + ' minutes')

  print('Total cost is ' + str(total2) + ' baht')

else:

  print('Error')
