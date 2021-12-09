def Sieve_of_Eratosthenes(limit):
    all_nums = [num for num in range(2, limit + 1)]
    print(f'Unsearched list = {all_nums}\n')

    p = 2
    index = 0

    list_length = len(all_nums)

    while p < list_length:

        for num in all_nums:
            if num == p:
                pass

            elif num % p == 0:
                all_nums.remove(num)

        print(f'Removing factors of {p}:')
        print(f'{all_nums}\n')

        list_length = len(all_nums)
        index += 1
        p = all_nums[index]






Sieve_of_Eratosthenes(100)
