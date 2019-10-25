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

def generateTicket():
	print("\n\n Generating Ticket for the pasenger")

	
	cnic = input("Enter your CNIC number: ")
	mycursor.execute("SELECT * FROM Flight")
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

	flightId = input("Choose flight Id from above mentioned Ids: ")

	sql = 'INSERT INTO Ticket(CNICPassenger ,fId) VALUES(%s,%s)'
	val = (cnic,flightId)
	mycursor.execute(sql,val)
	mydb.commit()
	sql = 'INSERT INTO FlighHistory(CNICPassenger ,fId) VALUES(%s,%s)'
	val = (cnic,flightId)
	mycursor.execute(sql,val)
	mydb.commit()
	
	
def cancelFlight():
	print("\n\nCancelling Flight...")

	cnic = input("Enter CNIC number: ")
	mycursor.execute("SELECT * FROM Flight")
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)

	flightId = input("Choose flight Id from above mentioned Ids: ")

	sql = "DELETE FROM Ticket WHERE fId = %s AND CNICPassenger = %s "
	val = (flightId,cnic)

	mycursor.execute(sql,val)
	mydb.commit()

def printHistory():
	print("\n\n  Printing Flight History...")

	cnic = input("Enter CNIC number: ")
	sql = "SELECT * from FlighHistory WHERE CNICPassenger = " + cnic
	val = (cnic)
	mycursor.execute(sql,val)
	result = mycursor.fetchall()

	for x in result:
		print(x)

def addNewFlight():
	flightID = input("Enter flight ID: ")
	depAir = input("Enter Departure Airport: ")
	arrAir = input("Enter Arrival Airport: ")
	depTime = input("Enter Departure Time: ")
	arrTime = input("Enter Arrival Time: ")
	airp = input("Enter airplane name: ")
	f = input("Enter fare of plane: ")

	sql = "INSERT INTO Flight (flightID,departureAirport,arrivalAirport,departureTime,arrivalTime,airplane,fare) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	val = (flightID,depAir,arrAir,depTime,arrTime,airp,int(f))

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
	elif option == "6":
		printHistory()
	elif option == "7":
		cancelFlight()

def updateFlight():
	print("\n\nUpdating Flight Record...")
	while(1):
		print("\n\nPress 1 to UPDATE flight id ")
		print("Press 2 to UPDATE Departure airport")
		print("Press 3 to UPDATE Arrival airport")
		print("Press 4 to UPDATE Departure time")
		print("Press 5 to UPDATE Arrival time")
		print("Press 6 to UPDATE Airport ")
		print("Press 7 to UPDATE fare")
		print("Press 8 to exit update ")
		option = int(input(""))
		if(option == 8):
			return
		elif(option == 1):
			coloumn = "flightID"
			flightid = input("enter flight_id row you want to change ")
			newval = input("enter the newvalue ")
		elif(option == 2):
			coloumn = "departureAirport"
			flightid = input("enter flight_id row you want to change ")
			newval = input("enter the newvalue ")
		elif(option == 3):
			coloumn = "arrivalAirport"
			flightid = input("enter flight_id row you want to change ")
			newval = input("enter the newvalue ")
		elif(option == 4):
			coloumn = "departureTime"
			flightid = input("enter flight_id row you want to change ")
			newval = input("enter the newvalue ")
		elif(option == 5):
			coloumn = "arrivalTime"
			flightid = input("enter flight_id row you want to change ")
			newval = input("enter the newvalue ")
		elif(option == 6):
			coloumn = "airplane"
			flightid = input("enter flight_id row you want to change ")
			newval = input("enter the newvalue ")
		elif(option == 7):
			coloumn = "fare"
			flightid = input("enter flight_id row you want to change ")
			newval = int(input("enter the newvalue "))
		elif option == "8":
			return

		sql = 'UPDATE Flight SET '+coloumn+' = %s WHERE flightID = %s'
		val = (newval,flightid);
		mycursor.execute(sql,val)
		mydb.commit()

def viewFlights():
	print("\n\nViewing Flights...")
	airport = input("Enter airport: ")

	sql = "SELECT * from Flight where arrivalAirport = %s OR departureAirport = %s"
	val = (airport,airport)

	mycursor.execute(sql,val)
	result = mycursor.fetchall()
	print("\n ALL Flights...")
	for x in result:
		print(x)

def adminHandler(option):
	if option == "1":
		addNewFlight()
	elif option =="2":
		updateFlight()
	elif option == "3":
		viewFlights()

def adminMenu():
	print("\n\nPress 1 add new flight.")
	print("Press 2 to Update details of an exsisting flight.")
	print("Press 3 to view all flights landing and taking off.")
	option = input("\nPlease Enter the number")
	adminHandler(option)


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
				adminMenu()
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