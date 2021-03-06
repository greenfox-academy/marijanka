from sys import *
from main import *
from open_write import *
from lists import *
from removes import *
import os
from menu import *


def help():
    #os.system('clear') # on linux / os x
    os.system('cls')  # on windows
    open_file = open('help.txt')
    open_text = open_file.read()
    open_file.close()
    print(open_text)

if len(argv) != 1 and len(argv) < 4:
    if (argv[1] == 'add'):
        if len(argv) == 3:
            add_todo(argv[2])
        else:
            add_todo()
    elif argv[1] == 'st':
            list_todo_all()
    elif (argv[1] == 'ls'):
        if len(argv) == 3 and argv[2] == '-l':
            list_todo_ch()
        elif len(argv) == 3 and argv[2] == '-la':
            list_todo_all()
        elif len(argv) == 3 and argv[2] == '-ch':
            list_todo_only_ch()
        else:
            list_todo()
    elif (argv[1] == 'rm'):
        if len(argv) == 3 and argv[2] == '-r':
            remove_todo()
        elif len(argv) == 3 and argv[2] == '-rf':
            remove_todo_ultimate()
        else:
            remove_todo()
    elif (argv[1] == 'ch'):
        completed_todo()
    elif (argv[1] == 'uch'):
        uncompleted_todo()
    elif (argv[1] == '--help'):
        help()
    elif (argv[1]) == '--version':
        print('TODO for Developers version 0.1')
    elif (argv[1] == 'del'):
        delete_database()
    elif (argv[1] == 'src'):
        search_todo()
    elif (argv[1] == '--menu'):
        clear()
        #os.system('clear') # on linux / os x
        os.system('cls')  # on windows
        menu_input(True)
    else:
        print('Invalid syntax')
else:
    help()
