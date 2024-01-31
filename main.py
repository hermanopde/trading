import requests
import json
from api.oanda_api import OandaApi
import sys
from infrastructure.instruments import Data
from strategies.ma_cross import MovingAverage, an_ma
import pandas as pd

d = Data()
    
d.instruments

if "EUR_USD" in d.instruments.keys():
      print("yes")
#print(sys.path)
#[print(x) for x in sys.path]



# def an_ma(curr= ["USD","EUR"], gran= ["H1","H4"], end= [4], tr=["short", "long"] ):
#         dict_res = {"pair":[],
#                   "res_pips":[]
#                   }
        
#         for c1 in curr:
#               for c2 in curr:
#                 p_p= f"{c1}_{c2}"                                         
#                 if p_p in d.instruments.keys():
#                      for g in gran:
#                         for e in end:
#                             for t in tr: 
#                                 p_t= f"{c1}_{c2}_{g}_{e}_{t}"
#                                 dict_res["pair"].append(p_t)
#                                 if t == "short":
#                                     r_s = calc_res_short(p_p,g,e) 
#                                     dict_res["res_pips"].append(int(r_s))
#                                 else:    
#                                     r_l = calc_res_long(p_p,g,e) 
#                                     dict_res["res_pips"].append(int(r_l)) 
                                                                     
        
#         df = pd.DataFrame(dict_res)                        
#         print(df)
#         # ma = MovingAverage(pair ="EUR_USD", granularity="H4")
#         # ma.add_ma(s=20, m=50,l=200, expon=False, end_trade =16)
#         # df_short_trades = ma.df_ma[ma.df_ma["SHORT_TR_L"] == 1].copy()
#         # df_long_trades = ma.df_ma[ma.df_ma["LONG_TR_L"] == 1].copy()
#         # df_short_trades["cum"] = df_short_trades.RES_SHORT.cumsum()
#         # df_long_trades["cum"] = df_long_trades.RES_LONG.cumsum()

#         # i_s =df_short_trades.tail(1).index[0]
#         # res_s = df_short_trades.loc[i_s,"cum"]

#         # i_l =df_long_trades.tail(1).index[0]
#         # res_l = df_long_trades.loc[i_l,"cum"]

#         # return res_s, res_l


# def calc_res_short(pair, granularity, end_trade):
#     ma = MovingAverage(pair =pair, granularity=granularity)
#     ma.add_ma(s=10, m=20,l=50, expon=False, end_trade =end_trade)
#     df_short_trades = ma.df_ma[ma.df_ma["SHORT_TR_L"] == 1].copy()
#     df_long_trades = ma.df_ma[ma.df_ma["LONG_TR_L"] == 1].copy()
#     df_short_trades["cum"] = df_short_trades.RES_SHORT.cumsum()
#     df_long_trades["cum"] = df_long_trades.RES_LONG.cumsum()

#     i_s =df_short_trades.tail(1).index[0]
#     res_s = df_short_trades.loc[i_s,"cum"]   

#     return res_s

# def calc_res_long(pair, granularity,end_trade):
#     ma = MovingAverage(pair =pair, granularity=granularity)
#     ma.add_ma(s=10, m=20,l=50, expon=False, end_trade =end_trade)
#     df_short_trades = ma.df_ma[ma.df_ma["SHORT_TR_L"] == 1].copy()
#     df_long_trades = ma.df_ma[ma.df_ma["LONG_TR_L"] == 1].copy()
#     df_short_trades["cum"] = df_short_trades.RES_SHORT.cumsum()
#     df_long_trades["cum"] = df_long_trades.RES_LONG.cumsum()

#     try:
#         i_l =df_long_trades.tail(1).index[0]
#         res_l = df_long_trades.loc[i_l,"cum"]
#         return res_l
#     except:
#          return 0

   


if __name__ == "__main__":
    
    #api = OandaApi()
    
    #sum =api.get_account_instruments()
    
    # [print(x["name"]) for x in sum]
    # print(sum) 
    # api.save_instruments()
    # account_instruments.create_file()
   

    #print(d.instruments["EUR_USD"])
    # d.load_instruments()
    # d.print_instruments()
    # x,candles =api.fetch_candles("EUR_JPY", count = 5, granularity="H1")
    
    # print("X", x)   
    
    # api.create_candles_df(candles)
    # ma = MovingAverage(pair ="EUR_USD", granularity="H1")
    # ma.add_ma(s=10,m=20,l=50, expon=True, end_trade =4)
    # print(ma.df_ma.head())
    # ma.short_trade()


    
    
    an_ma()
    #print(int(s),int(l))
    
   
    
    
    

    



