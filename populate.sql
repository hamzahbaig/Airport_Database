delete from Ticket;
ALTER TABLE `Ticket` AUTO_INCREMENT = 0;	
delete  from Flight;
delete from Passengers;
insert into Flight values("PK301", "LHR", "KHI", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK302", "PSH", "KHI", "08:00", "12:00", "ANJ-412", 155000);
insert into Flight values("PK303", "LHR", "KHI", "08:00", "12:00", "ANJ-412", 115000);
insert into Flight values("PK304", "ISL", "MUL", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK305", "MUL", "LHR", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK306", "KHI", "LHR", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK307", "KHI", "ISL", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK308", "KHI", "LHR", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK309", "KHI", "LHR", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK310", "ISL", "LHR", "08:00", "12:00", "ANJ-412", 135000);

insert into Passengers values("36302", "hamzah", "0312", "null", "pak1");
insert into Passengers values("36303", "minhal2", "0313", "null", "pak2");
insert into Passengers values("36305", "ali", "0314", "null", "pak3");
insert into Passengers values("36306", "usman", "0315", "null", "pak4");
insert into Passengers values("36307", "minhal3", "0316", "null", "pak3");
insert into Passengers values("36308", "areeb", "0317", "null", "pak2");
insert into Passengers values("36309", "adil", "0318", "null", "pak1");
insert into Passengers values("36310", "farhan", "0319", "null", "pak4");
insert into Passengers values("36311", "saad", "0310", "null", "pak3");
insert into Passengers values("36312", "rabia", "03140", "null", "pak3");

insert into Ticket(CNICPassenger ,fId) values("36302","PK301");
insert into Ticket(CNICPassenger ,fId) values("36303","PK302");
insert into Ticket(CNICPassenger ,fId) values("36305","PK303");
insert into Ticket(CNICPassenger ,fId) values("36306","PK304");
insert into Ticket(CNICPassenger ,fId) values("36307","PK305");
insert into Ticket(CNICPassenger ,fId) values("36308","PK306");
insert into Ticket(CNICPassenger ,fId) values("36309","PK307");
insert into Ticket(CNICPassenger ,fId) values("36310","PK308");
insert into Ticket(CNICPassenger ,fId) values("36311","PK309");
insert into Ticket(CNICPassenger ,fId) values("36312","PK310");

insert into FlighHistory(CNICPassenger ,fId) values("36302","PK301");
insert into FlighHistory(CNICPassenger ,fId) values("36303","PK302");
insert into FlighHistory(CNICPassenger ,fId) values("36305","PK303");
insert into FlighHistory(CNICPassenger ,fId) values("36306","PK304");
insert into FlighHistory(CNICPassenger ,fId) values("36307","PK305");
insert into FlighHistory(CNICPassenger ,fId) values("36308","PK306");
insert into FlighHistory(CNICPassenger ,fId) values("36309","PK307");
insert into FlighHistory(CNICPassenger ,fId) values("36310","PK308");
insert into FlighHistory(CNICPassenger ,fId) values("36311","PK309");
insert into FlighHistory(CNICPassenger ,fId) values("36312","PK310");
commit;