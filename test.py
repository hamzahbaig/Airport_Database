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
	print("\n\nCreating new Passenger Record...")
	sql = "INSERT INTO Passengers (CNIC,name,phone,address,nationality) VALUES (%s,%s,%s,%s,%s)"
	CNIC = input("\nEnter CNIC number: ")
	name = input("Enter Name: ")
	phone = int(input("Enter phone: "))
	address = input("Enter address: ")
	nationality = input("Enter nationality: ")
	val = (CNIC,name,phone,address,nationality)
	mycursor.execute(sql,val)
	mydb.commit()

def updateExistingPassenger():
	print("\n\nUpdating Passenger Record...")
	while(1):
		print("\nPress 1 to update name")
		print("Press 2 to update phone")
		print("Press 3 to update address")
		print("Press 4 to update nationality")
		print("Press 5 to cancel update")
		option = int(input("Enter option number: "))
		if(option == 5):
			break
		elif (option == 1):
			col = "name"
			cnic = input("\nEnter CNIC: ")
			newValue = input("Enter new value: ")
		elif (option == 2):
			col = "phone"
			cnic = input("\nEnter CNIC: ")
			newValue = input("Enter new value: ")
		elif (option == 3):
			col = "address"
			cnic = input("\nEnter CNIC: ")
			newValue = input("Enter new value: ")
		elif (option == 4):
			col = "nationality"
			cnic = input("\nEnter CNIC: ")
			newValue = input("Enter new value: ")

		sql = "UPDATE Passengers SET " + str(col) + " = %s WHERE CNIC = %s"
		val = (newValue,cnic)

		mycursor.execute(sql,val)
		mydb.commit() 

def availableFlights():
	print("\n\nCheck available Flights...")
	departureCode = input("Enter departure airport code: ")
	arrivalCode = input("Enter arrival airport code: ")

	if (len(departureCode) == 3 and len(arrivalCode) == 3 ):
		sql = "SELECT * FROM Flight WHERE departureAirport =  %s AND arrivalAirport = %s"
		val = (departureCode,arrivalCode)

		mycursor.execute(sql,val)
		myresult = mycursor.fetchall()

		for x in myresult:
			print(x)

def findCheapestFlights():
	print("\n\nCheck cheapest Flights...")
	departureCode = input("Enter departure airport code: ")
	arrivalCode = input("Enter arrival airport code: ")

	if (len(departureCode) == 3 and len(arrivalCode) == 3 ):
		sql = "SELECT * FROM Flight WHERE departureAirport = %s AND arrivalAirport = %s  ORDER BY fare ASC"
		val = (departureCode,arrivalCode)

		mycursor.execute(sql,val)
		print("\n\n\tCHEAPEST FLIGHT:- \n\n")
		myresult = mycursor.fetchone()

		print(myresult)

 # fixing this function, other than this function its working perfect
def generateTicket():
	print("\n\n Generating Ticket for the pasenger")

	cnic = input("Enter CNIC number: ")
	flightID = input("Enter Flight ID: ")

	mycursor.execute("SELECT * FROM Passengers WHERE CNIC = " + str(cnic))
	if(not mycursor.fetchone()):
		print("No such CNIC entry")
		return
	print("ALII")
	mycursor.execute("SELECT * FROM Flight WHERE flightID = 'PK305' ")
	# val = (flightID)
	if(not mycursor.fetchone()):
		print("No Such flight")
		return
	print("HAMZAHHH")
	sql = "INSERT INTO Ticket(CNICPassenger ,fID) VALUES (%S,%S)"
	val = (cnic,flightID)

	mycursor.execute(sql,val)
	mydb.commit()


def receptionistHandler(option):
	if option == "1":
		createNewPassengerRecord()
	elif option == "2":
		updateExistingPassenger()
	elif option == "3":
		availableFlights()
	elif option == "4":
		generateTicket()
	elif option == "5":
		findCheapestFlights()

	


def receptionistMenu():
	print("\n\nPress 1 to Create a new passenger record.")
	print("Press 2 to Update details of an exsisting record.")
	print("Press 3 to View all available flights in particular time period.")
	print("Press 4 to Generate ticket record for a particular passenger for a particular flight.")
	print("Press 5 to View cheapest flight.")
	print('Press 6 to View flight history of a particular passenger.')
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