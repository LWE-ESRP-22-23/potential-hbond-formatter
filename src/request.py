import requests
url = "https://swift.cmbi.umcn.nl/cgi/GenericCGI.py"

def requestServer(file:str):
    payload={'request': 'allhbonds',
    '&PDB1': '',
    'SubmitButton': 'Send'}
    files=[
    ('&FIL1',('5N4L_1101.pdb',open(file,'rb'),'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response = response.text[response.text.find("GenericCGI.py") + 13:response.text.find("\"", response.text.find("GenericCGI.py?") + 13)]

    return requests.get(url + response).text