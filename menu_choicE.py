menu_choice =''
while menu_choice !='z':
    menu_choice = input('Welcome to the Netflix Series database\n\b'
                        'Type the letter for the information you want:\n'
                        'A: All the music Netflix series database.\n'
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
        print_query('arrange the seasons from smallest first')
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
        print_query('speaks English')
    if menu_choice == 'K':
        print_query('speaks Korean')
    
