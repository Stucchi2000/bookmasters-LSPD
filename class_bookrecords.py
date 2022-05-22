#%%

import os
import sys
import numpy as np
import pandas as pd
from IPython.display import display
#import seaborn as sb


class BookRecords():
    
    def __init__(self, data_path="./df_books.csv"):
        # Check existence of DATA_PATH
        if not os.path.exists(data_path):
            raise AssertionError(f"Provided path \'{data_path}\' doesn\'t exist")
        self.data = pd.read_csv(data_path, sep=';', encoding='latin1', skip_blank_lines=True)
        self.data = self.data.dropna()
        self.labels = self.data.columns.values
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, label):
        # Check existence of column label
        if label not in self.data.columns.values:
            raise AssertionError(f'Column label {label} not present in dataset...')
        return self.data[label]
        
        
        
def main():
    
    books = BookRecords()#data_path='ciao.csv')
    print(books.labels)
    print(len(books))
    print(books['title'])
    
    
        
if __name__=='__main__':
    
    main()
    