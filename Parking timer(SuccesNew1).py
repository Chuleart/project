import time,os

def mainloop():
    os.system("cls") 
    #ที่วางจอดรถ
    praking = ["P1","P2","P3","P4","P5"]
    praking_sorted = sorted(praking)
    out = []
    out_sorted = sorted(out)
    #ที่วางจอดรถ
    #หลักการทำงาน praking = ["P1","P2","P3","P4","P5"] คือที่จอด out = [] ทีจอดไปแล้ว
    #p1-5 บันทึกเวลา 
    #เข้า in บันทึกเวลา เวลาจะเป็นเวลาปัจจุบันทีกดเข้า หน้า in และ ถูกบันทุกที่ p1 
    #เลือกที่จอด บันทีกเวลา ลบที่จอดได้ออก ไปที่ out แลคิดตัง
    #เวลาในที่จอดรถ
    
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    p5 = []

    #เวลาในที่จอดรถ

    #ในสวนของการทำให้ที่จอดรถมากกว่า 5 ที่ ทฤษฎี ใช่ for loop สร้างพื้นที่ในการจัดเก็บข้อมูลแล้วในการจัดเก็บ parking 

    def menu():
        # main 
        print("===================================")
        print("=========Welcome to Parking========")
        print("=== Do you want to enter or exit ==")
        print("=            in(1)                =")
        print("=            out(2)               =")
        print("=      check Time to in(3)        =")
        print("===================================")
        Theneed =input("   Fill in the required items :")
        if Theneed == "1":
            os.system("cls")
            in1()
            # 1 
        elif Theneed == "2":
            os.system("cls")
            Time()
            # 2
        elif Theneed == "3":
            os.system("cls")
            checktime()
            # 3
        elif Theneed == "*":
            os.system("cls")
            print(praking)
            menu()
            # 4
        else:
            os.system("cls")
            print("error ++")
            menu()


    def in1():
        #1
        timeis = time.localtime()
        a = time.strftime('%H''%M', timeis)
        t = input("do you want parking Y or N: ")
        # ต้องการจอด หรือไม่
        if t == "Y" or t == "y":
            os.system("cls")
            print("At this time",a)
            print("Free parking :",praking_sorted)
            Select = input("Select parking P? (E:exit): ")
            try:
                #เลือกที่จอด
                if Select == "P1" or Select  == "p1":
                    p1.append(a)
                    praking_sorted.remove("P1")
                    out_sorted.append("P1")
                    os.system("cls")
                    print("===================================")
                    print(" ========== Time ", a ,"===========")
                    menu()

                elif Select == "P2" or Select == "p2":
                    st = a
                    p2.append(st)   
                    praking_sorted.remove("P2")
                    out_sorted.append("P2")
                    os.system("cls") 
                    print("===================================")
                    print(" ========== Time ", a ,"===========")
                    menu()

                elif Select == "P3" or Select == "p3":
                    st = a
                    p3.append(st)
                    praking_sorted.remove("P3")
                    out_sorted.append("P3")
                    os.system("cls")
                    print("===================================")
                    print(" ========== Time ", a ,"===========")

                    menu()

                elif Select == "P4" or Select == "p4":
                    st = a
                    p4.append(st)
                    praking_sorted.remove("P4")
                    out_sorted.append("P4")
                    os.system("cls")
                    print("===================================")
                    print(" ========== Time ", a ,"===========")
                    menu()

                elif Select == "P5" or Select == "p5":
                    st = a
                    p5.append(st)
                    praking_sorted.remove("P5")
                    out_sorted.append("P5")
                    os.system("cls")
                    print("===================================")
                    print("=========== Time ", a ,"===========")
                    menu()
                elif Select == "e" or Select == "E":
                    os.system("cls")
                    menu()
                else:
                    os.system("cls")
                    print("error eng")
                    #Error ตัวอักษรหรือเลข
                    in1()
            except:
                os.system("cls")
                print("=Do not select items that do not exist.=")
                in1()
                #Error หา list ไม่เจอหรือ รายการใช่ไปแล้วแต่ยังไม่มีการออกจากที่จอดรถ
        elif t == "N" or t == "n":
            #no
            os.system("cls")
            menu()
        else:
            #ok
            os.system("cls")
            print("Do not enter characters that do not use Y and N.")
            in1()

    def Time():
        #2
        t = input("Do you want to exit the parking lot? Y or N: ")
        #ถามอีกรั้งว่าต้องการจอดไหม
        if t == "Y" or t == "y":
            #Yes
            os.system("cls")
            cal()

        elif t == "N" or t == "n":
            #No
            os.system("cls")
            menu()
        else:
            #Ok
            os.system("cls")
            print("Do not enter characters that do not use Y and N.")
            menu()


    def cal():
        #2.2
        timeis = time.localtime()
        a = time.strftime('%H' '%M', timeis)
        
        print(out_sorted)
        c = input("Choose your parking (E:Exit to menu): ")
        try:
            if c == "p1" or c == "P1":
                os.system("cls")
                out_sorted.remove("P1")
                praking_sorted.append("P1")
                for x in p1:
                    if x > "":
                        print(x)
                        p1.clear()

            elif c == "p2" or c == "P2":
                os.system("cls")          
                out_sorted.remove("P2")
                praking_sorted.append("P2")
                for x in p2:
                    if x > "":
                        print(x)
                        p2.clear()

            elif c == "p3" or c == "P3":
                os.system("cls")
                out_sorted.remove("P3")
                praking_sorted.append("P3")
                for x in p3:
                    if x > "":
                        print(x)
                        p3.clear()

            elif c == "p4" or c == "P4":
                os.system("cls")
                out_sorted.remove("P4")
                praking_sorted.append("P4")
                for x in p4:
                    if x > "":
                        print(x)
                        p4.clear()

            elif c == "p5" or c == "P5" :
                os.system("cls")
                out_sorted.remove("P5")
                praking_sorted.append("P5")
                for x in p5:
                    if x > "":
                        print(x)
                        p5.clear()

            else:
                os.system("cls")
                print("error calculator")
        except:
            os.system("cls")
            print("=Do not select items that do not exist.=")
            cal()

        if x:
          os.system("cls") 
          print(x)
          print(a)
          total = (int(a) - int(x))
          print(total)
          costPerHour = 20
          hours = round(int(total/ 60)) 
          total2 = round(hours * costPerHour, 2)  
          print('Your parking for ' + str(hours) + ' hours or ' + str(total) + ' minutes')  
          print('Total cost is ' + str(total2) + ' baht')
          restart()
        else: 
          print('Error')
        

    def restart():
        # 3
        R = input("return to menu Y or N: ")
        if R == "y" or R == "Y":
           os.system("cls")
           menu()
        elif R == "n" or R == "N":
           os.system("cls")
           print("Exit")
           exit()
        else:
           os.system("cls")
           print("Do not enter characters that do not use Y and N.")
           restart()

    def checktime():
        print("Can park   :",praking_sorted)
        print("Can't park :",out_sorted)
        print("parking 1  :",p1)
        print("parking 2  :",p2)
        print("parking 3  :",p3)
        print("parking 4  :",p4)
        print("parking 5  :",p5)
        menu()


    menu()
mainloop()
