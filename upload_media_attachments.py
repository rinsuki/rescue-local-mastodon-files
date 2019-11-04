from spid import genspid
import subprocess
import os
import json
from settings import copy

attachments = json.load(open("./data/media_attachments.json"))
for i, attachment in enumerate(attachments):
    path = "media_attachments/files/"+genspid(attachment["id"])+"original/"+attachment["file_file_name"]
    print(i, path)
    copy(path)
    print()

    ext = attachment["file_file_name"].split(".")[-1]
    path = "media_attachments/files/"+genspid(attachment["id"])+"small/"+attachment["file_file_name"]

    if attachment["file_content_type"].startswith("video/"): # videoの場合、サムネイルはpng
        path = path.replace("." + ext, ".png")

    print(i, path)
    copy(path)
    print()
