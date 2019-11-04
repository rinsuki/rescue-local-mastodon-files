from spid import genspid
import subprocess
import os
import json
from settings import copy

avatars = json.load(open("./data/accounts_avatar.json"))
for avatar in avatars:
    path = "accounts/avatars/"+genspid(avatar["id"])+"original/"+avatar["avatar_file_name"]
    copy(path)
