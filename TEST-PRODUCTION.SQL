--Tentative database name: crowdcon



--QUERIES


--Retrieve list of users.
SELECT username FROM Registered_User;

--Retrieve all events that a given user is attending (e.g. username = 'yon vo', current date = '10 / 20 / 2015', current time = '11:00').
SELECT Event.title FROM Registered_User, Part_Of, Event WHERE Registered_User.username = 'yon vo' AND Registered_User.email = Part_Of.email AND Part_Of.eid = Event.eid AND (Event.date > '10 / 20 / 2015' OR (Event.date = '10 / 20 / 2015' AND Event.time > '11:00'));

--Retrieve all events that a given user has attended (e.g. username = 'yon vo', current date = '10 / 20 / 2015', current time = '11:00').
(SELECT Event.title FROM Registered_User, Part_Of, Event WHERE Registered_User.username = 'yon vo' AND Registered_User.email = Part_Of.email AND Part_Of.eid = Event.eid) EXCEPT (SELECT Event.title FROM Registered_User, Part_Of, Event WHERE Registered_User.username = 'yon vo' AND Registered_User.email = Part_Of.email AND Part_Of.eid = Event.eid AND (Event.date > '10 / 20 / 2015' OR (Event.date = '10 / 20 / 2015' AND Event.time > '11:00')));

--Retrieve all users attending a given event (e.g. eid = 983).
SELECT Registered_User.username FROM Registered_User, Part_Of, Event WHERE Event.eid = 983 AND Registered_User.email = Part_Of.email AND Part_Of.eid = Event.eid;

--Retrieve the details for one given event (e.g. eid = 983).
SELECT title, date, time, location, description FROM Event WHERE eid = 983;

--Retrieve list of items a user has committed to bringing to an event (e.g. username = 'yon vo', eid = 983).
SELECT Who_Buys.ingredient_name, Who_Buys.bringing FROM Registered_User, Who_Buys WHERE Registered_User.username = 'yon vo' AND Who_Buys.eid = 983 AND Registered_User.email = Who_Buys.email;

--Retrieve all event ingredients for a specific potluck (e.g. eid = 983).
SELECT ingredient_name, quantity, units, comments FROM Event_Ingredient WHERE eid = 983;

--Retrieve list of items used in other events that have other items in common with a given event.  (_% of events that used ingredient _ also used another ingredient _ (complicated...))


--Retrieve who signed up to buy which items for a given event (e.g. eid = 983, item name = 'icing').
SELECT Registered_User.username, Who_Buys.bringing FROM Registered_User, Who_Buys WHERE Registered_User.email = Who_Buys.email AND Who_Buys.eid = 983 AND Who_Buys.ingredient_name = 'icing';

--Retrieve the users that haven't signed up to buy anything for a given event (e.g. eid = 983).
(SELECT Registered_User.username FROM Registered_User, Part_Of WHERE Registered_User.email = Part_Of.email AND Part_Of.eid = 983) EXCEPT (SELECT Registered_User.username FROM Registered_User, Who_Buys WHERE Registered_User.email = Who_Buys.email AND Who_Buys.eid = 983);

--Retrieve list of ingredients.
SELECT ingredient_name FROM Ingredient;

--Retrieve ingredients that have not been signed up for (at all) in a specific event (e.g. eid = 983).
(SELECT ingredient_name FROM Event_Ingredient WHERE eid = 983) EXCEPT ALL (SELECT ingredient_name FROM Who_Buys WHERE eid = 983);

--Retrieve ingredients that do not have enough people signed up for them in a specific event (e.g. eid = 983).
