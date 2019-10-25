import mysql.connector
import os

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="hamzah123",
	database = "Mydatabase"
	)
mycursor = mydb.cursor(buffered = True)	

def createNewPassengerRecord():
	print("\nCreating new Passenger Record..")
	sql = "INSERT INTO Passengers (CNIC,name,phone,address,nationality) VALUES (%s,%s,%s,%s,%s)"
	CNIC = input("Enter CNIC number: ")
	name = input("Enter Name: ")
	phone = int(input("Enter phone: "))
	address = input("Enter address: ")
	nationality = input("Enter nationality: ")
	val = (CNIC,name,phone,address,nationality)
	mycursor.execute(sql,val)
	mydb.commit()
def receptionistHandler(option):
	switcher = {
		1: createNewPassengerRecord()
	}

def receptionistMenu():
	print("\n\nPress 1 to Create a new passenger record.")
	print("Press 2 to Update details of an exsisting record.")
	print("Press 3 to view all available flights in particular time period.")
	print("Press 4 to generate ticket record for a particular passenger for a particular flight.")
	print("Press 5 to view cheapest flight.")
	print('Press 6 to view flight history of a particular passenger.')
	print('Press 7 to Cancel a particular ticket record.')
	option = input("\nPlease Enter the number")
	receptionistHandler(option)



def welcomeScreen():
	print("\n\n\n\t\t --- WELCOME TO AIRPORT ---")
	while(1):
		print("\n\n\t\tIf you are admin Press A|a and if you are a receptionist Press R|r  ")
		user = input()
		if (user == 'A' or user == 'a'):
			print("\n\nWelcome Admin :D")
			username = input("Enter Username: ")
			password = input("Enter Password: ")
			if(username == 'admin' and password == 'admin'):
				print("\nAccess Granted to Admin")
			else:
				print("\nWrong creditionals for Admin Login, Please Try again")

		elif (user == 'r' or user == 'R'):
			print("\n\nWelcome Receptionist")
			username = input("Enter Username: ")
			password = input("Enter Password: ")
			if(username == 'hamzah' and password == 'hamzah'):
				print("\nAccess Granted to Receiptionist")
				receptionistMenu()

			else:
				print("\nWrong creditionals for Receptionist, Please Try again")




def main():
	global mydb,mycursor

	fhandle = open("schema.sql")
	script = fhandle.read()
	records = mycursor.execute(script,multi = True)
	for row in records:
		print(row)
	fhandle = open("populate.sql")
	populate = fhandle.read()
	result = mycursor.execute(populate,multi = True)	
	for row in result:
		print (row)
	mydb.commit()
	welcomeScreen()
	# os.system('clear')





main()