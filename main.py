

import argparse
from book_dataset import BookRecords
from term_utils import input_search, input_request, input_suggestion


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, default="./df_books.csv")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    books = BookRecords(args.data_path)
    put = None
    
    while put != 'exit':
        put = input("------------------------------------------------\n------------------------------------------------\n\
                    Input command: \n- search - to look for matching entry in dataset \n- info - to request specific info about of a certain title \n- suggestion - to request a title suggestion \n- exit - to close program...\n\n")
        put = put.lower().strip()
    
        if put == 'search':
            input_search(books)
     
        elif put == 'info':
            input_request(books)
     
        elif put == 'suggestion':
            input_suggestion(books)
          
        elif put == 'exit':
            print("Farewell!")
           
        else:
            print(f"WARNING: {put} not recognized, please type -exit- to close the program...\n\n\n")
        
    return


if __name__ == '__main__':
    main()

