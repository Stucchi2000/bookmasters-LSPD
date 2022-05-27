#%%

import os
import sys
import numpy as np
import pandas as pd
from IPython.display import display
#import seaborn as sb


class BookRecords():
    
    def __init__(self, data_path="./df_books.csv"):
        # Check existence of dataset df_books.csv
        if not os.path.exists(data_path):
            raise AssertionError(f"Provided path \'{data_path}\' doesn\'t exist")
        self.data = pd.read_csv(data_path, sep=';', encoding='latin1', skip_blank_lines=True)
        self.data = self.data.dropna()
        self.labels = self.data.columns.values
        
    def __len__(self):
        # Returns the length of the input
        return len(self.data)
    
    def __getitem__(self, label):
        # Checks the existence of column label
        if label not in self.data.columns.values:
            raise AssertionError(f'Column label {label} not present in dataset...')
        return self.data[label]
    
    def get_info(self, title, info):
        # Returns the information of a given item based on a selected label 
        if title not in self['title'].values:
            out = self.search('title', title)
            raise AssertionError(f'Book title {title} not present in dataset...\n\nDid you mean {out[0].values}???')
        summ = self[info][self['title']==title].values
        print(f'--Book Name: \n\t{title}\n\n--{info}: \n\t {summ}\n\n')
    
    def search(self, label, keyword, out_label=None):
        # Search the given keyword over a specific label, returns all matching items
        mask = self[label].str.contains(keyword, case=False, na=False, regex=False).values
        if out_label is not None:
            out = self[out_label][mask]
        else:
            out = self[label][mask]
        return out, mask

    def suggestion(self, genre, label=None):
        """TO FINISH"""
        # Checks the existance of the given genre and category (optinal) 
        if genre not in self['genre'].values:
            out = self.search('genre', genre)
            raise AssertionError(f'Book genre {genre} not present in dataset...\n\nDid you mean {out[0].values}???')
        if label is not None and label not in self['category'].values:
            out = self.search('category', label)
            raise AssertionError(f'Book label {label} not present in dataset...\n\nDid you mean {out[0].values}???')
    
        return self.data.groupby(['genre', 'page_number'])
        
    
        
def main():
    
    books = BookRecords()#data_path='ciao.csv')
    print(books.labels)
    print(len(books))
    print(books['title'])
    print(books.search('author', 'Will'))
    print(books.suggestion('novel'))
if __name__=='__main__':
    
    main()
    