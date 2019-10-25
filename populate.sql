delete from Ticket;
ALTER TABLE `Ticket` AUTO_INCREMENT = 0;	
delete  from Flight;
delete from Passengers;
insert into Flight values("PK301", "LHR", "KHI", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK302", "LHR", "KHI", "08:00", "12:00", "ANJ-412", 155000);
insert into Flight values("PK303", "LHR", "KHI", "08:00", "12:00", "ANJ-412", 115000);
insert into Flight values("PK304", "ISL", "MUL", "08:00", "12:00", "ANJ-412", 135000);
insert into Flight values("PK305", "KHI", "LHR", "08:00", "12:00", "ANJ-412", 135000);
insert into Passengers values("36302", "minhal1", "0312", "null", "pak1");
insert into Passengers values("36303", "minhal2", "0313", "null", "pak2");
insert into Passengers values("36304", "minhal3", "0314", "null", "pak3");
insert into Ticket(CNICPassenger ,fID) values("36304","PK303");
insert into Ticket(CNICPassenger ,fID) values("36302","PK301");
insert into Ticket(CNICPassenger ,fID) values("36303","PK302");

commit;