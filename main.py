from operation import AdressBook, Record, Name, Phone


adress_book = AdressBook()


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Type help.'
    return inner


@input_error
def list_of_params(*args):
    conteiner = args[0].split()

    if not conteiner:
        raise IndexError
    
    return conteiner


def help(*args):
    return """
Show all contacts -- enter /show all
Add a new contact -- enter /add
Get contact -------- enter /phone [Name]
Change number ------ enter /change contact [Name] [current number] [new number]
Remove contact ----- enter /remove [Name]
For exit ----------- enter .
"""


def hello(*args):
    return 'How can I help you? For more information - enter /help'


@input_error
def add(*args):
    lst = list_of_params(*args)
    if len(lst) == 2:
            
        name = Name(lst[0])
        numb_of_phone = Phone(int(lst[1]))
        new_contact = Record(name, numb_of_phone)

        if lst[0] in [k for k in adress_book.keys()]:
            
            val = adress_book.get(lst[0])
            if lst[1] in [str(i) for i in val.phones]:
                    return f'This number is alredy yet in contact {name}'
            
            val.add_phone(Phone(int(lst[1])))
            return f'Contact {name} was update'

        if not lst[0] in [k for k in adress_book.keys()]:
            adress_book.add_contact(new_contact)
            return f'Contact {name} was added'
        
    else:
        raise IndexError


def exit(*args):
    return 'Bye'


def no_command(*args):
    return 'Unknown command. Try again'


def show_all(*args):
    return '\n'.join([f'{k}: {v.phones}' for k, v in adress_book.items()])


@input_error
def get_number(*args):
    lst = list_of_params(*args)
    
    for k, v in adress_book.items():
        if lst[0] == k:
            return f'{lst[0]}: {v.phones}'
        
    return f'Not contacts {lst[0]}'


@input_error
def change_contact(*args):
    lst = list_of_params(*args)

    if len(lst) == 3:
        if lst[0] in [k for k in adress_book.keys()]:
            adress_book.get(lst[0]).change_phone(Phone(int(lst[1])), Phone(int(lst[2])))
        return f'Contact {lst[0]} was change'
    
    else:
        raise IndexError


def remove_contact(*args):
    adress_book.pop(args[0])
    return f'Contact {args[0]} was deleted'


COMMANDS = {help: '/help',
            add: '/add',
            exit: '.',
            show_all: '/show all',
            get_number: '/phone',
            change_contact: '/change contact',
            remove_contact: '/remove',
            hello: 'hello'}


def command_handler(text: str):

    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
        
    return no_command, None


def main():

    while True:

        user_input = input('>>> ')
        if user_input in ('.', 'good bye', 'close', 'exit'):
            print(exit())
            break

        command, data = command_handler(user_input)
        print(command(data))



if __name__ == '__main__':
    main()

