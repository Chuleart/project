import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

#ดึงข้อมูลของ Tkinter

def on_click():
   #เมือกดฟังชันจะเริ้มทำงาน
   try:
      # try สร้างการเปรียบเทียบอะไรทีไม่ใช้ จากฟังชันหรือไม่ได้สร้างไว้จะไม่ error ใน Terminal แต่จะลงไปใน except เพือสร้าง popup
      score = tv_grade.get() 
      #ให้ tv = score และเปรียบเทียบค่า
      if score > 101:
         messagebox.showinfo("Error ʕ•ᴥ•ʔ", "Enter the number before 100 or more")
      elif score>=80 and score<=100:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 4')
         tv_total=Label(root, text="ได้เกรด 4.0")
         tv_total.grid(row=2, column=2, sticky=W)
         
      elif score>=75 and score<=79:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 3.5')
         tv_total=Label(root, text="ได้เกรด 3.5")
         tv_total.grid(row=2, column=2, sticky=W)

      elif score>=70 and score<=74:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 3')
         tv_total=Label(root, text="ได้เกรด 3.0")
         tv_total.grid(row=2, column=2, sticky=W)

      elif score>=65 and score<=69:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 2.5')
         tv_total=Label(root, text="ได้เกรด 2.5")
         tv_total.grid(row=2, column=2, sticky=W)

      elif score>=60 and score<=64:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 2')
         tv_total=Label(root, text="ได้เกรด 2.0")
         tv_total.grid(row=2, column=2, sticky=W)

      elif score>=55 and score<=59:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 1.5')
         tv_total=Label(root, text="ได้เกรด 1.5")
         tv_total.grid(row=2, column=2, sticky=W)

      elif score>=50 and score<=54:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 1')
         tv_total=Label(root, text="ได้เกรด 1.0")
         tv_total.grid(row=2, column=2, sticky=W)
         
      elif score>=1 and score<=49:
         os.system("cls")
         print('คะแนน',score,'ได้เกรด 0')
         tv_total=Label(root, text="ได้เกรด 0.0")
         tv_total.grid(row=2, column=2, sticky=W)
         
      else:
         print("again Please")
         messagebox.showinfo("Error ʕ•ᴥ•ʔ", "Enter the number after 1 or more")
   except:
      messagebox.showinfo("Error ʕ•ᴥ•ʔ", "Try again Please ʕ•ᴥ•ʔ ")
      #ในกรณีที่มีข้อผิดพลาดจะเข้ามาใน except เพือให้ messagebox สร้าง popup มาแจ้งเตือน
def reset():
   #ฟังชัน การ Reset 
   total = Label(root, text='ได้เกรด 0')
   total.grid(row=2, column=2, sticky=W)
   grade.delete(0, END)
   tv_grade.set(0) 
   #สร้างค่าเดิมให้กลายเป็น 0
   os.system("cls")

root = Tk()
root.option_add("*Font", "bold 20")
root.title("Cutting grade ʕ•ᴥ•ʔ")
root.geometry("300x100")
#คำสังการสร้าง Frame Tk ให้กับ window
tv_grade = DoubleVar()
tv_grade.set(0) 
#สร้างค่าเริมต้นให้เป็น 0
tv_total = DoubleVar() 
#สร้างตัวแปลในการเก็บข้อมูล 
Label(root, text='เกรด' ).grid(row=0, column=0, sticky=W)
#สร้างตัวหนังสือที่ชือว่า เกรด
grade =Entry(root, textvariable=tv_grade,width=5, justify="center")
grade.grid(row=0, column=2)
Label(root, text='คำตอบ').grid(row=2, column=0, sticky=W)
#สร้าง ตัวกรอกข้อมูล ให้ไปเก็บค่าที tv_grade
l1=Button(root, text=" Print Total ", command=on_click)
l1.grid(row=3, column=1, sticky=W)

Label(root, text='ได้เกรด 0').grid(row=2, column=2, sticky=W)

l2=Button(root, text=" Reset ", command=reset)
l2.grid(row=3, column=2, sticky=W)
#ปู๋มต่างๆๆ
root.mainloop() 
#การ loop ของโปรแกรม
