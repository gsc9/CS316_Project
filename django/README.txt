Annie Yang
Grace Chen
Grant Kelly
Martin Tamayo


Final README

Acquiring the production data set is a complicated process, so it is broken down into steps below. Make sure that all files are in a directory accessible from the vagrant virtual machine.

1) Run Generate Data.jar. This will output files admin.py and GEN-PRODUCTION.SQL to the directory that Generate Data.jar is in.

2) Navigate to the django/beers_alt directory and back up the admin.py file found there to a different folder.

3) Place the admin.py file created by Generate Data.jar in the django/beers_alt directory.

4) Launch vagrant and ssh into vagrant. Change directories to the django directory. The next step should only be necessary if the table Auth_User has been used in the past (likely, if other django applications have been run in vagrant) and if the tables associated with our app already exist.

5) Change directories to the django directory and run the command "psql mysite". Run the following commands in psql:
 - DELETE FROM Auth_User;
 - ALTER SEQUENCE Auth_User_id_seq RESTART WITH 1;
 - DROP TABLE Event;
 - DROP TABLE Ingredient;
 - DROP TABLE Part_Of;
 - DROP TABLE Event_Ingredient;
 - DROP TABLE Who_Buys;

6) Quit psql and run the following command in the command line: python manage.py runserver 0.0.0.0:8000

7) Wait ~20 minutes. Running the server will execute the code in the admin.py file, which is adding 10,000 users to django's Auth_User table, complete with encrypted passwords. Eventually, the command line will show an error. Control-c to stop running the server.

8) Move the original, backed-up admin.py file back to the django/beers_alt directory.

9) Run the following command in the command line to create the database tables: python manage.py syncdb

10) To populate the tables with the production data set, move the GEN-PRODUCTION.SQL file created by Generate Data.jar to the django directory.

11) In the django directory, run psql mysite and run:
 - \i GEN-PRODUCTION.SQL;

12) Wait a few moments for the database tables to be populated. Note that some of the insertions will throw errors. This is fine, as some of the insertion statements violate the constraints of the database tables. When done, exit pqsl.

13) Run the server again: python manage.py runserver 0.0.0.0:8000

14) It should now be possible to access the application using any browser in the VM at localhost:8000/beers_alt/

15) It may be desirable to create a django superuser (after adding the production data set users in admin.py) by running the command: python manage.py createsuperuser. This will allow you to view the database at localhost:8000/admin/