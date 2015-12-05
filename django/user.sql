CREATE TABLE Part_Of (email VARCHAR(256) NOT NULL REFERENCES Registered_User(email), eid INTEGER NOT NULL REFERENCES Event(eid), is_admin BOOLEAN NOT NULL, PRIMARY KEY(email, eid));
INSERT INTO Part_Of VALUES('carlos.denzine@example.com', 2685, TRUE);
INSERT INTO Part_Of VALUES('deneen.harian@example.com', 1765, TRUE);
INSERT INTO Part_Of VALUES('ronnie.teddy@example.com', 4693, TRUE);
INSERT INTO Part_Of VALUES('adella.hurles@example.com', 204, TRUE);
INSERT INTO Part_Of VALUES('laurence.senter@example.com', 3485, TRUE);
INSERT INTO Part_Of VALUES('sang.chilcoat@example.com', 4942, TRUE);
