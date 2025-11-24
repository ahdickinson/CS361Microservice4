communication contract

commands to create account, find account, and login require username.
create account and login commands require password.
will return OK or ERROR message.

example:
CREATE ACCOUNT : username|password
FIND ACCOUNT : username
LOGIN : username|password

example responses for account creation:
OK : Account username created at localpath 
ERROR : Account username already exists

example responses for login command:
ERROR : Account username does not exist
ERROR : Incorrect password for username
OK : Login successful for username
