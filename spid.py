import re

def genspid(id: int):
    return re.sub('([0-9]{3})', '\\1/', format(id, "09d"))