import database

if __name__ == "__main__":
    database.init()
    testSong = {"url" : "http://www.example.com", "title":"test"}
    database.addSong(testSong)
    print database.getSong()
