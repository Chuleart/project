import time,os

def main():
    Disable =["T0","T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11","T12","T13","T14","T15","T16","T17","T18","T19","T20","T25","T26","T27","T28","T29","T30"]
    #ไม่ได้เปิดใช่งาน หรือ ไม่ได้เพิมโต๊ะ
    intabel = []
    #โต๊ะทีมีและไม่ได้ใช่
    out     = []
    #โต๊ะที่มีลูกค้าแล้ว
    '''
    time = []
    #เวลาของลูกค้า
    Rable   = []
    #ลูกค้าจองโต๊ะ
    timeRable = []
    #เวลา check in ลูกค้า
    '''
    def menu():
        print("====Free Tabel====")
        print("Table Free:",intabel)
        print("Table Busy:",out)
        print("")
        print("(1) A/D")
        print("(2) Checkin")
        print("(3) Pay")
        print("(4) Exit")
        print("")

        try:
            opt = int(input("Data entry:"))
            if opt == 1 :
                os.system("cls")
                a_d()
            elif opt == 2 :
                os.system("cls")
                check_in()
            elif opt == 3 :
                os.system("cls")
                pay()
            elif opt == 4 :
                print("Exit")
                exit
            else:
                os.system("cls")
                print("Error ใน box")
                menu()
        except:
            os.system("cls")
            print("Error นอก box")
            menu()
    
    def a_d():
        print("(1) add tabel")
        print("(2) delete")
        print("(3) back to menu")
        try:
            opt = int(input("entry:"))
            if opt == 1 :
                os.system("cls")
                add()

            elif opt == 2 :
                os.system("cls")
                delete()

            elif opt == 3 :
                os.system("cls")
                menu()
            elif opt == "":
                os.system("cls")
            else:
                os.system("cls")
                print("Error a_d")
                a_d()
        except:
            os.system("cls")
            a_d()

    def add():
        #เพิ่ใโต๊ะในร้านค้าลองรับ โต๊ะถึง 0 - 30 โต๊ะ
        print("Disable",Disable)
        print("Free:",intabel)
        try:
            t = input("T1-T30 entry (Enter/Exit):")
            if t == t:
                Disable.remove(t)
                intabel.append(t)
                os.system("cls")
                print("Free:",intabel)
                add()
            else:
                os.system("cls")
                a_d()
        except:
            os.system("cls")
            print("If putting the proposal str or not clear will Back")
            a_d()
           
    def delete():
        #ลบโต๊ะที่มี
        print("Free:",intabel)
        try:
            t = input("Delete entry:")
            if t == t:
                intabel.remove(t)
                Disable.append(t)
                os.system("cls")
                delete()
            else:
                os.system("cls")
                a_d()
        except:
            os.system("cls")
            print("If putting the proposal str or not clear will Back")
            a_d()

    def check_in():
        #เพิ่มโต๊ะที่ลูกค้าเข้า
        timeis = time.localtime()
        Timeadd = time.strftime('%H''%M', timeis)
        Timein = time.strftime('%H' ':' '%M', timeis)
        print(intabel)
        try:
            t = input("Add a number table entry:")
            if t == "T1":
                intabel.remove(t)
                out.append(t)
                T1.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T2":
                intabel.remove(t)
                out.append(t)
                T2.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T3":
                intabel.remove(t)
                out.append(t)
                T3.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T3":
                intabel.remove(t)
                out.append(t)
                T4.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T4":
                intabel.remove(t)
                out.append(t)
                T5.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T5":
                intabel.remove(t)
                out.append(t)
                T5.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T6":
                intabel.remove(t)
                out.append(t)
                T6.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T7":
                intabel.remove(t)
                out.append(t)
                T7.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T8":
                intabel.remove(t)
                out.append(t)
                T8.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T9":
                intabel.remove(t)
                out.append(t)
                T9.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T10":
                intabel.remove(t)
                out.append(t)
                T10.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T11":
                intabel.remove(t)
                out.append(t)
                T11.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T12":
                intabel.remove(t)
                out.append(t)
                T12.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T13":
                intabel.remove(t)
                out.append(t)
                T13.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T14":
                intabel.remove(t)
                out.append(t)
                T14.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T15":
                intabel.remove(t)
                out.append(t)
                T15.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T16":
                intabel.remove(t)
                out.append(t)
                T16.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T17":
                intabel.remove(t)
                out.append(t)
                T17.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T18":
                intabel.remove(t)
                out.append(t)
                T18.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T19":
                intabel.remove(t)
                out.append(t)
                T19.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T20":
                intabel.remove(t)
                out.append(t)
                T20.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T21":
                intabel.remove(t)
                out.append(t)
                T21.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T22":
                intabel.remove(t)
                out.append(t)
                T22.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T23":
                intabel.remove(t)
                out.append(t)
                menu()
                T23.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T24":
                intabel.remove(t)
                out.append(t)
                T24.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T25":
                intabel.remove(t)
                out.append(t)
                menu()
                T25.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T26":
                intabel.remove(t)
                out.append(t)
                T26.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T27":
                intabel.remove(t)
                out.append(t)
                T27.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T28":
                intabel.remove(t)
                out.append(t)
                T28.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T29":
                intabel.remove(t)
                out.append(t)
                T29.append(Timeadd)
                print(Timein)
                menu()
            elif t == "T30":
                intabel.remove(t)
                out.append(t)
                T30.append(Timeadd)
                print(Timein)
                menu()
            else:
                os.system("cls")
                menu()
        except:
            os.system("cls")
            print("If putting the proposal str or not clear ")
            menu()

    def pay():  
        try:
            print("1 จ่ายสด")
            print("2 จ่ายบัตร")
            print("3 จ่ายบัตร")
            c = input("Add a number table entry:")
            if c == "1":
                os.system("cls")
                print("จ่ายสด")
                paymoney()

            elif c == "2":
                os.system("cls")
                print("จ่ายบัตร")
                paycrad()
            elif c == "3":
                os.system("cls")
                menu()    

            else:
                os.system("cls")
                menu()
        except:
            print("เลือกเอาจะจ่ายด้วยอะไร")
            menu()
    
    menu()
main()
