import MySQLdb
import os.path
import sqlite3
import time

conn = sqlite3.connect('musicURLs.db')

def init():
    global conn
    c = conn.cursor()

    # if this is the first time running, create the url table
    tableExists = c.execute("""SELECT *
                FROM sqlite_master
                WHERE
                    type='table'
                    and
                    name ='songs';""").fetchone()
    if not tableExists:
        c.execute(""" CREATE TABLE songs
                    (time_added integer,
                    url text,
                    title text,
                    artist text,
                    album text,
                    genre text""")
    conn.commit()

def addSong(song):
    global conn
    c = conn.cursor()

    if "url" not in song.keys():
        song["url"] = "None"
    if "title" not in song.keys():
        song["title"] = "None"
    if "artist" not in song.keys():
        song["artist"] = "None"
    if "album" not in song.keys():
        if "genre" in song.keys():
            song["album"] = song["genre"]
        else:
            song["album"] = "None"
    if "genre" not in song.keys():
        song["genre"] = "None"

    timeStamp = int(time.time() * 100)

    insertTuple = (timeStamp, song["url"], song["title"], song["artist"], song["album"], song["genre"])

    c.execute('INSERT INTO songs VALUES (?,?,?,?,?,?)', insertTuple)
    conn.commit()

def getSong():
    global conn
    c = conn.cursor()

    c.execute("""SELECT * FROM songs WHERE time_added = 
                (SELECT MIN(time_added) FROM SONGS)""")

    data = c.fetchone()

    song = {}
    song["url"] = str(data[1])
    song["title"] = str(data[2])
    song["artist"] = str(data[3])
    song["album"] = str(data[4])
    song["genre"] = str(data[5])

    return song
                

