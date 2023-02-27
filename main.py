# Initialization

from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from openpyxl import Workbook
import requests

wb = Workbook()
ws = wb.active

url = "https://swift.cmbi.umcn.nl/cgi/GenericCGI.py"

# Ask

maxDist = float(input("Please enter the maximum HBond distance: "))

print("Please select the desired save location:")
save_file = asksaveasfile(initialfile = 'Untitled.xlsx', defaultextension=".xlsx", filetypes=[("Excel","*.xlsx*")]).name

print("Please select the PDB file:")
pdb_file = filedialog.askopenfilename()

# Request

payload={'request': 'allhbonds',
'&PDB1': '',
'SubmitButton': 'Send'}
files=[
  ('&FIL1',('5N4L_1101.pdb',open(pdb_file,'rb'),'application/octet-stream'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
response = response.text[response.text.find("?"):]
response = response[0:response.find("\"")]

finalResponse = requests.get(url + response)

# Interpret

def isHead(string):
    if string.find("<-->") > -1:
        return True
    else:
        return False


data = finalResponse.text.split("\n")
del data[0:8], data[len(data) - 1]

ws.append(["Ligand (Source...Target)", "Bond Distance"])

export = []

nextExp = []
for i in range(len(data)):
    
    if isHead(data[i]):
        if len(nextExp) > 1:
            export.append(nextExp.copy())
            nextExp.clear()
        elif len(nextExp) > 0:
            nextExp.clear()

        data[i] = data[i].replace("(", " ")
        data[i] = data[i].replace(")", " ")
        split = data[i].split(" ")
        for n in range(len(split) - 1, -1, -1):
            if split[n] == "":
                del split[n]
                continue
            
            hasR = split[n].find("\r")
            if hasR > -1:
                split[n] = split[n].replace("\r", "")

        out = "{0} {1} ({2}) {4}...{6} {7} ({8}) {10}".format(*split)
        nextExp.append(out)
    else:
        if len(nextExp) > 1:
            export.append(nextExp.copy())
            nextExp.clear()
            nextExp.append("")
        
        data[i] = data[i].replace("(", " ")
        data[i] = data[i].replace(")", " ")
        split = data[i].split(" ")
        
        for n in range(len(split) - 1, -1, -1):
            if split[n] == "":
                del split[n]
                continue
            
            hasR = split[n].find("\r")
            if hasR > -1:
                split[n] = split[n].replace("\r", "")
        dist = float(split[3])

        if dist > maxDist:
            continue

        nextExp.append(split[3])


[ws.append(x) for x in export]

wb.save(save_file)

print(f"Formatted HBonds have been saved to {save_file}")