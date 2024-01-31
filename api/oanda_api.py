import requests
from constants import defs
import json
import pandas as pd
from dateutil import parser



class OandaApi():

    def __init__(self):
        self.session = requests.Session()
        headers= { "Authorization" : f"bearer {defs.API_KEY}","Content_Type": "application/json"}
        self.session.headers.update(headers)

    def make_request(self, url, verb = "get", code = 200, params = None, data= None, headers=None):
        full_url = f"{defs.URL}/{url}"
        try:
            response = None
            if verb == "get":
                response = self.session.get(full_url, params = params, data = data, headers = headers)

            if response == None:
                return False, {'error': 'verb not found, of iets anders'}
            
            if response.status_code == code:
                return True, response.json()
            else:
                return False, response.json()


        except Exception as error:
            return False, {'Exception': error}
        
    def get_account_ep(self, ep, data_key):
        url = f"accounts/{defs.ACCOUNT_ID_2}/{ep}"
        print(url)
        ok, data = self.make_request(url)

        if ok == True and data_key in data:
            return data[data_key]
        else:
            print("ERROR get_account_ep()", data)
            return None

    def get_account_summary(self):
        return self.get_account_ep("summary", "account")

    def get_account_instruments(self):
        return self.get_account_ep("instruments", "instruments")
    
    def save_instruments(self):
        account_instruments = self.get_account_instruments()
        instruments = {}
        for i in account_instruments:            
            dictje = {"name":i["name"],
                            "i_type":i["type"],
                            "displayName":i["displayName"],
                            "pipLocation":pow(10, i["pipLocation"]),                           
                            "tradeUnitsPrecisiontype":i["tradeUnitsPrecision"],
                            "marginRate":float(i["marginRate"])                         
                            }

            instruments[i["name"]] = dictje
            
            with open('./data/instruments.json', 'w') as f:
                f.write(json.dumps(instruments, indent =2))

    def fetch_candles(self,pair_name, count=10,granularity = "H1"):
        url = f"instruments/{pair_name}/candles"        

        params =  dict(
        granularity = granularity,
        count = count,
        price = "MBA" )
        
        ok, data= self.make_request(url, params = params)
        # print(ok, data)

        if "candles" not in data:
                data =[]
        else:        
            return ok, data
    
    def create_candles_df (self, data):
        candles= data["candles"]   
        if len(candles) == 0:        
            return df.DataFrame()
        else:
            final_data = []
            for candle in candles:
                if candle["complete"] == False:
                    continue
                else:
                    new_dict = {}
                    new_dict["time"] = parser.parse(candle["time"])
                    new_dict["volume"] = candle["volume"]
                    prices = ["bid","mid","ask"]
                    ohlc = ["o","h","l","c"]
                    for p in prices:
                        for x in ohlc:
                            key = f"{p}_{x}"
                            new_dict[key]=float(candle[p][x])
                    
                    final_data.append(new_dict)
            df = pd.DataFrame.from_dict(final_data)
            return df
        
    def create_candles_pickle_file(self, pair_name, count = 10,granularity = "H1" ):
        ok, data = self.fetch_candles(pair_name, count,granularity)
        candles_df = self.create_candles_df(data)
        candles_df.to_pickle(f"./data/{pair_name}_{count}_{granularity}.pkl")
        print(f"Saved to file: {pair_name} {granularity} {candles_df.shape[0]} {candles_df.time.min()} - {candles_df.time.max()}")








    # def create_data_file(self, pair_name, count=10,granularity = "H1"):
    #     code, data = self.fetch_candles(pair_name, count, granularity)
    #     if code != 200:
    #         print("FAILED", pair_name)
    #         return
    #     if len(data) == 0:
    #         print("NO CANDLES", pair_name)
            
    #     candles_df = get_candles_df(data)   
    #     candles_df.to_pickle(f"../data/{pair_name}_{granularity}.pkl")
    #     print(f"Saved to file: {pair_name} {granularity} {candles_df.shape[0]} {candles_df.time.min()} - {candles_df.time.max()}")



       

        


