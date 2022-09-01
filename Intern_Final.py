import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import PyPDF2
from fpdf import FPDF
import tkinter.font as font
from csv import DictWriter
from csv import DictReader
import os

# all inputs are stored in global variable
def all_input_global_variable():  # all inputs are stored in global variables
    global name, mobile, email, age, eligibility, gender
    name = name_input.get().strip()  # takes name input
    mobile = mobile_input.get()  # takes mobile input
    email = email_input.get()  # takes email input
    age = age_spinbox.get()  # takes age values from the input
    eligibility = el_state.get()  # takes eligibility input
    gender = gender_box.get()  # takes gender input

    # eligibility
    if eligibility == 1:
        eligibility = "Eligible"
    elif eligibility == 2:  # ************ if not selected then 0 check it **********
        eligibility = "Not eligible"


# Term And Condition Part
def terms_condition_display():  # displays terms and condition (function for terms and condition checkbox)
    if tc_state.get():
        tk.messagebox.showinfo("Terms & Condition", 'By agreeing terms and condition')  # displays term and condition
        # enables txt, pdf, csv buttons
        get_PDF_button.config(state="normal")
        get_CSV_button.config(state="normal")
        get_TXT_button.config(state="normal")

    else:
        tk.messagebox.showwarning("Error", 'Please agree the term and condition to continue')  # displays warning
        # disables txt, pdf, csv button
        get_PDF_button.config(state="disabled")
        get_CSV_button.config(state="disabled")
        get_TXT_button.config(state="disabled")  #


# validates if user input are correct or nt
def valid_input_check():  # performs on check (function for check button)
    all_input_global_variable()

    # ----------------------------checks the user input ----------------------------#
    if len(name) == 0 or not name.replace(" ", "").isalpha():  # checks if name input is null or contains digit
        tk.messagebox.showerror("ERROR", "Wrong Name Input")
        return 0  # returns 0 for error

    elif len(mobile) != 10 or not mobile.isdigit():
        # checks if mobile input is not 10 or not digit
        tk.messagebox.showerror("ERROR", "Wrong Mobile Input")
        return 0  # returns 0 for error

    elif '@' not in email or len(email) < 5 or (not email.endswith('.com') and not email.endswith('in')):
        # checks if email input does contain @ and whether ends with .com
        tk.messagebox.showerror("ERROR", "Wrong Email Input")
        return 0  # returns 0 for error

    elif int(age) not in range(0, 100):
        # if age is not in range 0 and 100
        tk.messagebox.showerror("ERROR", "Age is not proper \n\nPlease Select a number from 0 to 100")
        return 0  # returns 0 for error

    elif gender not in ["Male", "Female", "Others"]:
        # if age is not from drop menu
        tk.messagebox.showerror("ERROR", "Improper gender selection \n\nPlease Select from drop menu")
        return 0

    else:
        return 1  # return 1 for success


# function for clear button
def on_clear_click():  # performs on clear (function for clear button)
    info_textbox_display.config(state="normal")  # enables textbox to insert data
    info_textbox_display.delete(1.0, tk.END)  # delete data already present in text box
    info_textbox_display.config(state="disabled")  # disables textbox to avoid user input


# displays success message on textbox after data is stored
def success_message_textbox():
    # displays successfully stored message in textbox
    info_textbox_display.config(state="normal")  # enables textbox to insert data
    info_textbox_display.delete(1.0, tk.END)  # delete data already present in text box
    info_textbox_display.insert(tk.END, "The details have been successfully stored")  # inserts all file data in textbox
    info_textbox_display.config(state="disabled")  # disables textbox to avoid user input


