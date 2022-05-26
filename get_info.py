# %%

import os
import sys
import numpy as np
import pandas as pd
from IPython.display import display
# import seaborn as sb


class BookRecords():
    
    def get_info(self, title, info):
        # Check existence of column label
        if title not in self['title'].values:
            out = self.search('title', title)
            raise AssertionError(f'Book title {title} not present in dataset...\n\nDid you mean {out[0].values}???')
        summ = self[info][self['title'] == title].values
        print(f'--Book Name: \n\t{title}\n\n--{info}: \n\t {summ}\n\n')      


def main():
    
    books = BookRecords()
    print(books['title'])
    print(books['category'])
