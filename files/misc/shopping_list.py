def get_list():
    item_number = 1
    item_list = {}
    while True:
        item = input('Enter item: ')
        if len(item) != 0:
            item_list[item_number] = item
            print(len(item_list))
            item_number += 1
          #  item_list[str(item_number)].append(str(item))
          #  break
        #else:
        else: return item_list


def print_list():
    item_number = 1
    the_list = get_list()
    file = open('shopping.csv', 'w')
    file.write('Item #,Name\n')
    for i in range(len(the_list)):
        file.write(str(item_number) + ',' + the_list[i+1] + '\n')
        print(the_list[i+1])
        item_number += 1
    file.close()

print_list()