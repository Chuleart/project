import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

def on_click():
   try:
      score = tv_grade.get() 
      if score > 101:
         messagebox.showinfo("Error ʕ•ᴥ•ʔ", "Enter the number before 100 or more")
      elif score>=80 and score<=100:
         print('คะแนน',score,'ได้เกรด 4')
         total=Label(root, text="ได้เกรด 4.0")
         total.grid(row=2, column=2, sticky=W)
      elif score>=75 and score<=79:
         print('คะแนน',score,'ได้เกรด 3.5')
         total=Label(root, text="ได้เกรด 3.5")
         total.grid(row=2, column=2, sticky=W)
      elif score>=70 and score<=74:
         print('คะแนน',score,'ได้เกรด 3')
         total=Label(root, text="ได้เกรด 3.0")
         total.grid(row=2, column=2, sticky=W)
      elif score>=65 and score<=69:
         print('คะแนน',score,'ได้เกรด 2.5')
         total=Label(root, text="ได้เกรด 2.5")
         total.grid(row=2, column=2, sticky=W)
      elif score>=60 and score<=64:
         print('คะแนน',score,'ได้เกรด 2')
         total=Label(root, text="ได้เกรด 2.0")
         total.grid(row=2, column=2, sticky=W)
      elif score>=55 and score<=59:
         print('คะแนน',score,'ได้เกรด 1.5')
         total=Label(root, text="ได้เกรด 1.5")
         total.grid(row=2, column=2, sticky=W)
      elif score>=50 and score<=54:
         print('คะแนน',score,'ได้เกรด 1')
         total=Label(root, text="ได้เกรด 1.0")
         total.grid(row=2, column=2, sticky=W)
      elif score>=1 and score<=49:
         print('คะแนน',score,'ได้เกรด 0.0')
         total=Label(root, text="ได้เกรด 0")
         total.grid(row=2, column=2, sticky=W)
      else:
         print("again Please")
         messagebox.showinfo("Error ʕ•ᴥ•ʔ", "Enter the number after 1 or more")
   except:
      messagebox.showinfo("Error ʕ•ᴥ•ʔ", "Try again Please ʕ•ᴥ•ʔ ")
def reset():
   Label(root, text='ได้เกรด 0.0').grid(row=2, column=2, sticky=W)
   tv_grade.set(0) 

root = Tk()
root.option_add("*Font", "bold 20")
root.title("Cutting grade ʕ•ᴥ•ʔ")
root.geometry("300x100")

tv_grade = DoubleVar()
tv_grade.set(0) 
tv_total = StringVar  

Label(root, text='เกรด').grid(row=0, column=0, sticky=W)
Entry(root, textvariable=tv_grade,width=5, justify="center").grid(row=0, column=2)
Label(root, text='คำตอบ').grid(row=2, column=0, sticky=W)

l1=Button(root, text=" Print Total ", command=on_click)
l1.grid(row=3, column=1, sticky=W)

Label(root, text='ได้เกรด 0.0').grid(row=2, column=2, sticky=W)

l2=Button(root, text=" Reset ", command=reset)
l2.grid(row=3, column=2, sticky=W)

root.mainloop() 
