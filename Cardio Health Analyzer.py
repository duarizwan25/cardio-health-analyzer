from tkinter import *
from tkinter import messagebox
import random
import string
import csv
from PIL import Image,ImageTk
import smtplib
import os
import datetime
root = Tk()
root.geometry("1400x800")
root.title("profile")
def create_4th_page(disease):
    for widget in root.winfo_children():
        widget.destroy()

    root.config(bg=None)
    imge = Image.open("4thpage.png")
    imge = imge.resize((1400, 800))
    bk = ImageTk.PhotoImage(imge)

    Ll1 = Label(root, image=bk)
    Ll1.image = bk
    Ll1.place(x=0, y=0, relwidth=1, relheight=1)

    def send_prescription():
        global username
        global password
        global l
        email = email_e.get()


        subject = "Your Prescription for disease"
        message = f"Dear Patient,\n\nHere is your prescription for disease:\n\n{prescription}\n\nPlease follow the instructions provided by your healthcare provider.\n\nRegards,\nHospital Team"

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login("hospitalour6@gmail.com", "pbnb tkqo bfup arhp")
                smtp.sendmail("hospitalour6@gmail.com", email, f"Subject: {subject}\n\n{message}.")
            messagebox.showinfo("Prescription Sent", "The prescription has been sent to your email.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send prescription: {str(e)}")


    lb3 = Label(root, text="==========================")
    lb3.place(relx=0.4, rely=0.05)
    p_label = Label(root, text="PRESCRIPTION", fg='red', bg='black', font=("Helvetica", 15))
    p_label.place(relx=0.42, rely=0.1)
    lb4 = Label(root, text="==========================")
    lb4.place(relx=0.4, rely=0.15)

    d = disease.split()
    q = "No diseases match the selected symptoms."
    folder_path = r'C:\Users\Administrator\PycharmProjects\pythonProject2\Textfiles'
    def file_search(dir):
        file_names = os.listdir(dir)

        for file_name in file_names:
            file_path = f'{os.path.abspath(os.path.join(dir, file_name))}'
            with open(file_path, 'r') as f:
                lines = f.read()
                for i in d:
                    if i == "Heart" in d:
                        if "Heart" in lines:
                            with open("prescription.txt", 'a') as file:
                                file.write(f"{lines}\n")
                    else:
                        pass

        for file_name in file_names:
            file_path = f'{os.path.abspath(os.path.join(dir, file_name))}'
            with open(file_path, 'r') as f:
                lines = f.read()
                for i in d:
                    if i == "Valve" in d:
                        if "Valve" in lines:
                            with open("prescription.txt", 'a') as file:
                                file.write(f"{lines}\n")
                    else:
                        pass

        for file_name in file_names:
            file_path = f'{os.path.abspath(os.path.join(dir, file_name))}'
            with open(file_path, 'r') as f:
                lines = f.read()
                for i in d:
                    if i == "Vein" in d:
                        if "Vein" in lines:
                            with open("prescription.txt", 'a') as file:
                                file.write(f"{lines}\n")
                    else:
                        pass

        for file_name in file_names:
            file_path = f'{os.path.abspath(os.path.join(dir, file_name))}'
            with open(file_path, 'r') as f:
                lines = f.read()
                for i in d:
                    if i == "Stroke" in d:
                        if "Stroke" in lines:
                            with open("prescription.txt", 'a') as file:
                                file.write(f"{lines}\n")
                    else:
                        pass
        #
        for file_name in file_names:
            file_path = f'{os.path.abspath(os.path.join(dir, file_name))}'
            with open(file_path, 'r') as f:
                lines = f.read()
                for i in d:
                    if i == "Rhythm" in d:
                        if "Rhythm" in lines:
                            with open("prescription.txt", 'a') as file:
                                file.write(f"{lines}\n")
                    else:
                        pass
        for file_name in file_names:
            file_path = f'{os.path.abspath(os.path.join(dir, file_name))}'
            with open(file_path, 'r') as f:
                lines = f.read()
                for i in d:
                    if i == "ALHAMDULLILAH!" in d:
                        if "ALHAMDULLILAH!" in lines:
                            with open("prescription.txt", 'a') as file:
                                file.write(f"{lines}\n")
                    else:
                        pass

    file_search(folder_path)
    with open("prescription.txt", 'r') as f:
        prescription = f.read()
        prescription_label = Label(root, text=prescription, wraplength=400, justify=LEFT)
        prescription_label.place(relx=0.4,rely=0.25)
        with open('data.txt','a') as file:
            file.write(f'\n{prescription}')

    # button for prescription
    send_prescription_button = Button(root, text="Send Prescription",bg='blue',fg="white", command=lambda: send_prescription())
    send_prescription_button.place(relx=0.52,rely=0.5)

    os.remove('prescription.txt')

    #email input
    email_l = Label(root, text="Enter your email id", bg="red", fg='white')
    email_l.place(relx=0.4, rely=0.4)
    email_e = Entry(root, width=25)
    email_e.place(relx=0.5, rely=0.4)


