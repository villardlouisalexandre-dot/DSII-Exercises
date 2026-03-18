# =========================
# EXERCICE 1 — Smallest of Three Numbers
# =========================
def exo1():
    def smallest(a, b, c):
        return min(a, b, c)

    a = int(input())
    b = int(input())
    c = int(input())

    print(smallest(a, b, c))


# =========================
# EXERCICE 2 — Vowels Count
# =========================
def exo2():
    def count_vowels(text):
        vowels = "aeiouAEIOU"
        return sum(1 for ch in text if ch in vowels)

    text = input()
    print(count_vowels(text))


# =========================
# EXERCICE 3 — Characters in Range
# =========================
def exo3():
    def chars_in_range(a, b):
        start = min(ord(a), ord(b))
        end = max(ord(a), ord(b))
        return " ".join(chr(i) for i in range(start + 1, end))

    a = input()
    b = input()

    print(chars_in_range(a, b))


# =========================
# EXERCICE 4 — Password Validator
# =========================
def exo4():
    def valid_length(password):
        return 6 <= len(password) <= 10

    def only_letters_digits(password):
        return password.isalnum()

    def at_least_two_digits(password):
        return sum(ch.isdigit() for ch in password) >= 2

    password = input()
    is_valid = True

    if not valid_length(password):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not only_letters_digits(password):
        print("Password must consist only of letters and digits")
        is_valid = False
    if not at_least_two_digits(password):
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


# =========================
# EXERCICE 5 — Add and Subtract
# =========================
def exo5():
    def add(a, b):
        return a + b

    def subtract(result, c):
        return result - c

    a = int(input())
    b = int(input())
    c = int(input())

    print(subtract(add(a, b), c))


# =========================
# EXERCICE 6 — Middle Characters
# =========================
def exo6():
    def middle_chars(text):
        n = len(text)
        mid = n // 2
        if n % 2 == 0:
            return text[mid - 1:mid + 1]
        return text[mid]

    text = input()
    print(middle_chars(text))


# =========================
# EXERCICE 7 — NxN Matrix
# =========================
def exo7():
    def print_matrix(n):
        for _ in range(n):
            print(" ".join([str(n)] * n))

    n = int(input())
    print_matrix(n)


# =========================
# EXERCICE 8 — Factorial Division
# =========================
def exo8():
    def factorial(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    a = int(input())
    b = int(input())

    print(f"{factorial(a) / factorial(b):.2f}")


# =========================
# EXERCICE 9 — Palindrome Integers
# =========================
def exo9():
    def is_palindrome(num):
        return num == num[::-1]

    while True:
        command = input()
        if command == "END":
            break
        print("true" if is_palindrome(command) else "false")


# =========================
# EXERCICE 10 — Top Number
# =========================
def exo10():
    def sum_digits_divisible_by_8(num):
        return sum(int(d) for d in str(num)) % 8 == 0

    def has_odd_digit(num):
        return any(int(d) % 2 == 1 for d in str(num))

    n = int(input())

    for num in range(1, n + 1):
        if sum_digits_divisible_by_8(num) and has_odd_digit(num):
            print(num)


# =========================
# EXERCICE 11 — Array Manipulator
# =========================
def exo11():
    def get_filtered(nums, parity):
        if parity == "even":
            return [x for x in nums if x % 2 == 0]
        return [x for x in nums if x % 2 != 0]

    nums = list(map(int, input().split()))

    while True:
        command = input().split()
        if command[0] == "end":
            break

        if command[0] == "exchange":
            index = int(command[1])
            if 0 <= index < len(nums):
                nums = nums[index + 1:] + nums[:index + 1]
            else:
                print("Invalid index")

        elif command[0] in ("max", "min"):
            parity = command[1]
            indices = [i for i, x in enumerate(nums) if (x % 2 == 0 if parity == "even" else x % 2 != 0)]
            if not indices:
                print("No matches")
            else:
                if command[0] == "max":
                    target = max(nums[i] for i in indices)
                else:
                    target = min(nums[i] for i in indices)
                result = max(i for i in indices if nums[i] == target)
                print(result)

        elif command[0] in ("first", "last"):
            count = int(command[1])
            parity = command[2]
            if count > len(nums):
                print("Invalid count")
                continue

            filtered = get_filtered(nums, parity)

            if command[0] == "first":
                print(filtered[:count])
            else:
                print(filtered[-count:])

    print(nums)


# =========================
# MENU
# =========================
while True:
    choix = input("Choisis un exo (1-11) ou 'exit' : ")

    if choix == "1":
        exo1()
    elif choix == "2":
        exo2()
    elif choix == "3":
        exo3()
    elif choix == "4":
        exo4()
    elif choix == "5":
        exo5()
    elif choix == "6":
        exo6()
    elif choix == "7":
        exo7()
    elif choix == "8":
        exo8()
    elif choix == "9":
        exo9()
    elif choix == "10":
        exo10()
    elif choix == "11":
        exo11()
    elif choix == "exit":
        break
    else:
        print("Choix invalide")
