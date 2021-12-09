# Imports
import os
import random
import math

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
        Sieve_of_Eratosthenes()

    elif user_input == '6':
        exit()

    # Prevents incorrect input and reloads menu
    else:
        cls()
        main_menu()


# Runs after each algorithm is completed
def retry_option(function):
    print('----------------------------------------')
    print('1) Retry?')
    print('2) Main Menu')
    print('3) Exit')
    print('----------------------------------------')
    user_input = ''

    # Prevents incorrect input by keeping user in while loop until correct input
    while user_input not in ['1', '2', '3']:
        user_input = input('Make a selection:\n>')

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
        # Gets integer input to 1
        # If even, divide by 2
        # If odd, multiply by 3 and add 1

        collatz_list = []

        collatz_num = int(input('\nEnter an integer:\n>'))

        if collatz_num > 0:

            # Exit this while loop once the program successfully gets to 1
            while collatz_num != 1:

                # Divides even numbers by 2 (adds results to a list)
                if collatz_num % 2 == 0:
                    collatz_num = (collatz_num/2)
                    collatz_list.append(str(int(collatz_num)))

                # Multiply odd by 3 and add 1 (adds results to a list)
                elif collatz_num % 2 != 0:
                    collatz_num = ((collatz_num * 3) + 1)
                    collatz_list.append(str(int(collatz_num)))

            # Show results and number of steps taken to reach 1
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
        random_array = [random.choice(range(1, 100)) for _num in range(0, array_length)]

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

        # Prints each split to show user algorithm
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
        random_array = [random.choice(range(1, 100)) for _num in range(0, array_length)]

        if array_length > 0:

            print(f'\nUnsorted array = {random_array}\n')
            print('----------------------------------------\n')

            index_length = len(random_array) - 1
            is_sorted = False

            while not is_sorted:
                # Can only exit this loop if no swaps are completed in the loop
                is_sorted = True
                for i in range(0, index_length):
                    # Swaps numbers if the left number is bigger than the right
                    if random_array[i] > random_array[i + 1]:
                        random_array[i], random_array[i + 1] = random_array[i + 1], random_array[i]
                        i += 1
                        is_sorted = False
                        print('Sorting array:')
                        print(f'{random_array}\n')

            print('\nArray sorting complete!\n')

        else:
            print('INVALID INPUT')

    except ValueError:
        print('INVALID INPUT')

    retry_option(bubble_sort)


def closest_pair():
    # This is not the most optimised solution for this problem, this is instead a bruteforce method which is more beginner friendly to understand
    try:
        print('\n---------- CLASSIC ALGORITHMS ----------\n')
        print('------------ Closest Pair --------------')

        # Creates a list of tuples with (x, y) values
        num_of_points = int(input('\nEnter the amount of points on the x, y axis:\n>'))
        random_points = [(random.choice(range(1, 100)), random.choice(range(1, 100))) for _num in range(0, num_of_points)]

        # only compare with 2 or more coordinates
        if num_of_points > 2:

            point_pair_distance = []

            print(f'\nPoints = {random_points}')
            print('----------------------------------------\n')

            # Pair up every possible combinations
            all_possible_pairs = [(random_points[x], random_points[y]) for x in range(len(random_points)) for y in range(x + 1, len(random_points))]
            print(f'{len(all_possible_pairs)} possible pairs:\n')

            # Calculates distance of all these pairs and saves them in a list of tuples (distance, coord1, coord2)
            for coord1, coord2 in all_possible_pairs:
                print(coord1, coord2)
                point_pair_distance.append([math.sqrt(((coord1[0] - coord2[0]) ** 2) + ((coord1[1] - coord2[1]) ** 2)), coord1, coord2])

            # Tuple unpacking to find the smallest distance
            min_distance, min_coord1, min_coord2 = min(point_pair_distance)

            # Prints results
            print(f'\nThe smallest distance is: {min_distance}\n\nFound between {min_coord1} and {min_coord2}\n')

        else:
            print('INVALID INPUT')

    except ValueError:
        print('INVALID INPUT')

    retry_option(closest_pair)


def Sieve_of_Eratosthenes():
    try:
        print('\n---------- CLASSIC ALGORITHMS ----------\n')
        print('-------- Sieve of Eratosthenes ---------')

        # Creates a list of range: 2 - n
        range_of_num = int(input('\nEnter upper limit of array (must be 2 or larger)\n>'))

        if range_of_num > 2:

            all_nums = [num for num in range(2, range_of_num + 1)]
            print(f'Unsearched list = {all_nums}\n')

            # p is the current prime being searched
            p = 2
            index = 0

            list_length = len(all_nums)

            while index < list_length - 1:

                for num in all_nums:
                    if num == p:
                        pass

                    # Removes all numbers from list that a multiples of the current p
                    elif num % p == 0:
                        all_nums.remove(num)

                # Shows current algorithm progress
                print(f'Removing factors of {p}:')
                print(f'{all_nums}\n')

                # Changes p to next available number in list
                list_length = len(all_nums)
                index += 1
                p = all_nums[index]

            # Prints results
            print(f'Found {len(all_nums)} primes from 0-{range_of_num}\n')
            print('Prime Searching Complete!')

        else:
            print('INVALID INPUT')

    except ValueError:
        print('INVALID INPUT')

    retry_option(Sieve_of_Eratosthenes)


main_menu()
