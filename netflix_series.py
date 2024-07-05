# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'netflix_series.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice =''
while menu_choice !='Z':
    menu_choice = input('Welcome to the Netflix Series database\n\b'
                        'Type the letter for the information you want:\n'
                        'A: All the Netflix series database.\n'
                        'B: Seasons arranged from smallest to biggest.\n'
                        'C: Brief information about the Netflix database.\n'
                        'D: Netflix Series whose genre is fantasy.\n'
                        'E: Latest to oldest Netflix Series.\n'
                        'F: Series that has less than 50 episodes.\n'
                        'G: Series that has more than 5 seasons.\n'
                        'H: Series that were released after 2020.\n'
                        'I: Series that were released before 2020.\n'
                        'J: Series that speaks English.\n'
                        'K: Series that speaks Korean.\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('all data')
    if menu_choice == 'B':
        print_query('arrange the seasons')
    if menu_choice == 'C':
        print_query('brief info')
    if menu_choice == 'D':
        print_query('fantasy series')
    if menu_choice == 'E':
        print_query('latest to oldest')
    if menu_choice == 'F':
        print_query('less than 50 episodes')
    if menu_choice == 'G':
        print_query('more than 5 seasons')
    if menu_choice == 'H':
        print_query('released after 2020')
    if menu_choice == 'I':
        print_query('released before 2020')
    if menu_choice == 'J':
        print_query('English language')
    if menu_choice == 'K':
        print_query('Korean language')