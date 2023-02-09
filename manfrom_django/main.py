import operator
import re
from os import path


wrong_symbols = ['\'', '\"', "\n"]
lines = []


def clear_string(string):
    new_string = ''
    for symbol in string:
        if not symbol in wrong_symbols:
            new_string += symbol
    return new_string


def create_dict(main_list, current_list):
    i = 0
    temp_dict = dict.fromkeys(main_list)
    for key in temp_dict.keys():
        try:
            temp_dict[key] = current_list[i]
            i += 1
        except IndexError:
            temp_dict[key] = ' None'  # One of the lines was not created with all the fields
            # filled it with a stub value for normal use
    return temp_dict


def sort_data_by(data, keyword, reverse):
    try:
        sorted_data = sorted(data, key=lambda x: x[keyword].lower(), reverse=reverse)
        print(f'Sorted by {keyword}:')
        print("\n".join(map(str, sorted_data)), "\n")
    except KeyError:
        print('Wrong keyword!')


def re_find(data, keyword):
    result = []
    for person in data:
        for value in person.values():
            if bool(re.search(keyword, value, re.IGNORECASE)):
                result.append(person)
                break
    print(f'Search by {keyword}:')
    if len(result) == 0:
        print('No matches')
    else:
        print("\n".join(map(str, result)), "\n")


def main():
    basepath = path.dirname(__file__)
    with open("manfrom_django/test.csv", encoding="utf-8") as main_file:
        name_string = main_file.readline()[:-1]
        print(name_string)

        main_list = [element for element in name_string.split(",")]  # our fields
        print(main_list, '\n')

        data = []  # List with customers dicts

        for line in main_file:

            correct_string = clear_string(line)

            number = correct_string.split(",")[0]
            print(f'{number} -- >', correct_string)
            temp_list = []
            for element in correct_string[:-1].split(","):
                temp_list.append(element)
            print(temp_list)

            temp_dict = create_dict(main_list, temp_list)
            print(temp_dict, "\n")
            data.append(temp_dict)

    print("\n".join(map(str, data)), "\n")

    keyword = 'customers_lastname'  # Change sort keyword here
    reverse = False  # Reverse sorting?

    sort_data_by(data, keyword, reverse)

    keyword = '(^зубко$)'
    re_find(data, keyword)

    keyword = '(\W|^)[\w.\-]{0,25}@(yahoo|hotmail|mail)(\W|$)'  # regex for email
    re_find(data, keyword)

    #keyword = '^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'  # Trying to make regex for cutomers_telephone
    #re_find(data, keyword)

    #return main_list  # List with fields using in django | Comment this line if u using this script in single-mode.


if __name__ == "__main__":
    main()
