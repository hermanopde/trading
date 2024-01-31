import sys
import pandas as pd
import datetime as dt
import plotly.graph_objects as go
from exploration.plotting import CandlePlot

sys.path.append("../")

from infrastructure.instruments import Data
import openpyxl



class MovingAverage():
    def __init__(self, pair ="EUR_USD", granularity="H1"):
        self.pair = pair
        self.granularity = granularity
        
        self.df = pd.read_pickle(f"C:\\Users\\herma\\Documents\\Trading\\data\\{pair}_{granularity}.pkl")
        self.df_ma = self.df[['time','mid_o', 'mid_h',
       'mid_l', 'mid_c']].copy()
        self.ma_list = [6,10,20,50,80,200]    
        self.instr = Data()
        self.pip = self.instr.instruments[self.pair]["pipLocation"]
        



    def add_ma(self,s=10,m=20,l=50,expon=False, end_trade =4):
        if expon == False:
            self.df_ma[f"MA_S"]=self.df_ma.mid_c.rolling(window=s).mean()
            self.df_ma[f"MA_M"]=self.df_ma.mid_c.rolling(window=m).mean()
            self.df_ma[f"MA_L"]=self.df_ma.mid_c.rolling(window=l).mean()    
        else:
            self.df_ma[f"MA_S"]=self.df_ma.mid_c.ewm(span= s, adjust = False).mean()
            self.df_ma[f"MA_M"]=self.df_ma.mid_c.ewm(span= m, adjust = False).mean()
            self.df_ma[f"MA_L"]=self.df_ma.mid_c.ewm(span= l, adjust = False).mean() 



        self.df_ma["DELTA_S_M"]= self.df_ma["MA_S"]- self.df_ma["MA_M"]
        self.df_ma["DELTA_PREV_S_M"]= self.df_ma["DELTA_S_M"].shift(1)

        self.df_ma["MA_M_PREV"]= self.df_ma["MA_L"].shift(1)
        self.df_ma["DELTA_M"]= self.df_ma["MA_M_PREV"]*1000- self.df_ma["MA_M"]*1000

        self.df_ma["MA_L_PREV"]= self.df_ma["MA_L"].shift(1)
        self.df_ma["DELTA_L"]= self.df_ma["MA_L_PREV"]*1000- self.df_ma["MA_L"]*1000

        self.df_ma["TREND_L"] = self.df_ma.apply(self.trend_l, axis =1) 
        self.df_ma["TREND_M"] = self.df_ma.apply(self.trend_m, axis =1)
        
        self.df_ma["SHORT_TR_L"] = self.df_ma.apply(self.short_trade_trend_l, axis =1)
        self.df_ma["SHORT_TR_M"] = self.df_ma.apply(self.short_trade_trend_m, axis =1)
        self.df_ma["LONG_TR_L"] = self.df_ma.apply(self.long_trade_trend_l, axis =1)
        self.df_ma["LONG_TR_M"] = self.df_ma.apply(self.long_trade_trend_m, axis =1)        

        self.df_ma["END_TRADE"]= self.df_ma.mid_c.shift(-end_trade)

        self.df_ma["RES_SHORT"] = (self.df_ma["mid_c"] - self.df_ma["END_TRADE"]) /self.pip *1
        self.df_ma["RES_LONG"] = (self.df_ma["mid_c"] - self.df_ma["END_TRADE"]) /self.pip *-1

        self.df_ma.dropna(inplace=True)
        self.df_ma.reset_index(drop = True, inplace=True)

        


    def trend_l (self, row, delta = 0.05):
        if  abs(row["DELTA_L"]) <= delta:
            return "NONE"
        elif row["MA_L_PREV"] - row["MA_L"] <= 0 :
            return "BUL"
        else:
            return "BEAR"
    
    def trend_m (self, row, delta = 0.05):
        if  abs(row["DELTA_M"]) <= delta:
            return "NONE"
        elif row["MA_M_PREV"] - row["MA_M"] <= 0 :
            return "BUL"
        else:
            return "BEAR"

    
    
    def short_trade_trend_l (self,row):
        if  row["DELTA_PREV_S_M"] >= 0 and row["DELTA_S_M"] < 0 and row["TREND_L"] =="BEAR":        
            return 1 
        else:
            return 0
    
    def short_trade_trend_m (self,row):
        if  row["DELTA_PREV_S_M"] >= 0 and row["DELTA_S_M"] < 0 and row["TREND_M"] =="BEAR":        
            return 1 
        else:
            return 0

    def long_trade_trend_l (self,row):
        if  row["DELTA_PREV_S_M"] <= 0 and row["DELTA_S_M"] > 0 and row["TREND_L"] =="BUL":        
            return 1 
        else:
            return 0
    
    def long_trade_trend_m (self,row):
        if  row["DELTA_PREV_S_M"] <= 0 and row["DELTA_S_M"] > 0 and row["TREND_M"] =="BUL":        
            return 1 
        else:
            return 0

        
    
    


