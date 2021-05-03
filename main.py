# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f'is {name.__len__()} chars long')
    p=(4,5)
    x,y =p
    print(f'{x} and {y}')
    data =['declan',7]
    name, luckynum = data
    print(f'{name} and {luckynum}')
    s = 'Hello'
    print(f'{s} and 4th {s[3]}')
    print(f'{drop_first_last([5,7,8])}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')

def drop_first_last(grades):
 first, *middle, last = grades
 return avg(middle)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
