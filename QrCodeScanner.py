import pyqrcode
import png
from tkinter import *
from tkinter import messagebox
from sqlalchemy import false



# This Function is responsible to take the input -> Convert it to Image Code -> Convert Image code to png.
def get_code():
    name_var = name.get() 
    age_var = age.get()
    phone_var = phone.get()
    address_var = address.get()
    url_var = url.get()
    qr = pyqrcode.create(str(f"Name is : {name_var}\nAge is :{age_var}\nphone num is :{phone_var} \naddress is :{address_var} \nurl is :{url_var} "))
    qr.png('code.png', scale=4)
    messagebox.showinfo("sucess","Your QR has Sucessfully Created")
    name.set("")
    age.set("")
    phone.set("")
    address.set("")
    url.set("")

#Get a Tk window of 400 * 200
base = Tk()
base.geometry("470x330+350+250")
base.title("QR Code Generator")
base.resizable(width=False, height=False)

# variable to store text for QR Code
name = StringVar()
age = StringVar()
phone = StringVar()
address = StringVar()
url = StringVar()

# Field to input text
lable_name= Label(base,text="Enter ur name")
lable_name.place(x=50,y=50)
nameEntry = Entry(textvariable=name, width="30")
nameEntry.place(x=180,y=50)

lable_age= Label(base,text="Enter ur age")
lable_age.place(x=50,y=80)
ageEntry = Entry(textvariable=age, width="30")
ageEntry.place(x=180,y=80)

lable_phone= Label(base,text="Enter ur phone")
lable_phone.place(x=50,y=110)
phoneEntry = Entry(textvariable=phone, width="30")
phoneEntry.place(x=180,y=110)

lable_address= Label(base,text="Enter ur address")
lable_address.place(x=50,y=140)
addressEntry = Entry(textvariable=address, width="30")
addressEntry.place(x=180,y=140)

lable_url= Label(base,text="Enter ur url")
lable_url.place(x=50,y=170)
urlEntry = Entry(textvariable=url, width="30")
urlEntry.place(x=180,y=170)

# Call get_code() on click
button = Button(base,text="Get Code",command=get_code,width="30",height="2",bg="grey")
button.place(x=123,y=235)

base.mainloop() 
base.mainloop()