symptoms_to_diseases = {
    "Stroke": ["weakness and numbness", "speech problems", "confusion", "loss of coordination/balance",
               "visual changes"],
    "Heart failure": ["insomnia", "pain", "mood disturbances", "cognitive dysfunction", "nausea", "palpitations",
                      "pain below the ribs", "nervousness", "edema/excess fluid retention", "sweating"],
    "Valve disease": ["Stenosis", "Prolapse", "Atresia", "pulmonary hypertension"],
    "Rhythm disorders": ["fatigue", "shortness of breath", "dizziness", "chest pain",
                         "feeling faint or sudden loss of blood pressure", "anxiety"],
    "Vein and artery disease": ["leg pain", "aching","heaviness", "cramping", "tightness",
                                "restless legs syndrome", "skin irritation"]
}

selected_symptoms = []

background_image = None

def create_3rd_page():
        global background_image
        global l1_3rd_page
        global identify_button_3rd_page
        global symptoms_frame
        global next_button

        for widget in root.winfo_children():
            widget.destroy()

        root.title("Disease Identifier")
        root.config(bg='dark grey')

        if background_image is None:
            img = Image.open("bg.jpeg")
            img = img.resize((1400, 800))
            background_image = ImageTk.PhotoImage(img)

        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        symptoms_frame = Frame(root, bg='pink')
        symptoms_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        num_rows = 11
        num_columns = 2

        row_num = 0
        column_num = 0
        for disease, symptoms in symptoms_to_diseases.items():
            for symptom in symptoms:
                symptom_var = BooleanVar()
                symptom_var.set(False)

                def create_toggle(symptom=symptom):
                    return lambda: toggle_symptom(symptom)

                Checkbutton(symptoms_frame, text=symptom, bg='#87CEEB', fg='black', variable=symptom_var,
                            command=create_toggle(symptom)).grid(row=row_num, column=column_num, sticky="w")

                row_num += 1
                if row_num >= num_rows and column_num < num_columns:
                    row_num = 0
                    column_num += 1

        identify_button_3rd_page = Button(root, text="Identify Disease", bg="blue", fg="white", width=12,
                                          command=identify_disease)
        identify_button_3rd_page.place(relx=0.5, rely=0.7, anchor=CENTER)

        def next_command():
            # Your logic for next command
            pass


        # try:
        #     if s.get() != " ":
        #         messagebox.showerror("Error",'Select at least one disease')
        #     else:
        #         S = destroy_3rd_page()
        #
        # except Exception as e:
        #     messagebox.showerror("Error",'Select at least one disease')
        #
        # next_button = Button(root, text="Next",command=S, width=12, bg='blue', fg='white')
        # next_button.place(relx=0.5, rely=0.8, anchor=CENTER)
def toggle_symptom(symptom):
    if symptom in selected_symptoms:
       selected_symptoms.remove(symptom)
    else:
        selected_symptoms.append(symptom)

