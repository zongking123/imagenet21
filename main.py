# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    with open('class_names.txt', 'r', encoding='utf-8') as f, open('res_class_names.txt', 'w',encoding='utf-8') as fw:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if ',' in line:
                line = line.split(',')[0]
            if '_' in line:
                lineList = line.split('_')
                line = ''
                for value in lineList:
                    line = line + " " + value
            fw.write(line + '\n')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
