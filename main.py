# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

def multi() :
    a = int(input("Einmal Eins:"))
    x = int(input("Wiederholungen: "))
    print("_________________________")
    for i in range(1, x + 1):
        x = a * (i)
        print('   ', i, '    ', x)

def lotto():
    import random
    print ('hier kommen die Lottozahlen')
    lottozahlen_alle = []
    lottozahlen_alle.extend(range(1, 50))
    lottozahlen_gewinner = random.sample(lottozahlen_alle, 6)
    lottozahlen_gewinner.sort()
    print(lottozahlen_gewinner)
    print(random.choices(lottozahlen_alle, k=6))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    multi()
    lotto()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
