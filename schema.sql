drop table if exists Ticket CASCADE;
drop table if exists Flight CASCADE;
drop table if exists Passengers CASCADE;
drop table if exists FlighHistory CASCADE;

CREATE TABLE Flight(
	flightID VARCHAR(5) PRIMARY KEY, 
	departureAirport VARCHAR(3),
	arrivalAirport VARCHAR(3), 
	departureTime VARCHAR(5),
	arrivalTime VARCHAR(5),
	airplane VARCHAR(7),
	fare INT
);
CREATE TABLE Passengers(
	CNIC VARCHAR(13) PRIMARY KEY , 
	name VARCHAR(30),
	phone VARCHAR(15),
	address VARCHAR(30),
	nationality VARCHAR(30)
);
CREATE TABLE FlighHistory(
	FlighHistoryID INT AUTO_INCREMENT PRIMARY KEY ,
	CNICPassenger VARCHAR(13) , 
	fId VARCHAR(5)
);
CREATE TABLE Ticket (
	ticketID INT AUTO_INCREMENT PRIMARY KEY ,
	CNICPassenger VARCHAR(13) , 
	fId VARCHAR(5)
);
alter table Ticket 
	add FOREIGN KEY (fId) 
	REFERENCES Flight(flightID) ,
	add FOREIGN KEY (CNICPassenger) 
	REFERENCES Passengers(CNIC);


