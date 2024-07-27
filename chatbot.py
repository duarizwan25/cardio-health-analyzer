import tkinter as tk
from tkinter import ttk
import webbrowser
import os
def open_link(event):
    webbrowser.open("https://poe.com/Bot64BJXXIKBL")

# Create the Tkinter window
root = tk.Tk()
root.title("Link Example")
root.geometry("1400x800")
root.config(bg="black")
# Create a label with a hyperlink style
link_label = ttk.Label(root, text="Click me to chat", cursor="hand2", foreground="black",font=("Helvetica",20))
link_label.place(relx=0.2,rely=0.2)

def go_back():
    root.withdraw()
    os.system('python "kivy.py"')
    root.destroy()


# Bind the label to the function to open the link
link_label.bind("<Button-1>", open_link)
back_button=tk.Button(root,text="Back",font=("Arial", 15),width=15, bg="blue", fg="black",command=go_back)
back_button.place(relx=0.37,rely=0.4)
# Run the Tkinter event loop
root.mainloop()
