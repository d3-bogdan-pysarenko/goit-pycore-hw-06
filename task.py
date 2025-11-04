from collections import UserDict

class Field:
    def __init__(self,value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phoneNumber):
        phone_Num = Phone(phoneNumber)
        self.phones.append(phone_Num)
    
    def find_phone(self, phone):
        for phone_Obj in self.phones:
            if phone_Obj.value == phone:
                return phone_Obj

    def edit_phone(self, old_phone, new_phone):

        phone_Obj_to_edit = self.find_phone(old_phone)
        if phone_Obj_to_edit:
            phone_Obj_to_edit.value = new_phone
        else:
            print(f"Phone number '{old_phone}' not found for editing within '{self.name}' record")
            # raise ValueError(f"Phone number '{old_phone}' not found for editing within '{self.name}' record")
    
    def remove_phone(self, phone_Num):
        phone_Obj_to_remove = self.find_phone(phone_Num)
        if phone_Obj_to_remove:
            self.phones.remove(phone_Obj_to_remove)
        else:
            print(f"Phone number '{phone_Num}' not found in record for {self.name}.")
            # raise ValueError(f"Phone number '{phone_Num}' not found in record for {self.name}.")


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
        def add_record(self, record):
            if isinstance(record, Record):
                self.data[record.name.value] = record
            else:
                print("Only Record objects can be added to AddressBook")
                # raise TypeError("Only Record objects can be added to AddressBook.")
            
        def find(self,name):
            return self.data.get(name)
        
        def delete(self, name):
            if name in self.data:
                del self.data[name]
            else:
                print(f"Contact '{name}' not found in the address book")
                # raise KeyError(f"Contact '{name}' not found in the address book.")






# Checking time
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

jane= Record("Jane")
jane.add_phone("777777")
jane.add_phone("321558890")

book = AddressBook()
book.add_record(john_record)
book.add_record(jane)

for name, record in book.data.items():
    print(record)

john_for_edit = book.find("John")
print(john_for_edit)

print('------------------------------------------------------------------')
print('------------------------------------------------------------------')
print('------------------------------------------------------------------')

print(john_record.find_phone("5555555555"))
john_record.edit_phone("5555555555", "0000000000")
john_record.edit_phone("5555555555", "0000000000")
print(john_for_edit)
print(john_record)

print('------------------------------------------------------------------')
print('------------------------------------------------------------------')
print('------------------------------------------------------------------')

john_record.remove_phone("0000000000");
john_record.remove_phone("0000000000");
print(john_record)

print('------------------------------------------------------------------')
print('------------------------------------------------------------------')
print('------------------------------------------------------------------')

for name, record in book.data.items():
    print(record)

book.delete('Kevin')
book.delete('Jane')

for name, record in book.data.items():
    print(record)