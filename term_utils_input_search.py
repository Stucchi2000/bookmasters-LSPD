

def input_search(dataset):
    data = dataset
    while len(data)>1:
        criterion = None
        while criterion not in data.labels:
            criterion = input(f"------------------------------------------------\nPlease insert which criterion you want to restrict your research to... \n Choose among the following: {data.labels})\n")
            if criterion not in data.labels:
                print(f"{criterion} not recognized please try again...")
        string = input(f"------------------------------------------------\nNow type the string you want to search: \n")
        out_crit = None
        #while out_crit not in data.labels:
        out_crit = input(f"------------------------------------------------\nDo you want me to list for you the results based on another criterion? \n If yes type one in {data.labels}: \n")
        if out_crit not in data.labels:
            print(f"{out_crit} not recognized...displaying same criterion...")
            out_crit = criterion
        result, indexes = data.search(criterion, string, out_crit)
        data.data = data.data.loc[indexes]
        if len(data)>1:
            print(f"------------------------------------------------\nThe search gave {len(data)} matching outputs, do you want to refine the search?")
            cmd = input("Type \n-no- if you want to stop the search\n-display- to display the outputs: \n").lower()
            if cmd == 'no':
                break
            elif cmd == 'display':
                print(f'\nKeyword - {string} - matched: \n\t{result.values}\n\n')
        else:
            print(f'\nKeyword - {string} - matched: \n\t{result.values}\n\n')
