import hashlib
import os
import json
import csv
from datetime import datetime
def get_hash(filepath):
    with open(filepath,"rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
folder = "my_files"
new_hashes = {}
for file in os.listdir(folder):
    path = os.path.join(folder,file)
    if os.path.isfile(path):
        new_hashes[file] = get_hash(path)
if os.path.exists("folder_hashes.json"):
    with open("folder_hashes.json","r") as f:
        old_hashes = json.load(f)
else:
    print("[info] Pehli baar chal rha hy golden bann rha hy!")
    old_hashes = {}
report = []
for file , old_hash in old_hashes.items():
    if file not in new_hashes:
        print(f"[Deleted] {file} delete ho gy hy!")
        report.append([datetime.now(),file,"Deleted"])
    elif new_hashes[file]==old_hash:
        print(f"[Safe] {file} safe hy!")
        report.append([datetime.now(),file,"Safe"])
    else:
        print(f"[Alert] {file} alert aya hy!")
        report.append([datetime.now(),file,"Alert"])
for file , new_hash in new_hashes.items():
    if file not in old_hashes:
        print(f"[New] {file} add hye hy!")
        report.append([datetime.now(),file,"New"])
with open("report.csv","w",newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(["Time","File","Status"])
    writer.writerows(report)
with open("folder_hashes.json","w") as f:
    json.dump(new_hashes,f,indent = 4)
