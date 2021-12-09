import json
import uuid
import re
# file_name = 'phonebook.txt'
filename = 'phonebook.json'

def add_contact():
    with open(filename, 'r') as f:
        fp = f.read()
        try:
            file = json.loads(fp)
            phonebook = file
        except:
            phonebook = {}

    user_id = str(uuid.uuid1())
    contact = {}
    print("Welcome to add contact procedure. Please enter information.")
    contact['first_name'] = input("Please enter contact's first name: ")
    contact['last_name'] = input("Please enter contact's family: ")
    contact['phone_number'] = input("Please enter contact's phone number: ")
    phonebook[user_id] = contact
    pretty_file = json.dumps(phonebook, indent=4)
    with open(filename, 'w') as fp:
        fp.write(pretty_file)    
    print('Contact added.')

def search_contact():
    input_str = input("Welcome to search procedure. Please search by name or family or number:\n")
    with open(filename, 'r') as f:
        fp = f.read()
        try:
            file = json.loads(fp)
            phonebook = file
        except:
            print("No contact exists in phonebook. Maybe deleted or not added yet.")
            return
        
        max_width = 12
        found_contact = []
        for k_v in phonebook.values():
            for value in k_v.values():
                founded = re.search(f"^{input_str}$", value)
                if founded != None:
                    found_contact.append(k_v)
                    max_width = max(len(value), max_width)

        print(f"Founded {len(found_contact)} number{'s' if len(found_contact)>1 else ''}:")
        # if max_width > 11:
        #     width_space = " "*(max_width - 11)
        # else:
        #     width_space = " "
        # width_space = 14
        if len(found_contact) > 0:
            print(f"first name{4*' '} | last name{5*' '} | phone number{2*' '}")
            
            for record in found_contact:
                print("{:<14} | {:<14} | {:<14}".format(record['first_name'], record['last_name'], record['phone_number']))
                    # print(f"{record['first_name']}{lack_of_space} | " + 
                    #     f"{record['last_name']}{lack_of_space} | "+
                    #     f"{record['phone_number']}{lack_of_space}")
                    # for cell in record.values():
                    #     print(f"{0}{width_space} | {1}{width_space} | {2}{width_space}")
                # print("".join(found))
                
        # print(file)
        # found = []
        # for i in file:
        #     founded = re.search(f'r"\b{input_str}\b"', i)
        #     if founded != None:
        #         found.append(i)
        # if len(found) == 0:     
        #     print("No items founded.")
        # else:
        #     print(f"Founded {len(found)} number{'s' if len(found)>1 else ''}:")
        #     print("".join(found))

def delete_contact():
    admin = {'username': 'admin',
             'password': 'admin'}
    "You choose delete contact option. Need approve your access level."
    user = input('Please enter username: ')
    password = input("Please enter psasword: ")
    if user == admin['username']:
        if password == admin['password']:
            print('Your access level approved.')
    else:
        print('username or password incorrect. Access denied.')
        return
    search_contact()
    
    
        
print('-*-*-*-"Welcome to terminal phonebook app."-*-*-*-')
while True:
    command = input('To add phone contact press "a", to delete press "d", ' + 
                    'to search press "s", and to quit press "q" then press key "Enter".\n')

    if command == 'q':
        break
    elif command == "a":
        add_contact()
    elif command == 'd':
        delete_contact()
    elif command == 's':
        search_contact()
    else:
        print('Your input command is wrong, press the correct key.')
    print()

    
        
        
