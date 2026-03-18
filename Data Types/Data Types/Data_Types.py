# =========================
# EXERCICE 1 — Integer Operations
# =========================
def exo1():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())

    result = ((n1 + n2) // n3) * n4
    print(result)


# =========================
# EXERCICE 2 — Sum Digits
# =========================
def exo2():
    n = input()
    print(sum(int(ch) for ch in n))


# =========================
# EXERCICE 3 — Elevator
# =========================
def exo3():
    import math
    n = int(input())
    p = int(input())
    print(math.ceil(n / p))


# =========================
# EXERCICE 4 — Sum of Chars
# =========================
def exo4():
    n = int(input())
    total = 0

    for _ in range(n):
        total += ord(input())

    print(f"The sum equals: {total}")


# =========================
# EXERCICE 5 — ASCII Table
# =========================
def exo5():
    start = int(input())
    end = int(input())

    print(" ".join(chr(i) for i in range(start, end + 1)))


# =========================
# EXERCICE 6 — Triples of Latin Letters
# =========================
def exo6():
    n = int(input())

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")


# =========================
# EXERCICE 7 — Water Overflow
# =========================
def exo7():
    n = int(input())
    capacity = 255
    current = 0

    for _ in range(n):
        liters = int(input())
        if current + liters > capacity:
            print("Insufficient capacity!")
        else:
            current += liters

    print(current)


# =========================
# EXERCICE 8 — Beer Kegs
# =========================
def exo8():
    import math

    n = int(input())
    best_model = ""
    best_volume = -1

    for _ in range(n):
        model = input()
        radius = float(input())
        height = int(input())
        volume = math.pi * radius ** 2 * height

        if volume > best_volume:
            best_volume = volume
            best_model = model

    print(best_model)


# =========================
# EXERCICE 9 — Spice Must Flow
# =========================
def exo9():
    yield_amount = int(input())
    days = 0
    total = 0

    while yield_amount >= 100:
        total += yield_amount - 26
        days += 1
        yield_amount -= 10

    if total >= 26:
        total -= 26
    else:
        total = 0

    print(days)
    print(total)


# =========================
# EXERCICE 10 — Pokemon
# =========================
def exo10():
    n = int(input())
    m = int(input())
    y = int(input())

    original_n = n
    count = 0
    half = original_n * 0.5

    while n >= m:
        n -= m
        count += 1
        if n == half and y != 0:
            n //= y

    print(n)
    print(count)


# =========================
# EXERCICE 11 — Snowballs
# =========================
def exo11():
    n = int(input())

    best_value = -1
    best_snow = 0
    best_time = 0
    best_quality = 0

    for _ in range(n):
        snow = int(input())
        time = int(input())
        quality = int(input())

        value = (snow // time) ** quality

        if value > best_value:
            best_value = value
            best_snow = snow
            best_time = time
            best_quality = quality

    print(f"{best_snow} : {best_time} = {best_value} ({best_quality})")


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