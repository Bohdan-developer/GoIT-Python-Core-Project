import json
from collections import UserDict

class AddressBook(UserDict):
    
    '''Все контакты будут иметь вид:
    'имя контакта1' : { 'address' : 'адрес контакта', 'phone' : 'номер(пока что один и типа str)',
    'email' : 'електронная почта', 'birthday' : 'день рождения'},
    'имя контакта2' :{следующие данные},'''
    
    contacts = {}

    def __repr__(self):
        pass

    def serialize(self):
        with open('data.json', 'a') as file:
            json.dump(self.contacts, file)

    def deserialize(self):
        with open('data.json', 'r') as file:
            self.contacts = json.load(file)

    #Добавление контакта. Не добавив контакт через эту функ добавить другую информацию не вийдет
    def add_contact(self, name, phone_number):
        self.contacts[name] = {
            'Address' : None,
            'Phone' : phone_number,
            'Email' : None,
            'Birthday' : None
            }

    #Добавление адреса контакта
    #Добавить валидацию ввода   <-- Task!
    def add_address(self, name, address):
        self.contacts[name]['Address'] = address

    #Добавление електронной почты
    #Добавить валидацию ввода     <--Task
    def add_email(self, name, email):
        self.contacts[name]['Email'] = email

    #Добавление дня рождения. Только стринг. При будущих манипуляциях с датой переводим стринг в тип date
    #Нужно будет добавить валидацию ввода для дня рождения   <--Task
    def add_birthday(self, name, birthday):
        self.contacts[name]['Birthday'] = birthday

    #Выводит список контактов у которых день рождения через n_days от текущей даты
    def nearby_birthday(self, n_days):
        pass

    #Редакция контакта. можно разделить на отдельные функции
    def change_contact(self, name, address, phone, email, birthday):
        self.contacts[name] = {
            'Address' : address,
            'Phone' : phone,
            'Email' : email,
            'Birthday' : birthday
            }

    #Поиск по контактам. пока не знаю. будем только по имени или по всем параметрам????
    def search(self, string):
        for key, value in self.contacts.items():
            if key == string:
                return self.contacts[key]
            else:
                for val in value.values():
                    if val == string:
                        return self.contacts[key]
                    else:
                        continue

    #Удаление контакта
    def delete_contact(self, name):
        self.contacts.pop(name)
    
ab = AddressBook()
ab.add_contact('borys', '83749824')
ab.add_email('borys', 'ksjdflks@mail.com')
ab.add_contact('serg', '8374982445')
ab.add_email('serg', 'ksjdflksssr@mail.com')
ab.add_contact('art', '8374982423')
ab.add_email('art', 'kmnmsjdflks@mail.com')
ab.add_contact('nok', '8374982489')
ab.add_email('nok', 'ksjeckdflks@mail.com')


