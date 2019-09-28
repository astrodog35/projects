from Tkinter import *
import time
import random
import sys

customers = []

def addCustomer():
	addcoustomer = Tk()
	addcoustomer.title("Add Coustomer")
	addcoustomer.geometry("700x500")
	
	FirstName = StringVar()
	LastName = StringVar()
	Email = StringVar()
	RoomNum = StringVar()
	PhoneNum = StringVar()
	CostPerNights = IntVar()
	Nights = IntVar()
	
	Label(addcoustomer, text="First Name:", font=("Arial", 20)).grid(row=1, column=1)
	firstname = Entry(addcoustomer, textvariable=FirstName).grid(row=1, column=2)
	Label(addcoustomer, text="Last Name:", font=("Arial", 20), bg="white").grid(row=2, column=1)
	lastname = Entry(addcoustomer, textvariable=LastName, bg="white").grid(row=2, column=2)
	Label(addcoustomer, text="Email:", font=("Arial", 20)).grid(row=3, column=1)
	email = Entry(addcoustomer, textvariable=Email).grid(row=3, column=2)
	Label(addcoustomer, text="Room #:", font=("Arial", 20), bg="white").grid(row=4, column=1)
	roomnum = Entry(addcoustomer, textvariable=RoomNum, bg="white").grid(row=4, column=2)
	Label(addcoustomer, text="Phone #:", font=("Arial", 20)).grid(row=5, column=1)
	phonenum = Entry(addcoustomer, textvariable=PhoneNum).grid(row=5, column=2)
	Label(addcoustomer, text="Cost/Night:", font=("Arial", 20), bg="white").grid(row=6, column=1)
	costpernights = Entry(addcoustomer, textvariable=CostPerNights, bg="white").grid(row=6, column=2)
	Label(addcoustomer, text="Nights:", font=("Arial", 20)).grid(row=7, column=1)
	nights = Entry(addcoustomer, textvariable=Nights).grid(row=7, column=2)
	Label(addcoustomer, text="\n").grid(row=8, column=1)
	
	firstName = FirstName.get()
	lastName = LastName.get()
	eMail = Email.get()
	roomNum = RoomNum.get()
	phoneNum = PhoneNum.get()
	costPerNights = CostPerNights.get()
	nIghts = Nights.get()
	
	def getPrint():
		customers.append(str(lastName))
		print(customers[0])

	CreateCoustomer = Button(addcoustomer, text="Create Customer", command=getPrint).grid(row=9, column=8)

root = Tk()
root.title("Hotel")
root.geometry("700x500")

Label(root, text="Hotel v1.0", font=("Arial", 25)).pack()
Label(root, text="").pack()

add_customer = Button(root, text="Add Customer", command = addCustomer).pack()

mainloop()
