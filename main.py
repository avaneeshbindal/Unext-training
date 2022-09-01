import tkinter as tk
from tkinter import messagebox


#File Handling
def _file():
    f= open("Info.txt", "a+")
    a= "\n\nName="+entry1.get()+"\nMob No.="+entry2.get()+"\nAddress="+entry3.get()+"\nEmail Id="+entry4.get()+"\n\n\n"
    f.write(a)

def _readinfo():
    f= open("Info.txt", "r+")
    contents= (f.read())
    print("The info", contents)




# check_function
def _contactcheck():
    contact1 = entry2.get()
    if len(contact1) == 10 and contact1.isdigit():
        _addresscheck()
        pass
    else:
        _errorshow()


def _namecheck():
    name1 = entry1.get()
    if len(name1) != 0 and (name1.isalpha()):
        _contactcheck()
        pass
    else:
        _errorshow()


def _emailcheck():
    email1 = entry4.get()

    if "@" in email1 and len(email1) >= 5 and (email1.endswith('com') or email1.endswith('in')):
        _output()
        pass
    else:
        _errorshow()


def _addresscheck():
    address1 = entry3.get()

    if len(address1) != 0:
        _emailcheck()
        pass
    else:
        _errorshow()


# error display function
def _errorshow():
    tk.messagebox.showwarning("ERROR", "Enter Some Proper Values")


# onclick function
def _onclick():
    _namecheck()


# OUTPUT DISPLAY
def _output():
    print("Name=", entry1.get(), "\nMob No.=", entry2.get(), "\nAddress=", entry3.get(), "\nEmail Id=", entry4.get())
    _file()

# GUI
r = tk.Tk()
r.geometry("500x200")
r.title("MPillai____REGISTRATION FORM____")

head = tk.Label(r, text="REGISTRATION FORM", bg="black", fg="white")
head.grid(row=0, column=2)

label1 = tk.Label(r, text='Name', width=23, fg="red")
label1.grid(row=1, column=0)

label2 = tk.Label(r, text='Mob No.', width=20, fg="red")
label2.grid(row=4, column=0)

label3 = tk.Label(r, text='Address', width=23, fg="red")
label3.grid(row=7, column=0)

label3 = tk.Label(r, text='Email ID', width=20, fg="red")
label3.grid(row=10, column=0)

entry1 = tk.Entry(r, text="Enter Your Name", fg="blue")
entry1.grid(row=1, column=3)

entry2 = tk.Entry(r, text="Enter Your Mobile No.", fg="blue")
entry2.grid(row=4, column=3)

entry3 = tk.Entry(r, text="Enter Your Address", fg="blue")
entry3.grid(row=7, column=3)

entry4 = tk.Entry(r, text="Enter Your Email Id.", fg="blue")
entry4.grid(row=10, column=3)

button1 = tk.Button(r, text="Submit", fg="Black", bg="green", command=_onclick)
button1.grid(row=11, column=1)

button2 = tk.Button(r, text="Close", fg="Black", bg="green", command=r.destroy)
button2.grid(row=11, column=3)

button3= tk.Button(r, text="All Info", fg="Black", bg="green", command=_readinfo)
button3.grid(row=12,column=2)
r.resizable(0, 0)
r.mainloop()
