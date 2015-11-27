# 1.Count words


def count_words(arr):

    res = {}
    for word in arr:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res

print count_words(["python", "python", "python", "ruby"])

# 2.NaN Expand


def nan_expand(times):
    start = "Not a "
    end = "NaN"
    result = ""
    for i in range(0, times):
        result += start
    if len(result) != 0:
        result += end
    print result

nan_expand(5)

# 3.Iterations of NaN Expand


def iterations_of_nan_expand(expanded):

    count = 0

    if (len(expanded) == 0):
        return 0

    elif not ("NaN" in expanded):
        return "false"
    else:
        words = expanded.split(' ')
        for word in words:
            if word == "Not":
                count += 1
    return count


print iterations_of_nan_expand("Not a NaN")

# 4.The group function


def group(arr):

    count = 1
    result = []

    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1]:
            count += 1
            continue
        result.append([arr[i] for x in range(count)])
        count = 1

    # for last seq or element
    result.append([arr[len(arr) - 1] for x in range(count)])
    count = 1

    return result

print group([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])

# 5. Longest sequence


def max_consecutive(items):
    max_count = 0
    count = 1

    for i in range(0, len(items) - 1):
        if items[i] == items[i + 1]:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 1
    return max_count

print max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])

# Gas Stations


def gas_stations(distance, tank_size, stations):
    road_fuel = [stations[0]]

    for i in range(1, len(stations)):
        road_fuel.append(stations[i] - stations[i - 1])

    road_fuel.append(distance - stations[len(stations) - 1])

    count = road_fuel[0]
    for i in range(1, len(road_fuel) - 1):
        if(count + road_fuel[i + 1] < tank_size):
        	#count += road_fuel[i]
        	print count
        else:
        	print stations[i-1]
        	count = 0
    print road_fuel

gas_stations(320, 90, [50, 80, 140, 180, 220, 290])

# Sum all numbers in a given string


def sum_of_numbers(st):

    numbers = []
    curr_num = ""

    for i in range(0, len(st)):
        if st[i].isdigit():
            curr_num += st[i]
        else:
            if curr_num.isdigit():
                numbers.append(int(curr_num))
            curr_num = ""
    # last curr_num from the loop
    if curr_num.isdigit():
        numbers.append(int(curr_num))
    return sum(numbers)

print sum_of_numbers("1abc33xyz22a1")

# 6. Number To Message

KEYBOARD = {}
KEYBOARD[2] = ['a', 'b', 'c']
KEYBOARD[3] = ['d', 'e', 'f']
KEYBOARD[4] = ['g', 'h', 'i']
KEYBOARD[5] = ['j', 'k', 'l']
KEYBOARD[6] = ['m', 'n', 'o']
KEYBOARD[7] = ['p', 'q', 'r', 's']
KEYBOARD[8] = ['t', 'u', 'v']
KEYBOARD[9] = ['w', 'x', 'y', 'z']


def numbersToMessage(pressedSequence):

    pressed = group(pressedSequence)
    result = ""
    upper = False

    for combo in pressed:
        key = combo[0]
        count = len(combo)
        if key != -1:
            if key == 0:
                result += " "
                continue
            if key == 1:
                upper = True
                continue
            if upper:
                symbol = (
                    KEYBOARD[key][(count - 1) % len(KEYBOARD[key])]).upper()
                upper = False
            else:
                symbol = KEYBOARD[key][(count - 1) % len(KEYBOARD[key])]
            result += symbol

    print result

numbersToMessage(
    [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])


numbersToMessage([2, -1, 2, 2, -1, 2, 2, 2])

# 7. Message To Number


def messageToNumbers(messsage):

    button = 0
    index = 0
    sequence = []
    upper = False
    already_used = set()

    for ch in messsage:
        if ch == ' ':
            sequence.append(0)
            continue

        for i in range(2, len(KEYBOARD) + 2):

            for j in range(0, len(KEYBOARD[i])):
                if ch == KEYBOARD[i][j].upper():
                    upper = True

            if ch in KEYBOARD[i] or upper:
                button = i
                for pos in range(0, len(KEYBOARD[button])):
                    if KEYBOARD[button][pos] == ch.lower():
                        index = pos + 1
                        if upper:
                            sequence.append(1)
                        if len((set(KEYBOARD[button]) - already_used)) < len(KEYBOARD[button]):
                            sequence.append(-1)
                        sequence.append([button for x in range(index)])
                        already_used.clear()
                        already_used.add(KEYBOARD[button][index - 1])
                        # print already_used
            upper = False

    print sequence

messageToNumbers("aabcahahbbah")
messageToNumbers("Ivo e Panda")
