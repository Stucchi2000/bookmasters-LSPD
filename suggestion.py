def suggestion(self, genre, category=None):
    """TO FINISH"""
    # Check existence of column label
    if genre not in self['genre'].values:
        out = self.search('genre', genre)
        raise AssertionError(f'Book genre {genre} not present in dataset...\n\nDid you mean {out[0].values}???')
    if category is not None and category not in self['category'].values:
        out = self.search('category', category)
        raise AssertionError(f'Book category {category} not present in dataset...\n\nDid you mean {out[0].values}???')
    
    return self.data.groupby(['genre', 'page_number'])