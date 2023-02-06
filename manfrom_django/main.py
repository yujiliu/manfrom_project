import operator


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
            temp_dict[key] = ' None'
    return temp_dict


def sort_data_by(data, keyword, reverse):
    sorted_data = sorted(data, key=lambda x: x[keyword].lower(), reverse=reverse)
    print(f'Sorted by {keyword}:')
    print("\n".join(map(str, sorted_data)), "\n")


def main():
    with open("test.csv", encoding="utf-8") as main_file:
        name_string = main_file.readline()[:-1]
        print(name_string)

        main_list = [element for element in name_string.split(",")]
        print(main_list)

        data = []

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
    reverse = False  # Is sort reversed?

    sort_data_by(data, keyword, reverse)
    return main_list


if __name__ == "__main__":
    main()
