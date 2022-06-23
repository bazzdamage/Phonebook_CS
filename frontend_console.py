from pathlib import Path
from backend import read_from_file as rff
from backend import add_record as ar
from backend import write_record_to_file as wrtf
from backend import format_to_csv as f_csv
flag = ''
opened_file = ''


def main():
    global flag
    global opened_file
    opened_file = ''
    flag = 'main'
    print('Phonebook by CodeShavers salute you')
    print('\ntype "show" to see existing phonebooks')
    while True:
        command_processor(input_commands_with_check())


def input_commands_with_check():
    global flag
    print(f'\n--> you are in -={flag} menu=-')

    commands = ['quit']
    if flag == "export":
        commands = ['csv', 'help', 'return']
    elif flag == "show":
        commands = ['export', 'open', 'create', 'delete', 'return', 'help']
    elif flag == "read":
        commands = ['add', 'del', 'find', 'return', 'view', 'help']
    elif flag == "help":
        commands = ['return']
    else:
        flag = "main"
        commands = ['show', 'quit', 'help']
    while True:
        user_in = input('\ntype command or help: \n')
        if user_in.lower() in commands:
            return user_in.lower()
        else:
            print(f'{user_in} are unrecognized command')


def command_processor(command: str):
    if command == 'quit':
        return quit()
    if command == 'show':
        return file_manager()
    if command == 'help':
        return help_menu(flag)
    if command == 'return':
        return main()
    if command == 'open':
        f = input('input filename:\n')
        ext = 'txt'
        return open_existing_file(f, ext)
    if command == 'create':
        f = input('input filename:\n')
        ext = 'txt'
        create_new_file(f, ext)
        return file_manager()
    if command == 'add':
        f, e = opened_file
        input_info_for_record(f, e)
    if command == 'view':
        f, e = opened_file
        open_existing_file(f, e)
    if command == 'export':
        f = input('input filename:\n')
        export_to_other_format(f)


# check for number
def input_number_of_showing_records():
    while True:
        user_in = input('\ninput number of showing records: \n')
        if user_in.isdigit():
            return user_in
        else:
            print(f'{user_in} are not a number')


def input_info_for_record(filename: str, format_type: str):
    global flag
    flag = 'read'
    name = input('Name: \n')
    phone = input('Phone: \n')
    adress = input('Adress: \n')
    rec = ar(name, phone, adress)
    wrtf(rec, filename, format_type)
    open_existing_file(filename, format_type)


def choose_filename_and_format():
    pass


def open_existing_file(filename: str, format_type: str):
    global flag
    flag = 'read'
    global opened_file
    opened_file = [filename, format_type]
    rff(filename, format_type)


def create_new_file(filename: str, format_type: str):
    with open(f'{filename}.{format_type}', 'w') as file:
        file.write('txt file for Phonebook by CodeShavers\n')


def export_to_other_format(filename: str):
    f_csv(filename)


def rename_existing_file():
    pass


def file_manager():
    global flag
    flag = "show"
    print("Existed Phonebooks: \n")
    paths = (sorted(Path('.').glob('*.txt')))
    print("\n".join(list(map(str, paths))))


def help_menu(previous_flag: str):
    global flag
    flag = "help"
    menu_name = '** HELP **'
    help_commands = []
    desc_previous = f'you come here from ** {previous_flag} MENU ** list of possible commands are: '
    desc_return = 'type "return" to back in main menu'
    desc_help = 'help - way to come here'
    desc_export = 'export - export txt phonebook to other format'
    desc_csv = 'export to csv file'
    desc_xml = 'export to xml file'
    desc_open = 'open - open existing phonebook'
    desc_create = 'create - create new phonebook'
    desc_delete = 'delete - delete existing phonebook'
    desc_add = 'add - add record to current opened phonebook'
    desc_del = 'del - del record from current opened phonebook (not work in current version)'
    desc_find = 'find - find record in current opened phonebook (not work in current version)'
    desc_view = 'view - show records of current opened file'
    desc_show = 'show - show list of saved phonebooks'
    desc_quit = 'quit - quit from app'

    if previous_flag == 'options':
        pass
    elif previous_flag == 'show':
        help_commands = [desc_previous, desc_export, desc_open, desc_create, desc_delete, desc_help, desc_return]
    elif previous_flag == 'read':
        help_commands = [desc_previous, desc_add, desc_find, desc_del, desc_view, desc_help, desc_return]
    else:
        help_commands = [desc_previous, desc_show, desc_quit, desc_help, desc_return]

    print(menu_name)
    for com in help_commands:
        print(f'{com}\n')


if __name__ == '__main__':
    main()
