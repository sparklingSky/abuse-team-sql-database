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

# specifying an SQL query
sql = "SELECT * FROM TableName WHERE Email LIKE '%domain%';"


# fetching data from database; design 1; less flexible solution but more readable (allows selecting all table columns only)
# sample result: ID: 1|TicketNumber: 123456|FirstName: Jane|LastName: Doe|CompanyName: None|DomainName: domain.com etc.
def fetching_data(sql):
    try:
        # executing the SQL command
        cursor.execute(sql)
        # fetching all the rows
        results = cursor.fetchall()
        for row in results:
            # ID = row[0]
            # TicketNumber = row[1]
            # FirstName = row[2]
            # LastName = row[3]
            # CompanyName = row[4]
            # DomainName = row[5]
            # Email = row[6]
            # Address = row[7]
            # Phone = row[8]
            # Project1 = row[9]
            # Project2 = row[10]
            # Project3 = row[11]
            # Project4 = row[12]
            # FraudRecord = row[13]
            # Spamhaus_ROKSO = row[14]
            # Other = row[15]
            # printing fetched result for each row
            print("ID: " + str(int(row[0])) + "|" + "TicketNumber: " + str(int(row[1])) + "|" + "FirstName: " + str(row[2]) + "|" + "LastName: " + str(row[3]) + "|" + "CompanyName: " + str(row[4]) + "|" + "DomainName: " + str(row[5]) + "|" + "Email: " + str(row[6]) + "|" + "Address: " + str(row[7]) + "|" + "Phone: " + str(row[8]) + "|" + "Project1: " + str(row[9]) + "|" + "Project2: " + str(row[10]) + "|" + "Project3: " + str(row[11]) + "|" + "Project4: " + str(row[12]) + "|" + "FraudRecord: " + str(row[13]) + "|" + "Spamhaus_ROKSO: " + str(row[14]) + "|" + "Other: " + str(row[15]) + "|")

    except:
        print("Error: unable to fetch data")


# fetching data from database; design 2 (MySQL table console format); flexible solution but not quite readable for SELECT all columns queries
def fetching_data2(sql):
    try:
        # executing the SQL command
        cursor.execute(sql)
        # fetching all the rows in a list of lists
        results = cursor.fetchall()
        widths = []
        columns = []
        tavnit = '|'
        separator = '+'

        for cd in cursor.description:
            widths.append(max(cd[2], len(cd[0])))
            columns.append(cd[0])

        for w in widths:
            tavnit += " %-"+"%ss |" % (w,)
            separator += '-'*w + '--+'

        print(separator)
        print(tavnit % tuple(columns))
        print(separator)
        for row in results:
            print(tavnit % row)
            print(separator)

    except:
        print("Error: unable to fetch data")


# comment unnecessary / uncomment required line
fetching_data(sql)
fetching_data2(sql)

# disconnecting from the server
db_connect.close()
