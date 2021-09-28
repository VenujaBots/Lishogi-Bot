import re

# USI

def isusi(move):
    return bool(re.match("([1-9][a-i][1-9][a-i]\+?$)|([PLNSGBR]\*[1-9][a-i]$)", move))

# Makes sure the move is USI

def makeusi(move) -> str:
    return move
