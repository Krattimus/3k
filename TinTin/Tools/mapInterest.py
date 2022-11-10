import sys
import mysql.connector
import mysql.connector
from mysql.connector import errorcode
from tintin import TinTin
import os


filename = os.path.expanduser('~') + '/3kdb.txt'
file = open(filename, 'r')
content = file.read().splitlines()

dbConfig = {'user':'krattimus',
            'password':content[0],
            'host':'localhost',
            'database':'3kDB',
            'autocommit':'True'}

try:
    db = mysql.connector.connect(**dbConfig)
    cursor = db.cursor()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print ("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print ("Database does not exist")
    else:
        print (err)

mapNote = sys.argv[1];
roomID = sys.argv[2];
areaName = sys.argv[3];
symbol = sys.argv[4];

insertQuery = ("INSERT INTO MapInterests (Note, RoomID, AreaName, RoomSymbol) VALUES (%s, %s, %s, %s)")
dataQuery = (mapNote, roomID, areaName, symbol )
cursor.execute(insertQuery, dataQuery)
db.commit()

TinTin.showme("<094>--- InterestID [" + str(cursor.lastrowid) + "] added.")

cursor.close()
db.close()

  

