# bookmasters-LSPD

## The project

The purpose of the Bookmasters project is to create a simple interface that when it comes to reading everyone willing to search for information about books could get them by using such tool.

## Installation

Use the command git clone https://github.com/Stucchi2000/bookmasters-LSPD.git in the bash of your computer to locally download the git repository containing all the packages and modules. The libraries required to properly run the programs are:

os
sys
pandas
numpy
argparse
Ipython.display  

## Dataset

- *df_books.csv*

The dataset is composed by 41 entries and 8 columns, providing information about title, author, summary and others.

## Modules

### bookrecords.py 

The module contains a Python class, named BookRecords() which has been used to store the functions we needed. The functions developed are three. 

 - **The search():** function returns all the dataset entries over one column matching a given keyword. Optionally it can also override the output column with another column and provide the corresponding index matching elements.

- **The get_info():** function returns, given a specific column label, the entry of the asked book

- **The suggestion():** function returns a series of all the unique entries in dataset column genre

 
### term_utils.py

The module contains three functions which are needed to interact with the program and trigger the right user input request to guide him to what they want.

- **input_request:** is a function that serves to guide the user when he chooses the info option among the ones proposed.
It searches for the input criterion over the dataset columns and if any are found it asks you again,  if it is present instead it asks for the book title you are looking for, if not present among the books available it returns the first result of the search function output with the same inputs otherwise it returns the required data.

- **input_search():** is a function which is needed to interact with the program when choosing the search option among the ones proposed.
Asks the user to chose among what columns to restrict the search if not present, it asks yo to try again, then it asks you what keyword you want to search if any match is found it provides you with the number of matches either you can stop the search or display everything and continue refining the search until there's only one match.

- **input_suggestion():** function asks you genre you are interested in, if not present asks it again. Then it asks you which option you would like to choose among the available ones, if recent it'll return the most recent book of the category. The options are max_page to get longest, min_page to get the shortest, old to get the oldest and so on. 


## Main

The main.py file is the Python script meant to allow the user-application interaction. This should be the last file of the three to be run and once done your bash shell should look like this: 


<img width="433" alt="Starting point" src="https://user-images.githubusercontent.com/94078126/170876285-644c148e-b691-4e69-8476-80d7149f221a.png">


You will have four options to choose among. 

- **Search:** will allow you to search for info in the dataset with the help of the search and input_search functions. 

- **Info:** allows you to get specific information about a book, anything that is contained in the dataset obviously. 

- **Suggestion:** Last functionality helps you in search within the available genre any book you'd like based in a specific criterion for example a short story. 

## Possible use cases 

- **Question1:** Can I find all books within the dataset which authors name has W in it? 


<img width="669" alt="Search input" src="https://user-images.githubusercontent.com/94078126/170876321-4d81c67d-4b9c-40a1-9267-063a92e945db.png">

  
- **Question2** In which category the book "1984" lies? 


<img width="664" alt="Info input" src="https://user-images.githubusercontent.com/94078126/170876356-eaaf0ac9-5e33-45ed-97c7-3b1432bcbe1b.png">

  
- **Question3** What is the oldest avaliable novel written?


<img width="686" alt="Suggestion input" src="https://user-images.githubusercontent.com/94078126/170876373-ba9897d6-9970-4685-8c21-0bece55ee538.png">



