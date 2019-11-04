from spid import genspid
import subprocess
import os
import json
from settings import copy

attachments = json.load(open("./data/custom_emojis.json"))
for i, attachment in enumerate(attachments):
    path = "custom_emojis/images/"+genspid(attachment["id"])+"original/"+attachment["image_file_name"]
    print(i, path)
    copy(path)
    print()

    path = "custom_emojis/images/"+genspid(attachment["id"])+"static/"+attachment["image_file_name"]
    print(i, path)
    copy(path)
    print()
