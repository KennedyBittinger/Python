#!/usr/bin/env python3

"""Module to manage contacts."""

__author__ = 'Kennedy Bittinger'
__date__ = '6/15/2020'

import pathlib
import csv
import pickle

TEXT_FILE = 1
CSV_FILE = 2
BINARY_FILE = 3


def read_file(file_name, file_type):
    """Read contacts file.

    Args:
        file_name (str): name of file
        file_type (int): TEXT_FILE, CSV_FILE, or BINARY_FILE

    Returns:
        contacts (list): list of contacts from file
    """
    contacts = []
    # Check if file exists before attempting to open to avoid exception
    if pathlib.Path(file_name).exists():
        if file_type == TEXT_FILE:
            with open(file_name, 'r') as in_file:
                for line in in_file:
                    line = line.replace('\n', '')
                    contacts.append(line)
        elif file_type == CSV_FILE:
            with open(file_name, 'r', newline='') as in_file:
                # reader will be a two-dimensional list
                contact_reader = csv.reader(in_file)
                for row in contact_reader:
                    contacts.append(row)
        else:
            with open(file_name, 'rb') as in_file:
                contacts = pickle.load(in_file)
    return contacts


def write_file(file_name, file_type, contacts):
    """Write contacts file.

    Args:
        file_name (str): name of file
        file_type (int): TEXT_FILE, CSV_FILE, or BINARY_FILE
        contacts (list): list of contacts to write

    Returns:
        None
    """
    # Clobber the contents of the file and replace with my list
    if file_type == TEXT_FILE:
        with open(file_name, 'w') as out_file:
            for contact in contacts:
                out_file.write(contact + '\n')
    elif file_type == CSV_FILE:
        with open(file_name, 'w', newline='') as out_file:
            contact_writer = csv.writer(out_file)
            # contacts must be a two-dimensional list
            contact_writer.writerows(contacts)
    else:
        with open(file_name, 'wb') as out_file:
            pickle.dump(contacts, out_file)


def make_contact(file_type):
    """Create a new contact based on user input.

    Args:
        file_type (int): TEXT_FILE, CSV_FILE, or BINARY_FILE

    Returns:
        contact (str or list): contains data entered by user
    """
    first_name = input('First? ')
    print()
    last_name = input('Last? ')
    print()
    phone = input('Phone? ')
    print()

    if file_type == TEXT_FILE:  # text file using list
        contact = first_name + ' ' \
                  + last_name + ' ' \
                  + phone
    else:  # csv and binary file using two-dim list
        contact = []
        contact.append(first_name)
        contact.append(last_name)
        contact.append(phone)
    return contact


def main():
    """Manage contacts.

    Args:
        None

    Returns:
        None
    """
    file_type = int(input('1=text, 2=csv, 3=binary? '))
    print()
    file_name = input('File? ')
    print()

    # get contacts from file
    contacts = read_file(file_name, file_type)

    # edit the contacts
    command = 'a'
    while command != 'q':
        # print current list of contacts
        counter = 1
        for contact in contacts:
            print(str(counter) + ' - ' + str(contact))
            counter += 1

        # modify list of contacts
        command = input('(a)dd, (d)elete, (q)uit? ')
        print()
        if command == 'a':
            contact = make_contact(file_type)
            contacts.append(contact)
        elif command == 'd':
            num_to_remove = int(input('Remove? '))
            print()
            # subtract 1 because user types 1, 2, 3, but index is 0, 1, 2
            contacts.pop(num_to_remove - 1)

    # save edited contacts to file
    write_file(file_name, file_type, contacts)


if __name__ == '__main__':
    main()
