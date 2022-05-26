def input_suggestion(dataset):
    genre = None
    while genre not in dataset.genres:
        genre = input(f"------------------------------------------------\nPlease tell me which is your favourite genre among... \n Choose among the following: {dataset.genres})\n")
        if genre not in dataset.genres:
            print(f"{genre} not recognized please try again...")
    # get suggestion list by genre
    suggs = dataset.suggestion(genre)[['title', 'author', 'category', 'publication_year', 'page_number', 'rating']]
    opts = ['recent', 'old', 'min_page', 'max_page', 'best', 'worst', 'display']
    if len(suggs) > 1:
        key = None
        while key not in opts:  #dataset.labels.append('display'):
            key = input(f"------------------------------------------------\nType:\n\n- recent - for most recent title\n- old - for oldest title\n- max_page - for maximum page number\n- min_page - for minimum page number\n- best - for best book\n- worst - for worst book\n- display - if you want me to show all of them\n\n")
            if key not in opts:
                print(f"Input {key} not recognized, please try again...")
    if key == 'recent':
        print(f"My suggestion is...{suggs.loc[suggs['publication_year'].astype(int).idxmax()]}\n")
    elif key == 'old':
        print(f"My suggestion is...{suggs.loc[suggs['publication_year'].astype(int).idxmin()]}\n")
    elif key == 'min_page':
        print(f"My suggestion is...{suggs.loc[suggs['page_number'].astype(int).idxmin()]}\n")
    elif key == 'max_page':
        print(f"My suggestion is...{suggs.loc[suggs['page_number'].astype(int).idxmax()]}\n")
    elif key == 'best':
        print(f"My suggestion is...{suggs.loc[suggs['rating'].astype(int).idxmax()]}\n")
    elif key == 'worst':
        print(f"My suggestion is...{suggs.loc[suggs['rating'].astype(int).idxmin()]}\n")
    elif key == 'display':
        print(f"Displaying all results \n{suggs}\n")
         
    else:
        print(f"My suggestion is...{suggs}")
