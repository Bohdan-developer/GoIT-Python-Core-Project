from pathlib import Path
import os, time
from collections import Counter
from AddressBook import AddressBook

AB = AddressBook()

wrong = lambda: 'Wrong command!'

def add_contact():
    name = input('Enter Name:')
    phone = input('Enter Phone number:')
    if AB.validate_phone(phone):
        AB.add_contact(name, phone)
        return f'Contact {name} with phone number {phone} was created.'
    else:
        return f'Incorrect number. Try in format +380...'

def add_email():
    name = input('Enter Name:')
    if not AB.contacts.get(name):
        return f'Contact {name} does not exist!'
    email = input('Enter Email:')
    if AB.validate_email(email):
        AB.add_email(name, email)
        return f'{name}`s email {email} has been saved'
    else:
        return f'Incorrect email'

def add_address():
    name =  input('Enter Name:')
    if not AB.contacts.get(name):
        return f'Contact {name} does not exist!'
    address = input('Enter Address:')
    AB.add_address(name, address)
    return f'{name}`s address is {address}'

def add_birthday():
    name = input('Enter Name:')
    if not AB.contacts.get(name):
        return f'Contact {name} does not exist!'
    birthday = input('Enter Birthday in format 01.01.1990:')
    if AB.validate_birthday(birthday):
        AB.add_birthday(name, birthday)
        return f'{name}`s birthday {birthday} has been saved'
    else:
        return f'Incorrect date'

def change_contact():
    name = input('Enter Name:')
    if not AB.contacts.get(name):
        return f'Contact {name} does not exist!'
    address = input('Enter Address:')
    phone = input('Enter Phone number:')
    email = input('Enter Email:')
    birthday = input('Enter Birthday:')
    if AB.validate_birthday(birthday) and AB.validate_email(email) and AB.validate_phone(phone):
        AB.change_contact(name, address, phone, email,birthday)
        return f'{name}`s :\n Address: {address}, Phone: {phone}, Email: {email}, Birthday: {birthday}'
    else:
        return 'Incorrect data(email, phone number or birthday)'

def find_contact():
    return AB.search(input('Enter search info: '))

def nearby_birthday():
    n_days = input('Enter number of days: ')
    return AB.nearby_birthday(n_days)

def delete_contact():
    name = input('Enter Name of the contact: ')
    if not AB.contacts.get(name):
        return f'Contact {name} does not exist!'
    AB.delete_contact(name)
    return f'Contact {name} was deleted!'

def show_contacts():
    return AB.contacts

def create_new_note():
    tags = input('Enter tags for note(less then 6): ')
    note = input('Enter note text: ')
    data = f'{tags}\n\n{note}'
    t = str(time.time()).split('.')[0]
    filename = t+".txt" #Name would be similar to 1630063227.txt    
    try:
        with open(filename, "w") as file:
            file.write(data)            
    except IOError:
        print("File not accessible")
    return f'writing to, {filename}' #Display in console

def delete_note():
    filename = input("Enter FileName: ")
    path = os.getcwd()
    if os.path.isfile(filename):
        os.remove(os.path.join(path, filename))
        return f'{filename} deleted'
    else:
        return 'wrong FileName'

def note_search():
    note = input('note: ')
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    flist = []

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for filename in files:
        try:
            with open(os.path.join(__location__, filename), encoding='utf-8') as currentFile:
                text = currentFile.readlines()
                if (note.lower() in text[1].lower()): #Note we're looking for in the second line, lowercase
                    flist.append(filename[:-4])
        except:
            print(f"{filename} contains less than 2 strings or cannot be opened")

    result = Counter(flist)
    if not result:
        return 'No match!'
    else:
        res = 'Matches in Files:\n'
        for key, value in result.items():
            res += f'{value} : {key}\n'
        return res

def note_update():
    #file_to_open = 'data.txt' #filename input.
    file_to_open = input('Enter FileName: ')
    try:
        with open(file_to_open, 'r') as file:            
            data = file.readlines()
            
        
        print('Current note is:')
        print(data[1][:-1])
        note = input("Update a note: ") + '\n' #note input
        data[-1] = note
        with open(file_to_open, 'w') as file:
            file.writelines(data)
            

    except IOError:
        print("File not accessible")
    return f'Note updated to: {note}'

def Tag_Search_Helper(tag: str, flist: list, filename: str, text: str):
    if tag != '%%%%%%%%%%' and (tag.lower() in text[0].lower()): #Tag we're looking for in the first line, lowercase
        flist.append(filename[:-4])
    return flist

def tag_search():
    deftags = ['%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%']
    tags = input('Enter up to six tags ')
    tags = tags.split(' ')
    tags.extend(deftags)
    tags = tags[:6] 
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    flist=[]

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for filename in files:
        try:
            with open(os.path.join(__location__, filename), encoding='utf-8') as currentFile:
                text = currentFile.readlines()
                flist = Tag_Search_Helper(tags[0], flist, filename, text)
                flist = Tag_Search_Helper(tags[1], flist, filename, text)
                flist = Tag_Search_Helper(tags[2], flist, filename, text)
                flist = Tag_Search_Helper(tags[3], flist, filename, text)
                flist = Tag_Search_Helper(tags[4], flist, filename, text)
                flist = Tag_Search_Helper(tags[5], flist, filename, text)

        except:
            print(f"{filename} contains less than 2 strings or cannot be opened")

    result = Counter(flist)
    if not result:
        return 'No match!'
    else:
        res = 'Matches in Files:\n'
        for key, value in result.items():
            res += f'{value} : {key}\n'
        return res
    

def tag_update():
    #file_to_open = 'data.txt' #filename input.
    file_to_open = input('Enter FileName: ')
    try:
        with open(file_to_open, 'r') as file:
            data = file.readlines()           
        
        print('Current tags are:')
        print(data[0][:-1])
        tags = input("Write tags: ") + '\n' #tags input
        data[0] = tags
        

        with open(file_to_open, 'w') as file:
            file.writelines(data)

    except IOError:
        print("File not accessible")
    return f'Tags updated to: {tags}'

OPERATIONS = {
    'add contact' : add_contact,
    'add address' : add_address,
    'add email' : add_email,
    'add birthday' : add_birthday,
    'change contact' : change_contact,
    'find contact' : find_contact,
    'near birthday' : nearby_birthday,
    'delete contact' : delete_contact,
    'show contacts' : show_contacts,
    'create note' : create_new_note,
    'delete note' : delete_note,
    'change note' : note_update,
    'change tag' : tag_update,
    'search notes by tags' : tag_search,
    'search notes by text' : note_search
    }

def get_handler(operator):
    if not OPERATIONS.get(operator):
        return wrong
    return OPERATIONS[operator]


    
def main():
    #Start of the cli
    if os.path.exists('data.json'):
        AB.deserialize()
    print('Hello, User!')

    while True:
        command = input('Enter your command: ')
        if command == '.' or command == 'exit' or command == 'close':
            AB.serialize()
            print('Goodbye, User!')
            break
        handler = get_handler(command)
        answer = handler()
        print (answer)


if __name__ == '__main__':
    main()
