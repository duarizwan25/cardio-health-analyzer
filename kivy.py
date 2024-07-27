import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkcalendar import Calendar  # Import the Calendar widget

root = tk.Tk()
root.geometry("1400x800")
root.title("MedicalMagic")
root.configure(bg="#000000")

width = root.winfo_width()
height = root.winfo_height()
print(width, height)


def calender_command():
    # Create a top-level window for the calendar
    calendar_window = tk.Toplevel(root)
    calendar_window.title("Calendar")

    # Function to retrieve the selected date
    def get_selected_date():
        selected_date = cal.selection_get()
        messagebox.showinfo("Selected Date", f"Selected Date: {selected_date}")

    # Create a Calendar widget
    cal = Calendar(calendar_window, selectmode="day", date_pattern="yyyy-mm-dd", foreground="white",
                   background="black", bordercolor="white", headersbackground="black", headersforeground="white",
                   normalbackground="black", normalforeground="white", weekendbackground="black",
                   weekendforeground="red")
    cal.pack(padx=20, pady=20)

    # Create a button to get the selected date
    get_date_button = tk.Button(calendar_window, text="Get Selected Date", command=get_selected_date,
                                bg="blue", fg="white")
    get_date_button.pack(pady=10)


# Create a frame for the left sidebar
left_frame = tk.Frame(root, width=550, bg="#222222", padx=20, pady=20)
left_frame.grid(row=0, column=0, sticky="ns")

# Create labels and buttons for the left sidebar
title_label = tk.Label(left_frame, text="Medical Magic", font=("Arial", 16, "bold"), fg="white", bg="#222222")
title_label.grid(row=0, column=0, pady=10)

def dashboard_command():
    root.withdraw()
    os.system('python "Cardio Health Analyzer.py"')
    root.destroy()

def reports_command():
    root.withdraw()
    os.system('python "reports.py"')
    root.destroy()

def chat_command():
    root.withdraw()
    os.system('python "chatbot.py"')
    root.destroy()

dashboard_button = tk.Button(left_frame,text="Dashboard",bg="blue",fg="white",width=15,command=dashboard_command)
dashboard_button.grid(row=1,column=0,pady=10)
reports_button = tk.Button(left_frame,text="Reports",bg='blue',fg='white',width=15,command=reports_command)
reports_button.grid(row=2,column=0,pady=10)
calender_button = tk.Button(left_frame,text="Calendar",width=15,bg='blue',fg='white',command=calender_command)
calender_button.grid(row=3,column=0,pady=10)
chat_button = tk.Button(left_frame,text="Chatbot",width=15,bg='blue',fg='white',command=chat_command)
chat_button.grid(row=4,column=0,pady=10)
main_frame = tk.Frame(root, bg="#000000", padx=10, pady=10)
main_frame.grid(row=0, column=1, sticky="nsew")

title_label = tk.Label(main_frame, text="Check your Overall Health", font=("Arial", 24, "bold"), fg="white",
                       bg="#000000")
title_label.grid(row=0, column=0, columnspan=4, pady=10)

heart_image = Image.open("heart.png")
heart_photo = ImageTk.PhotoImage(heart_image)
heart_label = tk.Label(main_frame, image=heart_photo)
heart_label.grid(row=1, column=0, rowspan=4, padx=10, pady=10)

health_frame = tk.Frame(main_frame, bg="#000000", borderwidth=2, relief="groove", padx=10, pady=10)
health_frame.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=10)

health_data = [
    ("Blood Status", "112/75"),
    ("Heart Rate", "120 bpm"),
    ("Blood Count", "79-92"),
    ("Glucose", "162/ml")
]

for i, (label_text, value_text) in enumerate(health_data):
    label = tk.Label(health_frame, text=label_text, font=("Arial", 14, "bold"), fg="white", bg="#005cbf", padx=10,
                     pady=5)
    label.grid(row=i, column=0, sticky="ew")

    value = tk.Label(health_frame, text=value_text, font=("Arial", 14), fg="white", bg="#777777", padx=10, pady=5)
    value.grid(row=i, column=1, sticky="ew")

    mg = Image.open("4thpage.png")
    mg = mg.resize((300,400))
    bk = ImageTk.PhotoImage(mg)

appointments = [
    ("Go for health screening", "Have your blood pressure, blood", "cholesterol and glucose level checked"),
    ('Maintain a healthy weight', 'Excess weight increases your risk to', 'cardiovascular diseases and diabetes also'),
    ('Exercise Aim for 150-300 minutes', 'of moderate intensity aerobics', 'physical activity per week.')
]

for i, (doctor, appointment, date) in enumerate(appointments):
    frame = tk.Frame(main_frame, bg="#000000", borderwidth=2, relief="groove", padx=10, pady=10)
    frame.grid(row=i + 1, column=3, sticky="ew", pady=5)

    doctor_label = tk.Label(frame, text=doctor, font=("Arial", 14, "bold"), fg="white", bg="#ffa500", padx=10, pady=5)
    doctor_label.grid(row=0, column=0, sticky="ew")

    appointment_label = tk.Label(frame, text=appointment, font=("Arial", 14), fg="white", bg="#777777", padx=10, pady=5)
    appointment_label.grid(row=1, column=0, sticky="ew")

    date_label = tk.Label(frame, text=date, font=("Arial", 12), fg="white", bg="#777777", padx=10, pady=5)
    date_label.grid(row=2, column=0, sticky="ew")

root.mainloop()

