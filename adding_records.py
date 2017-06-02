#!/usr/bin/python

import MySQLdb

username = "username"
password = "password"
hostname = "hostname"

# opening server connection
db_connect = MySQLdb.connect(host=hostname, user=username, passwd=password)

# selecting a database
db_connect.select_db("AbuseTeamDB")

# preparing a cursor object
cursor = db_connect.cursor()

# specifying an SQL query to INSERT a record into the table
sql = """INSERT INTO TableName (Ticket, FirstName, LastName, DomainName, Email, Address, Phone, Project1, FraudRecord, Spamhaus_ROKSO)
VALUES (123456, 'Jane', 'Doe', 'domain.com', 'jane.doe@domain.com', '456 South Michigan Ave Suite 1234, 60611 Chicago, US', '+1.1234567890', 'Yes', 'Yes', 'Yes');"""
try:
    # executing the SQL command
    cursor.execute(sql)
    # committing changes in the database
    db_connect.commit()
except:
    # rollback in case there is any error
    db_connect.rollback()

# disconnecting from the server
db_connect.close()
