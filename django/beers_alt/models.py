from django.db import models

# class Bar(models.Model):
#     name = models.CharField(max_length=20, primary_key=True)
#     address = models.CharField(max_length=20, blank=True)

class Drinker(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    address = models.CharField(max_length=20, blank=True)

#CREATE TABLE Registered_User (email VARCHAR(256) NOT NULL PRIMARY KEY, username VARCHAR(256) NOT NULL);
class Registered_User(models.Model):
    email = models.CharField(max_length=256, primary_key=True)
    username = models.CharField(max_length=256)
    class Meta:
        db_table = u'registered_user'
    def __unicode__(self):
    	return self.pk

#CREATE TABLE Event (eid INTEGER NOT NULL UNIQUE PRIMARY KEY, title VARCHAR(256) NOT NULL, date DATE NOT NULL, time TIME NOT NULL, location VARCHAR(256) NOT NULL, description VARCHAR(400));
class Event(models.Model):
	eid = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=256)
	date = models.DateField()
	time = models.TimeField()
	location = models.CharField(max_length=256)
	description = models.CharField(max_length=400)
	class Meta:
		db_table = u'event'
	def __unicode__(self):
		return self.pk


#CREATE TABLE Ingredient (ingredient_name VARCHAR(256) NOT NULL PRIMARY KEY);
class Ingredient(models.Model):
	ingredient_name = models.CharField(max_length=256, primary_key=True)
	class Meta:
		db_table = u'ingredient'
	def __unicode__(self):
		return self.pk


#CREATE TABLE Part_Of (email VARCHAR(256) NOT NULL REFERENCES Registered_User(email), eid INTEGER NOT NULL REFERENCES Event(eid), is_admin BOOLEAN NOT NULL, PRIMARY KEY(email, eid));
class Part_Of(models.Model):
	email = models.ForeignKey(Registered_User, db_column='email')
	eid = models.ForeignKey(Event, db_column='eid')
	is_admin = models.BooleanField(default=False)
	class Meta:
		db_table = u'part_of'
        unique_together = (('email', 'eid'),)

#CREATE TABLE Event_Ingredient
#(name VARCHAR(256) NOT NULL REFERENCES Ingredient(name),
 #eid INTEGER NOT NULL REFERENCES Event(eid),
 #quantity INTEGER NOT NULL,
 #units VARCHAR(256),
 #comments VARCHAR(256),
 #PRIMARY KEY(name, eid));
class Event_Ingredient(models.Model):
	name = models.ForeignKey(Ingredient, db_column='name')
	eid = models.ForeignKey(Event, db_column='eid')
	quantity = models.IntegerField()
	units = models.CharField(max_length=256)
	comments = models.CharField(max_length=256)
	class Meta:
		db_table = u'event_ingredient'
        unique_together = (('name', 'eid'),)



#CREATE TABLE Who_Buys
#(email VARCHAR(256) NOT NULL REFERENCES RegisteredUser(email),
 #name VARCHAR(256) NOT NULL REFERENCES Ingredient(name),
 #eid INTEGER NOT NULL REFERENCES Event(eid),
 #bringing INTEGER NOT NULL,
 #user_comments VARCHAR(400),
 #PRIMARY KEY(email, name, eid));

class Who_Buys(models.Model):
	email = models.ForeignKey(Registered_User, db_column='email')
	name = models.ForeignKey(Ingredient, db_column='name')
	eid = models.ForeignKey(Event, db_column='eid')
	bringing = models.IntegerField()
	user_comments = models.CharField(max_length=400)
	class Meta:
		db_table = u'who_buys'
        unique_together = (('email', 'name', 'eid'),)

# class Frequents(models.Model):
#     drinker = models.ForeignKey(Drinker, db_column='drinker')
#     bar = models.ForeignKey(Bar, db_column='bar')
#     times_a_week = models.SmallIntegerField(null=True, blank=True)
#
# class Beer(models.Model):
#     name = models.CharField(max_length=20, primary_key=True)
#     brewer = models.CharField(max_length=20, blank=True)
#
# class Serves(models.Model):
#     bar = models.ForeignKey(Bar, db_column='bar')
#     beer = models.ForeignKey(Beer, db_column='beer')
#     price = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
#
# class Likes(models.Model):
#     drinker = models.ForeignKey(Drinker, db_column='drinker')
#     beer = models.ForeignKey(Beer, db_column='beer')
