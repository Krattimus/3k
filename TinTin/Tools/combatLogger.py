import os
import sys
import mysql.connector
from mysql.connector import errorcode
from baseDatabase import BaseDatabase

db3k = BaseDatabase()

averageDamage = sys.argv[1]
averagePerHit = sys.argv[2]
brawler = sys.argv[3]
currentRoom = sys.argv[4]
maxHit = sys.argv[5]
minHit = sys.argv[6]
mob = sys.argv[7]
palm = sys.argv[8]
pressure = sys.argv[9]
rating = sys.argv[10]
scaler = sys.argv[11]
totalDamage = sys.argv[12]
totalHits = sys.argv[13]
strength = sys.argv[14]
dex = sys.argv[15]
wis = sys.argv[16]
intelligence = sys.argv[17]
con = sys.argv[18]
cha = sys.argv[19]
speed = sys.argv[20]
power = sys.argv[21]
stance = sys.argv[22]
dmgType = sys.argv[23]
insight = sys.argv[24]
rounds = sys.argv[25]

if not brawler:
    brawler = 0
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
if not scaler:
    scaler = 0
if not rounds:
    rounds = 1
if not dmgType:
    dmgType = "Normal"
if not totalHits:
    totalHits = 1
if not totalDamage:
    totalDamage = 1

    
insertQuery = ("INSERT INTO CombatLog (AverageDamage, AveragePerHit, BrawlerActive, RoomID, MaxHit, MinHit, Mob, PalmActive, PressureActive, Rating, Scaler, TotalDamage, TotalHits, Strength, Dex, Wis, Intelligence, Con, Cha, Speed, Power, InsightActive, Stance, DamageType, Rounds ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

combatID = db3k.insert(insertQuery, [averageDamage, averagePerHit, brawler, currentRoom, 
    maxHit, minHit, mob, palm, pressure, rating, scaler, totalDamage, totalHits, 
    strength, dex, wis, intelligence, con, cha, speed, power, insight, stance, dmgType, rounds] )
    
db3k.dispose()