# text data
def get_text_data():
    # all inputs are stored in global variable
    all_input_global_variable()

    file_get_txt = open("Info_in_text.txt", "a+")  # opened a file in append mode (creates if does not exits)
    file_get_txt.seek(0)  # goes to first line of file
    file_contents_get_text = file_get_txt.read()  # all file contents are stored in this variable

    if not valid_input_check():
        # it checks if inputs are valid or not
        pass

    elif mobile in file_contents_get_text or email in file_contents_get_text:
        # mobile/ email id is already present in file
        tk.messagebox.showerror("ERROR", "Mobile Number or Email ID already present \n\nPlease Enter Valid Input")

    else:
        # if no problem in input then it will print in the file
        file_get_txt.write("Name :" + name + "\nMob No :" + str(
            mobile) + "\nEmail Id :" + email + "\nAge :" + age + "\nGender :" + gender + "\nEligible :" + eligibility + "\n\n")

        success_message_textbox()


def get_pdf_data():
    # all inputs are stored in global variable
    all_input_global_variable()
    """
    file_get_pdf = "Info_in_pdf.pdf"
    file_get_pdf_reader = PyPDF2.PdfFileReader(file_get_pdf)
    file_get_pdf_page = file_get_pdf_reader.getPage()
    file_get_pdf_text = file_get_pdf_page.extractText()


    if mobile in file_get_pdf_text or email in file_get_pdf_text:
        tk.messagebox.askyesno("Title","Message")
    pass
    """

    # to write in pdf
    write_data_pdf = FPDF()
    write_data_pdf.add_page()
    write_data_pdf.set_font("Arial", size=15)
    write_data_pdf.cell(300, 100, txt=name, ln=2, align="L")
    write_data_pdf.output("Info_in_pdf.pdf")
    success_message_textbox()


# csv data
def get_csv_data():
    all_input_global_variable() # all inputs are declaraed in gloabal variable

    get_csv_file = open("Info_in_csv.csv",'a',newline='') # csv file is called

    get_csv_file_reader = open("Info_in_csv.csv",'r')

    csv_dict_writer = DictWriter(get_csv_file,
                                 fieldnames=['Name', 'Mob No', 'Email Id', 'Age', 'Gender', 'Eligibility'])
    csv_dict_reader = DictReader(get_csv_file_reader)

    error_csv_data_reader = 0 # flag type variable for repeation check

    for row_csv_dict_reader in csv_dict_reader:
        if mobile in row_csv_dict_reader['Mob No'] or email in row_csv_dict_reader['Email Id']:
            error_csv_data_reader = 1 # setting value as 1 for error
            break

    if not valid_input_check(): # check if input is valid
        pass

    elif error_csv_data_reader == 1:     # if error_csv_data_reader == 1 then display error
        tk.messagebox.showerror("ERROR", "Mobile Number or Email Id Already Present")

    else:
        if os.path.getsize("Info_in_csv.csv") == 0: # check if file is empty
            csv_dict_writer.writeheader() # writes the heading

        # enters user data to csv file
        csv_dict_writer.writerow({
            'Name': name,
            'Mob No': mobile,
            'Email Id': email,
            'Age': age,
            'Gender': gender,
            'Eligibility': eligibility})

# check button function
def check_button_function():
    all_input_global_variable()

    if not valid_input_check():
        # it checks if inputs are valid or not
        pass
    else:
        info_textbox_display.config(state="normal")  # enables textbox to insert data
        info_textbox_display.delete(1.0, tk.END)  # delete data already present in text box

        # display user input data in textbox
        info_textbox_display.insert(tk.END,
                                    "Name :" + name + "\nMob No :" + str(
                                        mobile) + "\nEmail Id :" + email + "\nAge :" + age + "\nGender :" + gender + "\nEligible :" + eligibility + "\n\n")  # inserts all file data in textbox

        info_textbox_display.config(state="disabled")  # disables textbox to avoid user input


# GUI Part
r = tk.Tk()
el_state = tk.IntVar()  # for eligible radio button
tc_state = tk.IntVar()  # for terms and condition check box
r.geometry("400x650")
r.title("Registration Form")  # title of frame
r.configure(background="sky blue")  # background color

title_font_style = font.Font(family="Arial", size=15, weight=font.BOLD)  # font style for title
label_font_style = font.Font(family='Helvetica', size=11, weight=font.BOLD)  # font style for label
input_font_style = font.Font(family="Helvetica", size=11, weight=font.NORMAL)  # font style for inputs
button_font_style = font.Font(family="Arial", size=13, weight=font.BOLD)  # button style

