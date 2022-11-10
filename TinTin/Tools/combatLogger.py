import sys
import mysql.connector
import mysql.connector
from mysql.connector import errorcode
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

averageDamage = sys.argv[1];
averagePerHit = sys.argv[2];
brawler = sys.argv[3];
currentRoom = sys.argv[4];
maxHit = sys.argv[5];
minHit = sys.argv[6];
mob = sys.argv[7];
palm = sys.argv[8];
pressure = sys.argv[9];
rating = sys.argv[10];
scaler = sys.argv[11];
totalDamage = sys.argv[12];
totalHits = sys.argv[13];
strength = sys.argv[14];
dex = sys.argv[15];
wis = sys.argv[16];
intelligence = sys.argv[17];
con = sys.argv[18];
cha = sys.argv[19];
speed = sys.argv[20];
power = sys.argv[21];
stance = sys.argv[22];
dmgType = sys.argv[23];
insight = sys.argv[24];
rounds = sys.argv[25];

if not currentRoom:
    currentRoom = -1
if not maxHit:
    maxHit = -1
if not minHit:
    minHit = -1
if not palm:
    palm = 0
if not pressure:
    pressure = 0
if not rating:
    rating = -1

insertQuery = ("INSERT INTO CombatLog (AverageDamage, AveragePerHit, BrawlerActive, RoomID, MaxHit, MinHit, Mob, PalmActive, PressureActive, Rating, Scaler, TotalDamage, TotalHits, Strength, Dex, Wis, Intelligence, Con, Cha, Speed, Power, InsightActive, Stance, DamageType, Rounds ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
dataQuery = (averageDamage, averagePerHit, brawler, currentRoom, maxHit, minHit, mob, palm, pressure, rating, scaler, totalDamage, totalHits, strength, dex, wis, intelligence, con, cha, speed, power, insight, stance, dmgType, rounds )
cursor.execute(insertQuery, dataQuery)


db.commit()

cursor.close()
db.close()

