
import json
import pandas as pd

import sys


class Data:
    def __init__(self):
        self.instruments ={}
        self.load_instruments()


    def load_instruments(self):  
        with open(r'C:\Users\herma\Documents\Trading\data\instruments.json', 'r') as f:
                self.instruments=json.loads(f.read())
        return self.instruments
                
    def print_instruments(self):  
        with open('./data/instruments.json', 'r') as f:
                data =json.loads(f.read())
                for d in data:
                     print(d)


    def load_candles(self, file):
         data = pd.read_pickle(f'./data/{file}.pkl')
         return data

