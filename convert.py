import json
import os

filename = "transcript.csv"
PERMITTED_CHARS = "0123456789абвгдеёжзиклмнопрстуфхцчшщъыьэюя-!?:., " 

def hasNumber(s):
    return any(i.isdigit() for i in s)

with open('train.json') as json_data:
    d = json.load(json_data)

with open(filename, 'w') as outfile:
    for el in d["train"]:        
        path = el["basename"]
        text = el["text"].lower()
        if (not hasNumber(text) and len(text) < 200):
            text = "".join(c for c in text if c in PERMITTED_CHARS)
            lastPathEl = path.split('/')[-1]
            outfile.write(lastPathEl + "|" + text + "|" + text + "\n")