import os
import random

# Clears the terminal screen
def cls():
    os.system('cls')

def main_menu():
    print('\n---------- CLASSIC ALGORITHMS ----------\n')
    print('-------------- Main Menu ---------------')
    print('1) Collatz Conjecture')
    print('2) Merge Sort')
    print('3) Bubble Sort')
    print('4) Closest Pair')
    print('5) Sieve of Eratosthenes')
    print('6) EXIT')
    print('----------------------------------------')
    user_input = input('Make a selection:\n>')

    if user_input == '1':
        cls()
        collatz_conjecture()

    elif user_input == '2':
        cls()
        merge_sort_list()

    elif user_input == '3':
        cls()
        bubble_sort()

    elif user_input == '4':
        cls()
        closest_pair()

    elif user_input == '5':
        cls()

    elif user_input == '6':
        exit()

    else:
        cls()
        main_menu()


def retry_option(function):
    print('----------------------------------------')
    print('1) Retry?')
    print('2) Main Menu')
    print('3) Exit')
    print('----------------------------------------')
    user_input = input('Make a selection:\n>')

    while user_input not in ['1', '2', '3']:
        continue

    else:
        if user_input == '1':
            cls()
            function()

        elif user_input == '2':
            cls()
            main_menu()

        elif user_input == '3':
            exit()


def collatz_conjecture():
    try:
        print('\n---------- CLASSIC ALGORITHMS ----------\n')
        print('---------- Collatz Conjecture ----------')

        collatz_list = []

        collatz_num = int(input('\nEnter an integer:\n>'))

        if collatz_num > 0:

            while collatz_num != 1:

                if collatz_num % 2 == 0:
                    collatz_num = (collatz_num/2)
                    collatz_list.append(str(int(collatz_num)))

                elif collatz_num % 2 != 0:
                    collatz_num = ((collatz_num * 3) + 1)
                    collatz_list.append(str(int(collatz_num)))

            print(f'\nSequence completed in {len(collatz_list)} steps.')
            print(', '.join(collatz_list) + '\n')

        else:
            print('INVALID INPUT')

    except ValueError:
        print('INVALID INPUT')

    retry_option(collatz_conjecture)


def merge_sort_list():
    try:
        print('\n---------- CLASSIC ALGORITHMS ----------\n')
        print('-------------- Merge Sort --------------')

        # Create array of user defined length
        array_length = int(input('\nEnter the length of the array:\n>'))
        random_array = [random.choice(range(1, 100)) for num in range(0, array_length)]

        if array_length > 0:

            # Show user the array then begin to sort it
            print(f'\nUnsorted array = {random_array}\n')
            print('----------------------------------------\n')
            merge_sort(random_array)

            # Display this once sorting has been completed, and ask for user input
            print('\nArray sorting complete!\n')

        else:
            print('INVALID INPUT')

    except ValueError:
        print('INVALID INPUT')

    retry_option(merge_sort_list)


def merge_sort(array):

    if len(array) > 1:

        # Recursively dividing array
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        print(f'Left array = {left_array}')
        print(f'Right array = {right_array}\n')

        merge_sort(left_array)
        merge_sort(right_array)

        # Merging
        left_array_index = 0
        right_array_index = 0
        merge_array_index = 0

        while left_array_index < len(left_array) and right_array_index < len(right_array):
            if left_array[left_array_index] < right_array[right_array_index]:
                array[merge_array_index] = left_array[left_array_index]
                left_array_index += 1

            else:
                array[merge_array_index] = right_array[right_array_index]
                right_array_index += 1

            merge_array_index += 1

        while left_array_index < len(left_array):
            array[merge_array_index] = left_array[left_array_index]
            left_array_index += 1
            merge_array_index += 1

        while right_array_index < len(right_array):
            array[merge_array_index] = right_array[right_array_index]
            right_array_index += 1
            merge_array_index += 1

    if len(array) > 1:
        print('Sorting array:')
        print(f'{array}\n')


def bubble_sort():
    try:

        print('\n---------- CLASSIC ALGORITHMS ----------\n')
        print('------------- Bubble Sort --------------')

        # Create array of user defined length
        array_length = int(input('\nEnter the length of the array:\n>'))
        random_array = [random.choice(range(1, 100)) for num in range(0, array_length)]

        if array_length > 0:

            # Show user the array then begin to sort it
            print(f'\nUnsorted array = {random_array}\n')
            print('----------------------------------------\n')

            index_length = len(random_array) - 1
            is_sorted = False

            while not is_sorted:
                is_sorted = True
                for i in range(0, index_length):
                    if random_array[i] > random_array[i + 1]:
                        random_array[i], random_array[i + 1] = random_array[i + 1], random_array[i]
                        i += 1
                        is_sorted = False
                        print('Sorting array:')
                        print(f'{random_array}\n')

            # Display this once sorting has been completed, and ask for user input
            print('\nArray sorting complete!\n')

        else:
            print('INVALID INPUT')

    except ValueError:
        print('INVALID INPUT')

    retry_option(bubble_sort)


# The closest pair of points problem or closest pair problem is a problem of computational geometry: given n points in metric space, find a pair of points
# with the smallest distance between them.
def closest_pair():
    try:
        print('\n---------- CLASSIC ALGORITHMS ----------\n')
        print('------------ Closest Pair --------------')

        # Create array of user defined length
        array_length = int(input('\nEnter the amount of points on the x, y axis:\n>'))
        random_array = [(random.choice(range(1, 100)), random.choice(range(1, 100))) for num in range(0, array_length)]

        if array_length > 0:

            # Show user the array then begin to sort it
            print(f'\nPoints (x, y): {random_array}')
            print('----------------------------------------\n')

        else:
            print('INVALID INPUT')

    except ValueError:
        print('INVALID INPUT')

    retry_option(closest_pair)


main_menu()
