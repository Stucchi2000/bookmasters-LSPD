

def input_search(dataset):
    # needed to run search function in main.py
    data = dataset
    while len(data) > 1:
        criterion = None
        while criterion not in data.labels:
            criterion = input(f"------------------------------------------------\nPlease insert which criterion you want to restrict your research to... \n Choose among the following: {data.labels})\n")
            if criterion not in data.labels:
                print(f"{criterion} not recognized please try again...")
        string = input(f"------------------------------------------------\nNow type the string you want to search: \n")
        out_crit = None
        # asking to search based on another criterion
        out_crit = input(f"------------------------------------------------\nDo you want me to list for you the results based on another criterion? \n If yes type one in {data.labels}: \n")
        if out_crit not in data.labels:
            print(f"{out_crit} not recognized...displaying same criterion...")
            out_crit = criterion
        result, indexes = data.search(criterion, string, out_crit)
        data.data = data.data.loc[indexes]
        # asking to refine the search
        if len(data) > 1:
            print(f"------------------------------------------------\nThe search gave {len(data)} matching outputs, do you want to refine the search?")
            cmd = input("Type \n-no- if you want to stop the search\n-display- to display the outputs: \n").lower()
            if cmd == 'no':
                break
            elif cmd == 'display':
                print(f'\nKeyword - {string} - matched: \n\t{result.values}\n\n')
        else:
            print(f'\nKeyword - {string} - matched: \n\t{result.values}\n\n')
 

def input_request(dataset):
    # needed to run get_info function in main.py
    criterion = None
    while criterion not in dataset.labels:
        # asking on which criterion to get the info
        criterion = input(f"------------------------------------------------\nPlease insert which criterion you want me to display... \n Choose among the following: {dataset.labels})\n")
        if criterion not in dataset.labels:
            print(f"{criterion} not recognized please try again...")
    title = None
    while title not in dataset['title'].values:
        # asking for which book you want the info
        title = input(f"------------------------------------------------\nPlease input the title of the book you are looking for:\n")
        if title not in dataset['title'].values:
            result, _ = dataset.search('title', title)
            print(f'Book title {title} not present in dataset...\n\nDid you mean one of these: {result.values}???')
        else:
            break    
    dataset.get_info(title, criterion)


def input_suggestion(dataset):
    # needed to run suggestion function in main.py
    genre = None
    while genre not in dataset.genres:
        genre = input(f"------------------------------------------------\nPlease tell me which is your favourite genre among... \n Choose among the following: {dataset.genres})\n")
        if genre not in dataset.genres:
            print(f"{genre} not recognized please try again...")
    # get suggestion list by genre
    suggs = dataset.suggestion(genre)[['title', 'author','category', 'publication_year', 'page_number', 'rating']]
    opts = ['recent', 'old', 'min_page', 'max_page', 'best', 'worst', 'display']
    if len(suggs) > 1:
        key = None
        while key not in opts:
            # asking on which option to base the suggestion
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
        print(f"My suggestion is... {suggs}")

