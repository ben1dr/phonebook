import json
import uuid
import re
import time
import getpass

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
    input_str = input("Welcome to search procedure. Please search by name or family or number: ")
    with open(filename, 'r') as f:
        fp = f.read()
        try:
            file = json.loads(fp)
            phonebook = file
        except:
            print("No contact exists in phonebook. Maybe deleted or not added yet.")
            return
        
        found_contact = []
        for key, value in phonebook.items():
            for item in value.values():
                founded = re.search(f"^{input_str}$", item)
                if founded != None:
                    found_contact.append(key)
        return found_contact
 
    
def show_contacts(id_list):
    print(f"Founded {len(id_list)} number{'s' if len(id_list)>1 else ''}.")
    if len(id_list) > 0:
        number_mapped = {}
        with open(filename, 'r') as f:
            fp = f.read()
            # try:
            file = json.loads(fp)
            phonebook = file
            # except:
            #     print("No contact exists in phonebook. Maybe deleted or not added yet.")
            #     return
            print(f" | first name{4*' '} | last name{5*' '} | phone number{2*' '}")
        
            for item in range(len(id_list)):
                id_number = id_list[item] 
                record = phonebook[id_number]
                print("{:<1}. {:<14} | {:<14} | {:<14}".format(item+1,record['first_name'], record['last_name'], record['phone_number']))
                number_mapped[item+1] = id_number
        return number_mapped    
        
    else:
        print('No contacts founded.')
        return False
            
        
def authorization():
    admin = {'username': 'admin',
             'password': 'admin'}
    print("'This section need access level approval.'")
    user = input('Please enter username: ')
    password = getpass.getpass("Please enter psasword: ")
    if user == admin['username']:
        if password == admin['password']:
            print('Your access level approved.')
            return True
    else:
        print('username or password incorrect. Access denied.')
        return False
    
    
def edit_contact(decide):
    check = authorization()
    if check:
        items = search_contact()
        contacts = show_contacts(items)
        if contacts != False:
            try:
                if decide == 'delete':
                    message = 'Please type contact row number that you want to delete it: '
                elif decide == 'edit':
                    message = 'Please type contact row number that you want to edit it: '
                contact_chosen = int(input(message))
                if 0 < contact_chosen <= len(contacts):
                    with open(filename, 'r') as f:
                        fp = f.read()
                        file = json.loads(fp)
                        phonebook = file
                    
                    
                    if decide == 'delete':
                        del phonebook[contacts[contact_chosen]]   
                        print('Contact deleted successfully') 
                    elif decide == 'edit':
                        intended_contact = phonebook[contacts[contact_chosen]]
                        print("If you don't want edit any field press enter key.")
                        for key in intended_contact:
                            input_value = input(f"Enter new value for {key}: ")
                            if input_value:
                                intended_contact[key] = input_value 
                        phonebook[contacts[contact_chosen]] = intended_contact
                        print('Contact edited successfully.')

                    pretty_file = json.dumps(phonebook, indent=4)
                    with open(filename, 'w') as fp:
                        fp.write(pretty_file)
                else:
                    print("Your input is wrong.")
            except:
                print('Your input is so wrong.')   
            

           
    

    
def menu(close):        
    while True:
        print("""Type your desired option number from menu, then press Enter key.
    1. Add contact to phonebook
    2. Search for contact(s)
    3. Edit contact
    4. Delete contact
    5. Quit from app""")
        try:
            command = int(input('Your choice: '))
            if command == 1:
                add_contact()
            elif command == 2:
                output = search_contact()
                show_contacts(output)
            elif command == 3:
                edit_contact(decide='edit')
            elif command == 4:
                edit_contact(decide='delete')
            elif command == 5:
                close = True
        except:
            print('You must type a number between 1 and 5. Please try again.')
            time.sleep(.5)
        finally:    
            if close == True:
                quit("""
                Thank you for using my program.
                Yours sincerely, 
                        --> Benyamin Derakhshani <--
                S e e   Y o u   L a t e r
                     """)
            input('-->Press Enter to continue...')
            print()


if __name__ == '__main__' :
    print('-*-*-*-"Welcome to terminal phonebook app."-*-*-*-')
    close = False     
    menu(close)

        
        
