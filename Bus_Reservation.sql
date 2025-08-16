drop database if exists bus_reservation;
create database bus_reservation;
use bus_reservation;

DROP TABLE IF EXISTS `bank_balence`;
CREATE TABLE `bank_balence` (
  `user_id` varchar(50) DEFAULT NULL,
  `balence` int DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `passengerid` varchar(50) DEFAULT NULL
);

INSERT INTO `bank_balence` VALUES ('Eric@1945',86200,'1945','Eric@1945'),('Brian@1947',148400,'2401','Brian@1947'),('Sruthi@2007',60000,'2007','Sruthi@2007'),('Riddle_88',175846,'6978','Riddle@Avada_kedavra'),('Elton@1947',160627,'0811','Elton@1947');

DROP TABLE IF EXISTS `bus`;
CREATE TABLE `bus` (
  `busno` int DEFAULT NULL,
  `travels_name` varchar(50) DEFAULT NULL,
  `depart` varchar(20) DEFAULT NULL,
  `dest` varchar(20) DEFAULT NULL,
  `type_bus` varchar(10) DEFAULT NULL,
  `no_of_seats` int DEFAULT NULL,
  `fare` float DEFAULT NULL,
  `statuss` varchar(20) DEFAULT NULL,
  `avail_tickt` int DEFAULT NULL
);

INSERT INTO `bus` VALUES (1,'Brian and Co.','Chennai','Coimbatore','A/C',60,500,'Available',16),(2,'Jishnu Travels','Tiruchirapalli','Madurai','Non A/C',80,250,'Available',5),(3,'Prathin Travels Agency','Erode','Chennai','Non A/C',70,400,'Unavailable',0),(4,'Tony and Co.','Tanjore','Hyderabad','A/C',90,800,'Available',3),(5,'Prathin Travels Agency','Kanyakumari','Ladakh','A/C',50,2900,'Unavailable',0),(6,'Jishnu Travels','Chennai','Coimbatore','A/C',70,450,'Available',34);

DROP TABLE IF EXISTS `passenger`;
CREATE TABLE `passenger` (
  `passengerid` varchar(50) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `phone_no` varchar(10) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `type` varchar(5) DEFAULT NULL
);

INSERT INTO `passenger` VALUES ('Eric@1945','Eric1945','Eric','9235854930','Hurtwood Edge, Cranleigh, UK','user'),('Brian@1947','Brian1947','Brian','1934586438','Baker Street, London, United Kingdom','user'),('Sruthi@2007','Sruthi2007','Sruthi','8374859682','T-9, Ragavendra apt, no-69, Thiruchirapalli, India','user'),('Elton@1947','Elton1947','Elton','1236547890','1 Blythe Road, London, W14 0HG','user'),('Harish@2007','Harish2007','Harish','9203947652','D-202 premier grihalakshmi apt virugambakkam','admin');

DROP TABLE IF EXISTS `passenger_travel`;
CREATE TABLE `passenger_travel` (
  `name` varchar(30) DEFAULT NULL,
  `busno` int DEFAULT NULL,
  `depart` varchar(50) DEFAULT NULL,
  `dest` varchar(50) DEFAULT NULL,
  `type_bus` varchar(10) DEFAULT NULL,
  `amt_paid` int DEFAULT NULL,
  `seats_booked` int DEFAULT NULL,
  `ticket_no` int DEFAULT NULL,
  `date` varchar(10) DEFAULT NULL
);
INSERT INTO `passenger_travel` VALUES ('Eric',6,'Chennai','Coimbatore','A/C',2250,5,1,'07-08-2024'),('Sruthi',6,'Chennai','Coimbatore','A/C',900,2,2,'28-10-2024'),('Brian',4,'Tanjavur','Hydrabad','A/C',1600,2,5,'29-05-2024'),('Elton',2,'Tiruchirapalli','Madurai','Non A/C',750,3,6,'02-06-2024');
