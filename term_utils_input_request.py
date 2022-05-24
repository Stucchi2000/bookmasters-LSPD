
def input_request(dataset):
    criterion = None
    while criterion not in dataset.labels:
        criterion = input(f"------------------------------------------------\nPlease insert which criterion you want me to display... \n Choose among the following: {dataset.labels})\n")
        if criterion not in dataset.labels:
            print(f"{criterion} not recognized please try again...")
    title = None
    while title not in dataset['title'].values:
        title = input(f"------------------------------------------------\nPlease input the title of the book you are looking for:\n")
        if title not in dataset['title'].values:
            result, _ = dataset.search('title', title)
            print(f'Book title {title} not present in dataset...\n\nDid you mean one of these: {result.values}???')
        else:
            break        
    dataset.get_info(title, criterion)
            