# Title label
title_label = tk.Label(r, text="REGISTRATION FORM", bg="black", fg="white", font=title_font_style)  # title label
title_label.place(x=75, y=10)

# Label Part
name_label = tk.Label(r, text="Name", fg="black", bg="sky blue", font=label_font_style)  # name label
name_label.place(x=60, y=60)

mobile_label = tk.Label(r, text="Mobile No.", fg="black", bg="sky blue", font=label_font_style)  # mobile label
mobile_label.place(x=60, y=100)

email_label = tk.Label(r, text="Email ID", fg="black", bg="sky blue", font=label_font_style)  # email id label
email_label.place(x=60, y=140)

age_label = tk.Label(r, text="Age", fg="black", bg="sky blue", font=label_font_style)  # age label
age_label.place(x=60, y=180)

gender_label = tk.Label(r, text="Gender", fg="black", bg="sky blue", font=label_font_style)  # gender label
gender_label.place(x=60, y=220)

# Input Part
name_input = tk.Entry(r, width=15, font=input_font_style)  # name input
name_input.place(x=180, y=60)

mobile_input = tk.Entry(r, width=15, font=input_font_style)  # mobile no input
mobile_input.place(x=180, y=100)

email_input = tk.Entry(r, width=15, font=input_font_style)  # email input
email_input.place(x=180, y=140)

# eligibility input
eligible1_radio = tk.Radiobutton(r, text="Eligible", variable=el_state, value=1, bg="sky blue",
                                 font=label_font_style)
eligible1_radio.place(x=60, y=260)
eligible2_radio = tk.Radiobutton(r, text="Not Eligible", variable=el_state, value=2, bg="sky blue",
                                 font=label_font_style)
eligible2_radio.place(x=200, y=260)
el_state.set(1)  # initially it would be set at eligible condition

# term & condition
agreement_checkbox = tk.Checkbutton(r, text="Agree to Terms and Conditions", variable=tc_state,
                                    command=terms_condition_display, font=label_font_style)
# active background
agreement_checkbox.place(x=60, y=310)

age_spinbox = tk.Spinbox(r, from_=0, to=100, width=18)  # age input
age_spinbox.place(x=180, y=180)

gender_box = ttk.Combobox(r, width="17", values=["Male", "Female", "Others"])  # age input
gender_box.place(x=180, y=220)

# buttons
get_TXT_button = tk.Button(r, text="TEXT", bg="sky blue",
                           font=button_font_style, state="disabled", command=get_text_data)  # to view txt data
get_TXT_button.place(x=60, y=350)

get_PDF_button = tk.Button(r, text="PDF", command=get_pdf_data, bg="sky blue", state="disabled",
                           font=button_font_style)  # to view pdf data
get_PDF_button.place(x=170, y=350)

get_CSV_button = tk.Button(r, text="CSV", command=get_csv_data, bg="sky blue", state="disabled",
                           font=button_font_style)  # to view csv data
get_CSV_button.place(x=260, y=350)

check_button = tk.Button(r, text="CHECK", command=check_button_function, bg="black", fg="white",
                         font=button_font_style)  # submit button
check_button.place(x=60, y=600)

clear_button = tk.Button(r, text="CLEAR", command=on_clear_click, bg="black", fg="white",
                         font=button_font_style)  # submit button
clear_button.place(x=240, y=600)

# text box ********************* scroll bar problem *************************
info_textbox_display = tk.Text(r, width=31, height=10, state="disabled")
info_textbox_display.place(x=60, y=400)

info_textbox_scrollbar = tk.Scrollbar(r, command=info_textbox_display.yview, orient="vertical")
info_textbox_scrollbar.config(command=info_textbox_display.yview)

info_textbox_display.config(yscrollcommand=info_textbox_scrollbar.set)
# info_textbox_display.pack(side="left", fill="both", expand='NO')
info_textbox_scrollbar.pack(side="right", fill="both")

r.resizable(0, 0)  # to disable minimize and maximize
r.mainloop()
