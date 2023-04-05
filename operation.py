from collections import UserDict


class Field:
    def __init__(self, value):

        if not isinstance(value, str):
            raise ValueError('Value must be a string')
        self.value = value

    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return str(self)


class Record(Field):

    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone] if phone else []
    
    def add_phone(self, phone):
        self.phones.append(phone)
    
    def add_phones(self, phones):
        self.phones += phones

    def change_phone(self, old_phone, new_phone):

        for i, p in enumerate(self.phones):
            if p.value == old_phone.value:
                self.phones[i] = new_phone

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

    cont.change_phone(Phone(+380665411384), Phone(+231331))
    
    adress_book.add_contact(cont)

    for key, value in adress_book.items():
        print(key, value.phones)

    cont.add_phone(Phone(62743883))
    
    for key, value in adress_book.items():
        print(key, value.phones)
    
    
    cont.add_phones([Phone(352266), Phone(30689340986)])
    
    for key, value in adress_book.items():
        print(key, value.phones)

