def years():
    year = int(input('Enter a year: '))
    a = year % 4
    b = year % 100
    c = year % 400
    if a == 0 and b == 0 and c == 0:
        print('Leap year.')
    else:
        print("Not leap year.")
years()