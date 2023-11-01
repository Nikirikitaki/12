from collections import UserDict
from datetime import datetime
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Birthday(Field):
    def __init__(self, value):
        self._value = None  
        self.value = value
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        try:
            datetime.strptime(new_value, '%Y-%m-%d')
            self._value = new_value
        except ValueError:
             print("wrong type of data, try like this '1990-10-26'")

class Phone(Field):
    def __init__(self, value):
        self._value = None  
        self.value = value
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if len(new_value) == 10 and new_value.isdigit():
            self._value = new_value
        else:
            raise ValueError("Invalid phone number,try like this  '0956150338'")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthdays = []
    
    def add_birthday(self,birthday):
        birthday_obj = Birthday(birthday)  
        self.birthdays.append(birthday_obj)  
        return birthday_obj
            
    def add_phone(self,phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self,phone):
        phone_str = str(phone)
        if phone_str in [str(p) for p in self.phones]:
            self.phones = [p for p in self.phones if str(p) != phone_str]
        else:
            print(f"No record {phone} ")
            
    def edit_phone(self,phone,new_phone):
        found_res = self.find_phone(phone)
        if found_res:
            self.remove_phone(phone)
            self.add_phone(new_phone)
        else:
            raise ValueError 
        
    def find_birthday(self,birthday):
         for p in self.birthdays:
            if p.value == birthday:
                return p
            else:
               print('No record') 
                           
    def find_phone(self,phone:str):
        for p in self.phones:
            if p.value == phone:
            
                return p
    
    def days_to_birthday(self):
        if self.birthdays:
            birthday_date = datetime.strptime(self.birthdays[0].value, '%Y-%m-%d')
        else:
            return "No data"
        
        today = datetime.now()
        current_year = today.year
        next_birthday = birthday_date.replace(year=current_year)
    
        if today > next_birthday:
            next_birthday = next_birthday.replace(year=current_year + 1)
        
        days_until_birthday = (next_birthday - today).days
        print(f'Birthday in {days_until_birthday} days!!!))')
        return days_until_birthday

    def __str__(self):
        phone_numbers = ', '.join(str(phone) for phone in self.phones)
        birthday = ', '.join(str(birstday) for birstday in self.birthdays)
        return f'{self.name} - {phone_numbers}: {birthday}'
            
        
class AddressBook(UserDict):
    def __init__(self,page_size = 8):
        super().__init__()
        self.data = {}
        self.page_size = page_size
        self.current_page = 0 
        
    def add_record(self, record):
        self.__setitem__(record.name.value, record)
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"No record {name} ")
    
   
        
    def __iter__(self):
        return self

    def __next__(self):
        items = list(self.data.items())
        start = self.current_page * self.page_size
        end = (self.current_page + 1) * self.page_size
        if start < len(self.data):
            page_items = items[start:end]
            page = dict(page_items)
            self.current_page += 1
            return page
        else:
            raise StopIteration

    
        
        
if __name__ == '__main__':
    book = AddressBook()
    
    jane_record = Record("Jane")
    jane_record.add_phone("1234567890")
    jane_record.add_phone("1231231233")
    jane_record.add_phone("3332223331")
    book.add_record(jane_record) #1
    John_record = Record("John")
    John_record.add_phone("1234567890")
    John_record.add_phone("5555555555")
    John_record.add_birthday('1995-05-04')
    book.add_record(John_record) #2
    Vill_record = Record("Vill")
    Vill_record.add_phone("1234567890")
    book.add_record(Vill_record)#3
    Stiv_record = Record("Stiv")
    Stiv_record.add_phone("1234567890")
    book.add_record(Stiv_record)#4
    
    
   
    
    phone = John_record.find_phone("1234567890")
    days = John_record.days_to_birthday()
   
    print(f'Adres book size : {len(book)}')
    
    
    
     
    for page in book:
        print('----------')
        print(type(page))
        for contact in page:
            print(page.get(contact))
            
    
   