import pickle

phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321"},
             ]

def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])


def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1

def print_phonebook_by_numbers():
    idx = 0
    phone_book.sort(key=lambda entry: entry.get("phone_number"))
    for entry in phone_book:
        idx += 1
        print_entry(idx, entry)

def print_phonebook_by_age():
    phone_book.sort(key=lambda entry: entry.get("age"))
    idx = 0
    for entry in phone_book:
        idx += 1
        print_entry(idx, entry)

def add_entry_phonebook(surname, name, age):
    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    phone_book.append(entry)

def printError(message):
    print ("ERROR: %s" % message)

def printInfo(message):
    print ("INFO: %s" % message)

def find_entry_name_phonebook(name):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def find_entry_age_phonebook(age):
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def delete_entry_name_phonebook(name):
    idx = 0
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            del phone_book[idx-1]
            idx += 1
            found = True
    if not found:
        printError('Not Found!!!')

def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))

def print_avr_age():
    sum_age = 0
    avr_age = 0
    idx = 0
    for entry in phone_book:
        sum_age += entry["age"]
        avr_age = sum_age / len(phone_book)
        idx += 1
        print_entry(idx, entry)
    print("Средний возраст абонентов равняется: ", avr_age)

def increase_age(number_of_years):
    idx = 0
    for entry in phone_book:
        entry["age"] += number_of_years
        idx += 1
        print_entry(idx, entry)

def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


def main():
    while True:
        user_input = ""
        try:
            print ()
            print ()
            print ()
            print ("~ Welcome to phonebook ~")
            print ("Select one of actions below:")
            print ("     1 - Print phonebook entries")
            print ("     2 - Print phonebook entries (by age)")
            print ("     3 - Add new entry")
            print ("     4 - Find entry by name")
            print ("     5 - Find entry by age")
            print ("     6 - Delete entry by name")
            print ("     7 - The number of entries in the phonebook")
            print ("     8 - Avr. age of all persons")
            print ("     9 - Increase age by num. of years")
            print ("-----------------------------")
            print ("     s - Save to file")
            print ("     l - Load from file")
            print ("     0 - Exit")

            user_input = input("Enter you choice: ")
            choice = int(user_input)

            if choice == 1:
                print_phonebook()
            elif choice == 2:
                print_phonebook_by_age()
            elif choice == 3:
                surname = str(input("    Enter surname: "))
                name = str(input("    Enter name: "))
                age = int(input("    Enter age: "))
                add_entry_phonebook(surname, name, age)
            elif choice == 4:
                name = str(input("    Enter name: "))
                find_entry_name_phonebook(name)
            elif choice == 5:
                age = int(input("    Enter age: "))
                find_entry_age_phonebook(age)
            elif choice == 6:
                name = str(input("    Enter name: "))
                delete_entry_name_phonebook(name)
            elif choice == 7:
                count_all_entries_in_phonebook()
            elif choice == 8:
                print_avr_age()
            elif choice == 9:
                nmbrs_of_years = int(input("    Enter number of years to add to current ages: "))
                increase_age(nmbrs_of_years)
            elif choice == 0:
                print ("Bye!")
                break
            else:
                print ("Enter action within range [0..9]")

        except ValueError:
            if str(user_input) == 's':
                save_to_file()
            elif str(user_input) == 'l':
                load_from_file()
            else:
                printError("Something went wrong. Try again...")


if __name__ == '__main__':
    main()