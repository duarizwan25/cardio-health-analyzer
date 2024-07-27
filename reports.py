from tkinter import *
import os
root = Tk()
root.geometry("1400x800")
root.config(bg="black")
with open('data.txt', 'r') as f:
    data3 = f.read()
    reports_page = Label(root, text=f'Here are your reports:\n {data3}')
    reports_page.place(relx=0.3, rely=0.1)

def go_back():
    root.withdraw()
    os.system('python "kivy.py"')
    root.destroy()


# back button
back_button=Button(root,text="Back",font=("Arial", 15),width=15, bg="blue", fg="black",command=go_back)
back_button.place(relx=0.37,rely=0.4)
root.mainloop()