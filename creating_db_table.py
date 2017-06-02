#!/usr/bin/python

import MySQLdb

username = "username"
password = "password"
hostname = "hostname"

# opening server connection
db_connect = MySQLdb.connect(host=hostname, user=username, passwd=password)

# preparing a cursor object
cursor = db_connect.cursor()


# creating a database
sql1 = "CREATE DATABASE IF NOT EXISTS AbuseTeamDB;"


def creating_DB(sql):
    cursor.execute(sql)


# creating a table
sql2 = """CREATE TABLE IF NOT EXISTS TableName (
ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Ticket INT,
FirstName NVARCHAR(50),
LastName NVARCHAR(50),
CompanyName NVARCHAR(150),
DomainName NVARCHAR(100),
Email NVARCHAR(100),
Address NVARCHAR(100),
Phone NVARCHAR(50),
Project1 NVARCHAR(5),
Project2 NVARCHAR(5),
Project3 NVARCHAR(5),
Project4 NVARCHAR(5),
FraudRecord NVARCHAR(5),
Spamhaus_ROKSO NVARCHAR(5),
Other NVARCHAR(100)
);"""


def creating_table(sql):
    cursor.execute(sql)

# comment / uncomment the line if required
creating_DB(sql1)

# selecting a database
db_connect.select_db("AbuseTeamDB")

# comment / uncomment the line if required
creating_table(sql2)

# disconnecting from the server
db_connect.close()
