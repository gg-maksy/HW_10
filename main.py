from operation import AdressBook, Record, Name, Phone

adress_book = AdressBook()

contacts = {'Ilia': ['+22332'],
            'Boris': ['+2121414', '+23124411'],
            'Vlad': ['+4345333']}

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

        adress_book.add_contact(new_contact)
        
        # if name in AdressBook():
        #     contacts[name].extend(numb_of_phone)
        #     return f'Contact {name} was update'
        
        # elif not name in contacts:
        #     contacts.update({name: numb_of_phone})
        #     return f'Contact {name} was added'
    else:
        raise IndexError


def exit(*args):
    return 'Bye'

def no_command(*args):
    return 'Unknown command. Try again'

def show_all(*args):
    return '\n'.join([f'{k}: {v.phone}' for k, v in adress_book.items()])

@input_error
def get_number(*args):
    lst = list_of_params(*args)
    
    for k, v in adress_book.items():
        if lst[0] == k:
            return f'{lst[0]}: {v.phone}'
        
    return f'Not contacts {lst[0]}'

@input_error
def change_contact(*args):
    lst = list_of_params(*args)
    if len(lst) == 2:
        for k, v in adress_book.items():
            if k == lst[0]:
                contact = Record(Name[k], Phone(int(lst[1])))
                adress_book.update({contact.name.value: contact})
        return f'Contact {lst[0]} was change'
    else:
        raise IndexError

def remove_contact(*args):
    contacts.pop(args[0])
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
        # if command == exit:
        #     break

if __name__ == '__main__':
    main()
    print(adress_book)