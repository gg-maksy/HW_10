from collections import UserDict


class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Record(Field):

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def change_phone(self, new_phone):
        old_phone = self.phone
        self.phone = new_phone
        return f'Change {old_phone} to {new_phone}'
    
    

class Phone(Field):
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a interger')
        self.value = value


class Name(Field):
    pass



class AdressBook(UserDict):
    def add_contact(self, contact:Record):
        self.data[contact.name.value] = contact


if __name__ == '__main__':

    adress_book = AdressBook()
    cont = Record(Name('Boris'), Phone(+380665411384))

    cont.change_phone(+231331)
    
    adress_book.add_contact(cont)

    for key, value in adress_book.items():
        print(key, value.phone)



