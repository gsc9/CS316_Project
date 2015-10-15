CREATE TABLE User
(email VARCHAR(256) NOT NULL PRIMARY KEY,
 username VARCHAR(256) NOT NULL);

INSERT INTO User VALUES(‘grace.s.chen@duke.edu’, ‘Grace Chen’);
INSERT INTO User VALUES(‘grant.kelly@duke.edu’, ‘Grant Kelly’);
INSERT INTO User VALUES(‘asy11@duke.edu’, ‘Annie Yang’);
INSERT INTO User VALUES(‘martin.tamayo@gmail.com’, ‘Martin Tamayo’);


CREATE TABLE Event
(eid INTEGER NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
 title VARCHAR(256) NOT NULL, 
 date DATE NOT NULL,
 time TIME NOT NULL,
 location VARCHAR(256) NOT NULL,
 description VARCHAR(400));

INSERT INTO Event VALUES(1, ‘Eclipse Viewing’, ‘2015-09-27’, ‘21:07:00’, ‘location’, ‘Supermoon’);
INSERT INTO Event VALUES(2, ‘Midterm Cram Session’, '2015-10-07', '19:00:00', 'your house', 'Study session the night before the midterm');
INSERT INTO Event VALUES(3, 'Birthday Potluck', '2015-10-15', '20:00:00', 'His House', 'My sister's surprise birthday party');
INSERT INTO Event VALUES (4, 'July BBQ', '2015-7-15', '18:00:00', 'Our house, BBQ for group bonding after class');


CREATE TABLE Ingredient
 (name VARCHAR(256) NOT NULL PRIMARY KEY);

INSERT INTO Ingredient VALUES(‘Birthday Cake’);
INSERT INTO Ingredient VALUES(‘Bug spray’);
INSERT INTO Ingredient VALUES(‘Cookies’);
INSERT INTO Ingredient VALUES(‘Corn’);
INSERT INTO Ingredient VALUES(‘Cups’);
INSERT INTO Ingredient VALUES(‘Mooncakes’);
INSERT INTO Ingredient VALUES(‘Napkins’);
INSERT INTO Ingredient VALUES(‘Picnic blanket’);
INSERT INTO Ingredient VALUES(‘Pizza’);
INSERT INTO Ingredient VALUES(‘Plates’);
INSERT INTO Ingredient VALUES(‘Soda’);
INSERT INTO Ingredient VALUES(‘Someone’s room’);
INSERT INTO Ingredient VALUES(‘Tablecloth’);
INSERT INTO Ingredient VALUES(‘Telescope’);
INSERT INTO Ingredient VALUES(‘Textbook’);
INSERT INTO Ingredient VALUES(‘Trail Mix’);
INSERT INTO Ingredient VALUES(‘Utensils’);
INSERT INTO Ingredient VALUES(‘Water bottles’);
INSERT INTO Ingredient VALUES(‘Buns’);
INSERT INTO Ingredient VALUES(‘Ketchup’);
INSERT INTO Ingredient VALUES(‘Tomatoes’);
INSERT INTO Ingredient VALUES(‘Ground Beef’);


CREATE TABLE Part_Of 
(email VARCHAR(256) NOT NULL REFERENCES User(email),
 eid INTEGER NOT NULL REFERENCES Event(eid),
 PRIMARY KEY(email, eid));

INSERT INTO Part_Of VALUES(‘grace.s.chen@duke.edu’, 1);
INSERT INTO Part_Of VALUES(‘grace.s.chen@duke.edu’, 2);
INSERT INTO Part_Of VALUES(‘grace.s.chen@duke.edu’, 3);
INSERT INTO Part_Of VALUES(‘grant.kelly@duke.edu’, 4);


CREATE TABLE Event_Ingredient 
(name VARCHAR(256) NOT NULL REFERENCES Ingredient(name),
 eid INTEGER NOT NULL REFERENCES Event(eid), 
 quantity INTEGER NOT NULL,
 units VARCHAR(256),
 comments VARCHAR(256),
 PRIMARY KEY(name, eid));

INSERT INTO Event_Ingredient VALUES(‘Mooncakes’, 1, 20, NULL, ‘The giant ones’);
INSERT INTO Event_Ingredient VALUES(‘Picnic blanket’, 1, 2, NULL, ‘Since there are so many of us’);
INSERT INTO Event_Ingredient VALUES(‘Telescope’, 1, 1, NULL, ‘I believe Tom has one? (nudge nudge)’);
INSERT INTO Event_Ingredient VALUES(‘Plates’, 1, 25, NULL, ‘My sisters super eco-conscientious, so paper cups are best’);
INSERT INTO Event_Ingredient VALUES(‘Napkins’, 1, 25, NULL, NULL);
INSERT INTO Event_Ingredient VALUES(‘Water bottles’, 1, 25, NULL, NULL);
INSERT INTO Event_Ingredient VALUES(‘Bug spray’, 1, 1, ‘can’, NULL);
INSERT INTO Event_Ingredient VALUES(‘Cookies’, 2, 1, ‘package’, NULL);
INSERT INTO Event_Ingredient VALUES(‘Trail Mix’, 2, 1, ‘bag’, NULL);
INSERT INTO Event_Ingredient VALUES(‘Soda’, 2, 1, ‘bottle’, NULL);
INSERT INTO Event_Ingredient VALUES(‘Cups’, 2, 10, NULL, NULL);
INSERT INTO Event_Ingredient VALUES(‘Textbook’, 2, 3, NULL, ‘My sister's also vegetarian, so please buy at least one vegetarian pizza!’);
INSERT INTO Event_Ingredient VALUES(‘Room of someone’, 2, 1, NULL, NULL);
INSERT INTO Event_Ingredient VALUES(‘Birthday Cake’, 3, 1, NULL, NULL);
INSERT INTO Event_Ingredient VALUES('Plates', 3, 20, NULL, 'My sisters super eco-conscientious so paper cups are best');
INSERT INTO Event_Ingredient VALUES('Napkins', 3, 20, NULL, NULL );
INSERT INTO Event_Ingredient VALUES('Utensils', 3, 1, 'box', NULL);
INSERT INTO Event_Ingredient VALUES('Soda', 3, 2, 'bottles', NULL );
INSERT INTO Event_Ingredient VALUES('Cups', 3, 20, null, 'Again super eco-conscientious');
INSERT INTO Event_Ingredient VALUES('Pizza', 3, 5, 'boxes', 'My sisters also vegetarian comma so please buy at least one vegetarian pizza!');
INSERT INTO Event_Ingredient VALUES('Tablecloth', 3, 2, NULL, null);
INSERT INTO Event_Ingredient VALUES('Someones room', 3, 1, null, 'Probably mine');
INSERT INTO Event_Ingredient VALUES('Corn', 4, 1, null, null);
INSERT INTO Event_Ingredient VALUES('Ground Beef', 4, 4, null, 'packages comma make sure it is lean');
INSERT INTO Event_Ingredient VALUES('Cups', 4, 40, null, null);
INSERT INTO Event_Ingredient VALUES('Corn', 4, 24, null, 'On the cob please');
INSERT INTO Event_Ingredient VALUES('Tomatos', 4, 10, null, null);
INSERT INTO Event_Ingredient VALUES('Buns', 4, 4, 'packages', 'For hamburgers');
INSERT INTO Event_Ingredient VALUES('Ketchup', 4, 1, 'bottle', 'Can bring from your own fridge');


CREATE TABLE Who_Buys
(email VARCHAR(256) NOT NULL REFERENCES User(email),
 name VARCHAR(256) NOT NULL REFERENCES Ingredient(name),
 eid INTEGER NOT NULL REFERENCES Event(eid),
 bringing INTEGER NOT NULL,
 user_comments VARCHAR(400),
 PRIMARY KEY(email, name, eid));

INSERT INTO Who_Buys VALUES(‘Picnic blanket’, grace.s.chen@duke.edu, 1, 2, NULL);
INSERT INTO Who_Buys VALUES(‘Bug spray’, grace.s.chen@duke.edu, 1, 1, NULL);
INSERT INTO Who_Buys VALUES(‘Soda’, grace.s.chen@duke.edu, 2, 1, NULL);
INSERT INTO Who_Buys VALUES(‘Textbook’, grace.s.chen@duke.edu, 2, 1, NULL);
INSERT INTO Who_Buys VALUES(‘Birthday Cake’, grace.s.chen@duke.edu, 3, 1, NULL);
INSERT INTO Who_Buys VALUES(‘Pizza’, grace.s.chen@duke.edu, 3, 1, NULL);
INSERT INTO Who_Buys VALUES(‘Room of someone’, grace.s.chen@duke.edu, 3, 1, NULL);
INSERT INTO Who_Buys VALUES(‘Ketchup’, grant.kelly@duke.edu, 4, 1, NULL);
INSERT INTO Who_Buys VALUES(‘Ground Beef’, grant.kelly@duke.edu, 4, 2, NULL);



--QUERIES


--Retrieve list of users.
SELECT username FROM User;

--Retrieve all events that a given user is attending.


--Divide these events into events that have yet to happen / are currently happening versus events that are already over.


--Retrieve all users attending a given event.


--Retrieve the details for one given event.


--Retrieve list of items a user has committed to bringing to an event.


--Retrieve all event ingredients for a specific potluck.


--Retrieve list of items used in other events that have other items in common with a given event.  (_% of events that used ingredient _ also used another ingredient _ (complicated))


--Retrieve who signed up to buy which items for a given event


--Retrieve the users that haven’t signed up to buy anything


--Retrieve list of ingredients.
SELECT name FROM Ingredient;

--Retrieve ingredients that have not been signed up for (at all) in a specific event
SELECT name, eid
FROM Event_Ingredient
WHERE NOT EXISTS (SELECT name AS notTaken
		FROM whoBuys
		WHERE name = notTaken); //EID??

--Retrieve ingredients that do not have enough people signed up for them in a specific event
SELECT name
FROM Event_Ingredient, whoBuys