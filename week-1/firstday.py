# Sum of all digits of a number


def sum_of_digits(n):

    result = 0
    while (n > 0):
        result += n % 10
        n /= 10

    return result

print (sum_of_digits(1325132435356))

# Turn a number into a list of digits


def to_digits(n):
    num_as_str = str(n)
    digits_array = []
    print(num_as_str)

    for c in num_as_str:
        digits_array.append(int(c))

    print digits_array

print (to_digits(12312))

# Turn a list of digits into a number


def digits_number(n):
    count = 0
    if n == 0:
        return 1
    while (n > 0):
        n /= 10
        count += 1
    return count


def power_of_ten(arr):
    count = 0
    for el in arr:
        count += digits_number(el)
    return count


def to_number(digits):
    result = 0
    index = 1
    for num in digits:
        multiplicator = power_of_ten(digits[index::])
        result += num * 10**multiplicator
        print "multiplicator " + str(multiplicator)
        print result
        index += 1

    return result
print (to_number([22, 5, 13]))


# Factorial Digits
def factorial(n):
    if (n == 1):
        return 1

    return n * factorial(n - 1)


def fact_digits(number):
    result = 0

    while (number > 0):
        digit = number % 10
        number /= 10
        result += factorial(digit)

    return result

print (fact_digits(999))

# First nth members of Fibonacci


def fibonacci(n):
    sequence = [1]
    first = 0
    second = 1

    for i in range(1, n):
        sequence.append(first + second)
        temp = first
        first = second
        second = temp + second

    return sequence

print fibonacci(7)
# a, b = 1,1
# a, b = b, a + b

# Fibonacci number


def fib_number(n):
    chain = fibonacci(n)
    result = ""
    for el in chain:
        result += str(el)
    return result


print (fib_number(10))

# Palindrome


def palindrome(obj):
    text = str(obj)
    for i in xrange(0, len(text)): 
        if (text[i] != text[len(text) - 1 - i]):
            return False


    return True

print palindrome("kapsdpak")

# count vowels in a string


def count_vowels(word):
    count = 0
    lower_word = word.lower()
    all_vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for ch in lower_word:
        for i in xrange(0, len(all_vowels)):
            if (ch == all_vowels[i]):
                count += 1
                continue
    return count

print count_vowels("Github is the second best thing that happend to programmers, after the keyboard!")

# count consonants
#  B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X,Z


def check_consonats(word):
    count = 0
    lower_word = word.lower()

    allCons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
               'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    for ch in lower_word:
        for i in xrange(0, len(allCons)):
            if (ch == allCons[i]):
                count += 1
                continue

    return count

print check_consonats("Github is the second best thing that happend to programmers, after the keyboard!")

# char histogram


def char_histogram(sequence):
    histogram = {}
    for el in sequence:
        if (not histogram.has_key(el)):
            histogram[el] = 1
        else:
            histogram[el] += 1

    for i in histogram:
        print (str(i) + "= " + str(histogram[i]))

char_histogram("AAAAaaa!!!")