def identify_disease():
    if not selected_symptoms:

        messagebox.showinfo("No Symptoms Selected", "Please select at least one symptom.")
        return

    matching_diseases = []
    perfect_match = False
    for disease, symptoms in symptoms_to_diseases.items():
        if all(symptom in selected_symptoms for symptom in symptoms):
            perfect_match = True
            matching_diseases.insert(0, disease)
        elif sum(symptom in selected_symptoms for symptom in symptoms) >= 3:
            matching_diseases.append(disease)
    global s
    s = StringVar()
    if perfect_match:

        s.set(f"The patient most likely has {matching_diseases[0]} based on the selected symptoms.")
        messagebox.showinfo("Diagnosis",s.get())
        if s.get() == "":
            messagebox.showerror("Error","sjdhf")
    elif matching_diseases:
        s.set(f"The patient may be at risk of the following diseases based on the selected symptoms:\n{', '.join(matching_diseases)}")
        messagebox.showinfo("Potential Diseases",s.get())
        if s.get() == "":
            messagebox.showerror("Error","sjdhf")
    else:
        s.set("No diseases match the selected symptoms. ALHAMDULLILAH!")
        messagebox.showinfo("No Match",s.get())
        if s.get() == "":
            messagebox.showerror("Error","sjdhf")

    next_button = Button(root, text="Next", command=destroy_3rd_page, width=12, bg='blue', fg='white')
    next_button.place(relx=0.5, rely=0.8, anchor=CENTER)

def destroy_3rd_page():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    button.destroy()
    label4.destroy()
    label5.destroy()
    label_weight.destroy()
    height_dropdown.destroy()
    weight_dropdown.destroy()
    e1.destroy()
    e2.destroy()
    a.destroy()
    b.destroy()
    l1.destroy()
    button1.destroy()
    identify_button_3rd_page.destroy()
    symptoms_frame.destroy()
    create_4th_page(s.get())

    def go_back():
        root.withdraw()
        os.system('python "C:\\Users\\Administrator\\PycharmProjects\\pythonProject2\\kivy.py"')
        root.destroy()

    # back button
    back_button = Button(root, text="Back", font=("Arial", 10), bg="blue", fg="white", width=10, command=go_back)
    back_button.place(relx=0.42, rely=0.5)



def create_2nd_page():

    global l1
    global my_text
    global button1

    root.title("Disease Identifier")
    root.geometry('1500x800')

    img = Image.open("pg2.jpg")
    img = img.resize((1500, 800))
    bg = ImageTk.PhotoImage(img)

    l1 = Label(root, image=bg)
    l1.image = bg
    l1.place(x=0, y=0, relwidth=1, relheight=1)

    button1 = Button(root, text="Hello Dear! CLICK ME and Tell me the symptoms", bg="black", fg='grey', font=('Helvetica', 15),
                     command=destroy_2nd_page)
    button1.place(relx=0.2, rely=0.8, anchor=CENTER)

def destroy_2nd_page():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    button.destroy()
    label4.destroy()
    label5.destroy()
    label_weight.destroy()
    height_dropdown.destroy()
    weight_dropdown.destroy()
    e1.destroy()
    e2.destroy()
    a.destroy()
    b.destroy()
    l1.destroy()
    button1.destroy()

    create_3rd_page()


def destroy_1st_page():
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    label_weight.destroy()
    height_dropdown.destroy()
    weight_dropdown.destroy()
    button.destroy()
    e1.destroy()
    e2.destroy()
    a.destroy()
    b.destroy()
    lll1.destroy()
    create_2nd_page()


