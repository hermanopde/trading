import requests
import json
from constants import defs

aa = defs.API_KEY
print(aa)

URL = defs.URL
API_KEY = defs.API_KEY
ACOOUNT_ID_1 = defs.ACOOUNT_ID_1
ACOOUNT_ID_2 = defs.ACCOUNT_ID_2

session = requests.Session()

headers= {
    "Authorization" : f"bearer {API_KEY}",
    "Content_Type": "application/json"
}


#SEND HEADERS WITH EVRY REQUEST
session.headers.update(headers)


params =  dict(
    granularity = "H4",
    count = 10,
    price = "MBA"    
)



#respons= session.get(url, params = params) 
# #print(dir(r))
#rint(respons.json())

def fetch_candles(pair_name, count=10,granularity = "H1"):
    url = f"{URL}/instruments/{pair_name}/candles"
    
    params =  dict(
    granularity = granularity,
    count = count,
    price = "MBA" )
    
    respons= session.get(url, params = params)
    data = respons.json()
    if respons.status_code == 200:
        if "candles" not in data:
            data =[]
        else:
             data =data["candles"]

    
    return respons.status_code , data


code, data = fetch_candles("EUR_USD")
print(code, data[0])

final_data = []
for candle in data:
    if candle["complete"] == False:
        continue
    else:
        new_dict = {}
        new_dict["time"] = candle["time"]
        new_dict["volume"] = candle["volume"]
    final_data.append(new_dict)


