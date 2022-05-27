#%%

import os
import sys
import numpy as np
import pandas as pd
from IPython.display import display
#import seaborn as sb


class BookRecords():
    
    def __init__(self, data_path="./df_books.csv"):
        # Check existence of dataset
        if not os.path.exists(data_path):
            raise AssertionError(f"Provided path \'{data_path}\' doesn\'t exist")
        self.data = pd.read_csv(data_path, sep=';', encoding='latin1', skip_blank_lines=True)
        self.data = self.data.dropna()
        self.labels = self.data.columns.values
        
    def __len__(self):
        # Returns the length of the input
        return len(self.data)
    
    def __getitem__(self, label):
        # Check the existance of column label
        if label not in self.data.columns.values:
            raise AssertionError(f'Column label {label} not present in dataset...')
        return self.data[label]
    
    def search(self, label, keyword, out_label=None):
        # Given a keyword searches among a specific column, returns all matching items
        mask = self[label].str.contains(keyword, case=False, regex=False,na=False).values
        if out_label is not None:
            out = self[out_label][mask]
        else:
            out = self[label][mask]
        return out, mask
        
    def get_info(self, title, info):
        # Based on a specific column label returns the info of a given title
        if title not in self['title'].values:
            out = self.search('title', title)
            raise AssertionError(f'Book title {title} not present in dataset...\n\nDid you mean {out[0].values}???')
        summ = self[info][self['title']==title].values
        print(f'--Book Name: \n\t{title}\n\n--{info}: \n\t {summ}\n\n')
        
    def suggestion(self, genre):
        # Returns the dataframe entries matching the given genre
        if genre not in self['genre'].values:
            out = self.search('genre', genre)
            raise AssertionError(f'Book genre {genre} not present in dataset...\n\nDid you mean {out[0].values}???')
        
        return self.data.groupby(['genre']).get_group(genre)
    
           
def main():
    
    books = BookRecords()#data_path='ciao.csv')
    print(books.labels)
    print(len(books))
    print(books.search('title', 'Will'))

if __name__=='__main__':
    
    main()
    