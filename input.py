import yt
import spot
import red

def addSpotify(args):
    spot.add(args[3])

def addYoutube(args):
    yt.add(args[3])

def addSubreddit(args):
    red.add(args[3])

def updateSpotify(args):
    spot.update(args[3])

def updateYoutube(args):
    yt.update(args[3])

def updateSubreddit(args):
    red.update(args[3])

def handleInputAdd(args):
    subcommand = args[2]
    if subcommand == "subreddit":
        addSubreddit(args)
    if subcommand == "youtube":
        addYoutube(args)
    if subcommand == "spotify":
        addSpotify(args)

def handleInputUpdate(args):
    subcommand = args[2]
    if subcommand == "subreddit":
        updateSubreddit(args)
    if subcommand == "youtube":
        updateYoutube(args)
    if subcommand == "spotify":
        updateSpotify(args)

def handleInputDownload(args):
    pass

def handleInput(args):
    command = args[1]
    if command == "add":
        handleInputAdd(args)
    if command == "update":
        handleInputUpdate(args)
    if command == "download":
        handleInputDownload(args)

