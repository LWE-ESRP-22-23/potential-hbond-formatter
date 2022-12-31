print("Please enter the minimum HBond distance: ")
minDist = float(input())

print("Please enter the get request URL: ")
url = input()

print("Please enter the desired file name (will be saved to current directory): ")
file_name = input()

from openpyxl import Workbook
import requests
wb = Workbook()
ws = wb.active

def isHead(string):
    if string.find("<-->") > -1:
        return True
    else:
        return False

b = requests.get(url)

data = b.text.split("\n")
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

        if dist < minDist:
            continue

        nextExp.append(split[3])


[ws.append(x) for x in export]

wb.save(file_name + ".xlsx")

print(f"Formatted HBonds have been saved to {file_name}.xlsx")