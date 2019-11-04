from spid import genspid
import subprocess
import os
import json
from settings import copy

avatars = json.load(open("./data/accounts_header.json"))
for avatar in avatars:
    path = "accounts/headers/"+genspid(avatar["id"])+"original/"+avatar["header_file_name"]
    copy(path)
