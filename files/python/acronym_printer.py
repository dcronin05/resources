try:
    acronym = input('Enter your word ("q" to quit): ')
    while acronym != 'q':
        for i in range(len(acronym)):
            print('[' + str.upper(acronym[i]) + ']')
        acronym = input('Enter your word ("q" to quit): ')
except:
    print('Error: ')
