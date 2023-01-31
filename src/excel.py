from openpyxl import Workbook

export = []

wb = Workbook()
ws = wb.active

def addExport(add):
    export.append(add)

def save(location:str, clear:bool=True):
    global export
    [ws.append(x) for x in export]
    wb.save(location)

    if clear:
        export = []