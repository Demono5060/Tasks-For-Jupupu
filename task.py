import os
import math
import time
import datetime


def unreal_join(arr, simble):
    string = ''
    for i in arr:
        string+=i+simble
    return string[0:-1]


def hour_angle():
    time = datetime.timedelta(hours=int(input("Hours: ")))
    return (360/12)*(int(str(time)[0:2])-12+int(str(time)[0:2])%12)


def school_desks(arr):
    return int(arr[0]/2)+arr[0]%2+int(arr[1]/2)+arr[1]%2+(arr[2]/2)+arr[2]%2


def how_much_time():
    time = datetime.timedelta(minutes=int(input("How many minutes past? :")))
    return str(time)[-8:]


def shift(values):
    values_buf = values.copy()
    for i in range(len(values)):
        if(i!=0):
            values[i] = values_buf[i-1]
        else:
            values[i] = values_buf[len(values)-1]
            values[len(values)-1] = values_buf[0]
    return values


def change_min_to_max(values):
    mx = values.index(max(values))
    mn = values.index(min(values))
    buf = values[mx]
    values[mx] = values[mn]
    values[mn] = buf
    return values


def func_4(values):
    if (values[-1] == 0):
        count = 0
        max_size = 0
        for i in range(len(values)):
            if(values[i] == values[i-1] and i != 0):
                count += 1
                if(count > max_size):
                    max_size = count
        return count


def frame():
    size = int(input("Enter the size for frame: \n"))
    os.system("cls||clear")
    char = input("Enter the char for frame: \n")
    os.system("cls||clear")
    print(char*size)
    [print(char+' '*(size-2)+char) for i in range(size)]
    print(char*size)


def counter():
    value = input("Enter the value to count nums: \n")
    os.system("cls||clear")
    num = input("Enter the num to count\n")
    os.system("cls||clear")
    count = 0
    for v in value:
        if(v == num):
            count += 1
    print("Counter = {}".format(count))


def stair():
    num = input("Choose orientation to the stair: \n 0) Left \n 1) Right \n")
    os.system("cls||clear")
    char = input("Choose the char: \n ")
    os.system("cls||clear")
    size = int(input("Choose the size of stair: \n"))
    os.system("cls||clear")
    if(num == '0'):
        [print(char * i) for i in range(size)]
    if(num == '1'):
        [print(' ' * (size-i)+char * i) for i in range(size)]


def main():
    num = input(
        'Choose the task: \n 0) Stair \n 1)Counter for num \n 2)Framen\n 3) Func 4\n '+
        '4) Change min to max and conversly \n 5) Shift\n 6) How much time\n 7) school_desks\n'+
        '8) hour angle \n 9) join\n')
    if(num == '0'):
        os.system("cls||clear")
        stair()
    elif(num == '1'):
        os.system("cls||clear")
        counter()
    elif(num == '2'):
        os.system("cls||clear")
        frame()
    elif(num == '3'):
        os.system("cls||clear")
        print(func_4([0, 0, 2, 3, 1, 4, 2, 4, 3,
              3, 3, 3, 4, 544, 5, 2, 3, 4, 0]))
    elif(num == '4'):
        os.system("cls||clear")
        print(change_min_to_max(
            [0, 2, 2, 2, 43, 215, 54, 324, 13, 342, 123, 52]))
    elif(num == '5'):
        os.system("cls||clear")
        print(shift([0, 2, 2, 2, 43, 215, 54, 324, 13, 342, 123, 52]))
    elif(num == '6'):
        os.system("cls||clear")
        print(how_much_time())
    elif(num=='7'):
        os.system("cls||clear")
        print(school_desks([10,13,16]))
    elif(num=="8"):
        os.system("cls||clear")
        print(hour_angle())
    elif(num=="9"):
        os.system("cls||clear")
        print(unreal_join(['HELLO',"BITCH"],'*'))


if __name__ == "__main__":
    main()
