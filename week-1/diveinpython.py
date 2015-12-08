from math import sqrt, floor
import copy

# 1.Is Number Balanced?


def is_number_balanced(n):
    num_as_str = str(n)
    left_sum, right_sum = 0, 0
    for i in range(0, len(num_as_str) / 2):
        left_sum += int(num_as_str[i])
        right_sum += int(num_as_str[len(num_as_str) - 1 - i])

    return left_sum == right_sum

print is_number_balanced(1238033)

# 2.Increasing and Decreasing Sequences


def is_increasing(seq):
    for i in range(0, len(seq) - 1):
        if (not (seq[i] < seq[i + 1])):
            return False
    return True

print is_increasing([1, 1, 1, 1])

# 2.2 Descreasing sequence?


def is_decreasing(seq):
    for i in range(0, len(seq) - 1):
        if (not (seq[i] > seq[i + 1])):
            return False
    return True

print is_decreasing([100, 50, 20])

# 3. Largest Palindrome


def palindrome(obj):
    text = str(obj)
    for i in range(0, len(text)):
        if (text[i] != text[len(text) - 1 - i]):
            return False
    return True


def get_largest_palindrome(n):
    num = n
    while True:
        if palindrome(num - 1):
            return (num - 1)
        else:
            num -= 1

print get_largest_palindrome(994687)
print get_largest_palindrome(99)

# 4. Prime Numbers


def prime_numbers(n):
    rootN = int(floor(sqrt(n + 1)))
    length = n + 2
    all_num = [True for x in range(0, length)]
    all_num[0], all_num[1] = False, False

    for i in range(2, rootN + 1):
        if all_num[i] is True:
            for j in range(i * i, length, i):
                all_num[j] = False

    result = []
    for i in range(2, length):

        if all_num[i] is True:
            result.append(i)

    print result

prime_numbers(5)

# 5. Anagrams


def create_dict_from_word(word):
    result = {}
    for ch in word:
        if ch not in result:
            result[ch] = 1
        else:
            result[ch] += 1
    return result


def is_anagram(a, b):

    first = str(a).lower()
    second = str(b).lower()

    first_dict = create_dict_from_word(first)
    second_dict = create_dict_from_word(second)

    if len(first_dict) != len(second_dict):
        return False

    return first_dict == second_dict

print is_anagram("dsa", "ASD")

# 6. Birthday Ranges


def is_num_inside_tuple(n, tpl):
    return ((n >= tpl[0]) and (n <= tpl[1]))


def birthday_ranges(birthdays, ranges):
    result = []
    for tpl in ranges:
        count = 0
        for num in birthdays:
            if is_num_inside_tuple(num, tpl):
                count += 1
        result.append(count)

    return result


print birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])

print birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])

# 7. Sum Numbers in Matrix


def sum_matrix(mtx):
    rows = len(mtx)
    cols = len(mtx[1])
    result = 0

    for i in range(0, rows):
        for j in range(0, cols):
            result += mtx[i][j]
    return result


print sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])


# 8. Bombing matrix

def within_bounds(mtx, coords, check):
    if (coords[0] + check[0]) < 0 or (coords[0] + check[0]) > (len(mtx) - 1):
        return False
    if (coords[1] + check[1]) < 0 or (coords[1] + check[1]) > (len(mtx[1]) - 1):
        return False
    return True


def do_bombing(mtx, curr_coord, value):
    combo = [-1, 0, 1]
    copy_mtx = copy.deepcopy(mtx)
    x = curr_coord[0]
    y = curr_coord[1]
    for i in range(0, len(combo)):
        for j in range(0, len(combo)):
            add_x = combo[i]
            add_y = combo[j]
            if not (add_x == 0 and add_y == 0):
                if within_bounds(mtx, curr_coord, [add_x, add_y]):
                    copy_mtx[x + add_x][add_y + y] -= min(
                        value, mtx[x + add_x][add_y + y])
    return sum_matrix(copy_mtx)


def bombing_matrix(mtx):
    result = {}
    for row in range(0, len(mtx)):
        for col in range(0, len(mtx[0])):
            cell_value = mtx[row][col]
            bomb_res = do_bombing(mtx, [row, col], cell_value)
            result[(row, col)] = bomb_res

    return result

mtx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print bombing_matrix(mtx)

# 9.Transversal


def is_transversal(transversal, family):
    for tr_set in family:
        if len(set(transversal) - set(tr_set)) == len(transversal):
            return False
    return True

print is_transversal([2, 3, 4], [[1, 7], [2, 3, 5], [4, 8]])
