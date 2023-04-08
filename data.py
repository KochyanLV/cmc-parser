import pandas as pd
from parse import Parser

def some_logic(data):
    columns =  ['RANK', 'NAME', 'PRICE', 'MARKET CAP', 'VOLUME(24H)', 'SUPPLY'] 
    df = pd.DataFrame(data = data, columns = columns)
    df.index += 1
    df.to_csv('crypto.csv')
    return df






