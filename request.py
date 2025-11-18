### Example File to interact with FAST API XGBClassifier model efficiently

import requests

url = "http://localhost:9696/predict"

### payload contains features to pass to FAST API. See README.md for general feature description and constraints
payload = {
    "age": 73.0,               ##age: years (greater > 0, less < 120)
    "bp": 70.0,               ## p: blood pressure (greater > 0)
    "sg": 1.005,            ## sg: specific gravity (greater > 0)
    "al": 0.0,             ## al: albumin (greater > 0)
    "su": 0.0,            ## su: sugar (greater > 0)
    "pcc": "notpresent",    ## pcc: pus cell clumps ["notpresent", "present"]
    "ba": "notpresent",    ## ba: bacterial ["notpresent", "present"]
    "bgr": 70.0,           ## bgr: blood glucose random (greater > 0)
    "bu": 32.0,           ## bu: blood urea (greater > 0)
    "sc": 0.9,          ## sc: serum creatinine (greater > 0)
    "sod": 125.0,      ## sod: sodium (greater > 0)
    "pot": 4.0,        ## pot: potassium (greater > 0)
    "hemo": 10.0,      ## hemo: hemoglobin (greater > 0)
    "pcv": 29.0,       ## pcv: packed cell volume (greater > 0)
    "wbcc": 18900.0,    ## wbcc: white blood cell count (greater > 0)
    "rbcc": 3.5,       ## rbcc: red blood cell count (greater > 0)
    "htn": "yes",     ## htn: hypertension ["yes", "no"]
    "dm": "yes",     ## dm: diabetes ["yes", "no"]
    "cad": "no",    ## cad: coronary artery disease ["yes", "no"]
    "appet": "good",    ## appet: appetite ["good", "poor"]
    "pe": "yes",      ## pe: pedal edema ["yes", "no"]
    "ane": "no"       ## ane: anemia ["yes", "no"]

}

response = requests.post(url, json=payload)


print(response.json())