def login():
    p_name = e1.get().strip()
    Patient_name = p_name
    Patient_age = e2.get()
    Patient_gender = r.get()
    Patient_weight = weight_var.get()
    Patient_height = height_var.get()
    if Patient_name == "" and Patient_age == "" and Patient_gender == "":
        messagebox.showerror("Error", "Blank not allowed")
    elif Patient_name == "":
        messagebox.showinfo("Error", "please enter your name!")
    elif Patient_age == "":
        messagebox.showinfo("Error", "please enter your age")
    elif Patient_gender not in [1,2]:
        messagebox.showinfo('Error', 'Please select a gender')
    elif not all(x.isalpha() or x.isspace() for x in Patient_name):
        messagebox.showinfo("Error", "Patient name should contain only alphabets")
    elif not Patient_age.isdigit():
        messagebox.showinfo("Error", 'Age should only contain digits')
    elif len(Patient_name) < 3:
        messagebox.showerror("error","Name should contain at least 3characters")
    elif int(Patient_age) <= 0 or int(Patient_age) >= 100:
        messagebox.showerror("Error","Age should be in between 0 and 100")
    else:
        user = ["-- USER_INTERFACE --"]
        user_input = [
            f"| Patient Name: {Patient_name}|\n| Patient Age: {Patient_age} |\n| Patient Gender: {Patient_gender} |\n| Patient Weight: {Patient_weight}|\n"
            f"| Patient Height: {Patient_height}|\n""-----------------------"
        ]

        with open("data.txt","w") as f:
            f.write(f' Patient_name: {Patient_name} ')
            f.write(f'\n Patient_age: {Patient_age}')

        x = datetime.datetime.now()
        with open("hospital_record.csv", "a", newline="") as hospital:
            record = csv.writer(hospital)
            record.writerow([x.strftime("%Y-%m-%d %H:%M:%S"), Patient_name, Patient_age, Patient_gender, Patient_height,
                             Patient_weight])
        messagebox.showinfo("WElCOME", "Thank you for choosing our facility. We're here to provide care.")
        # # x = datetime.datetime.now()
        # with open("hospital_record.csv", "a", newline="") as hospital:
        #     record = csv.writer(hospital)
        #     record.writerow([Patient_name, Patient_age, Patient_gender, Patient_height, Patient_weight])
        # messagebox.showinfo("WElCOME", "Thank you for choosing our facility. We're here to provide care.")
        destroy_1st_page()


global pg1_pic
global button1

img_1 = Image.open("pg1.jpg")
img_1 = img_1.resize((1500, 800))
bg_1 = ImageTk.PhotoImage(img_1)

lll1 = Label(root, image=bg_1)
lll1.image = bg_1
lll1.place(x=0, y=0, relwidth=1, relheight=1)

# heading for login page
label1 = Label(root, text="Patient Profile",fg="red",width=15, font=('Bradley Hand ITC', 30))
label1.place(relx=0.2, rely=0.1, anchor='center')

# Weight options
weights = ["50 kg", "60 kg", "70 kg", "80 kg", "90 kg"]
weight_var = StringVar(root)
weight_var.set(weights[0])
weight_dropdown = OptionMenu(root, weight_var, *weights)
weight_dropdown.place(relx=0.2, rely=0.65,anchor='center')

# Height options
heights = ["150 cm", "160 cm", "170 cm", "180 cm", "190 cm"]
height_var = StringVar(root)
height_var.set(heights[0])
height_dropdown = OptionMenu(root, height_var, *heights)
height_dropdown.place(relx=0.2, rely=0.55,anchor='center')

# name of patient
label2 = Label(root, text="Patient Name:", bg="red",width=15,fg="white")
label2.place(relx=0.1, rely=0.2,anchor='center')

# AGe of patient
label3 = Label(root, text="Patient's Age:", bg="red",width=15, fg="white")
label3.place(relx=0.1, rely=0.3,anchor='center')

# Patient's gender
label4 = Label(root, text="Patient's gender:", bg="red",width=15, fg="white")
label4.place(relx=0.1, rely=0.4,anchor='center')

# height of patient
label5 = Label(root, text="Patient's Height:", bg='red',width=15,fg='white')
label5.place(relx=0.1, rely=0.55,anchor='center')

# weight of patient
label_weight = Label(root, text="Weight:", bg='red',width=15,fg='white')
label_weight.place(relx=0.1, rely=0.65,anchor='center')

# Entry for name
e1 = Entry(root,width=20)
e1.place(relx=0.2, rely=0.2,anchor='center')
# entry for age
e2 = Entry(root,width=20)
e2.place(relx=0.2, rely=0.3,anchor='center')

# radio buttons
r = IntVar()
a = Radiobutton(root, text="MALE", variable=r, value=1, fg='orange',width=10)
a.place(relx=0.2, rely=0.4,anchor='center')
b = Radiobutton(root, text="FEMALE", variable=r, value=2, fg='orange',width=10)
b.place(relx=0.2, rely=0.45,anchor='center')

button = Button(root, text="Done", command=login, fg='yellow', bg="blue", width=10)
button.place(relx=0.2, rely=0.75,anchor='center')


root.mainloop()

