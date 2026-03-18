# =========================
# EXERCICE 1 — Ages
# =========================
def exo1():
    age = int(input())
    if 0 <= age <= 2:
        print("baby")
    elif age <= 13:
        print("child")
    elif age <= 19:
        print("teenager")
    elif age <= 65:
        print("adult")
    else:
        print("elder")


# =========================
# EXERCICE 2 — Division
# =========================
def exo2():
    n = int(input())
    if n % 10 == 0:
        print("The number is divisible by 10")
    elif n % 7 == 0:
        print("The number is divisible by 7")
    elif n % 6 == 0:
        print("The number is divisible by 6")
    elif n % 3 == 0:
        print("The number is divisible by 3")
    elif n % 2 == 0:
        print("The number is divisible by 2")
    else:
        print("Not divisible")


# =========================
# EXERCICE 3 — Vacation
# =========================
def exo3():
    people = int(input())
    group_type = input()
    day = input()

    prices = {
        "Friday": {"Students": 8.45, "Business": 10.90, "Regular": 15.00},
        "Saturday": {"Students": 9.80, "Business": 15.60, "Regular": 20.00},
        "Sunday": {"Students": 10.46, "Business": 16.00, "Regular": 22.50},
    }

    paying_people = people
    if group_type == "Business" and people >= 100:
        paying_people -= 10

    total = paying_people * prices[day][group_type]

    if group_type == "Students" and people >= 30:
        total *= 0.85
    elif group_type == "Regular" and 10 <= people <= 20:
        total *= 0.95

    print(f"Total price: {total:.2f}")


# =========================
# EXERCICE 4 — Print and Sum
# =========================
def exo4():
    start = int(input())
    end = int(input())

    nums = list(range(start, end + 1))
    print(*nums)
    print(f"Sum: {sum(nums)}")


# =========================
# EXERCICE 5 — Login
# =========================
def exo5():
    username = input()
    password = username[::-1]

    for attempt in range(4):
        current = input()
        if current == password:
            print(f"User {username} logged in.")
            return
        if attempt == 3:
            print(f"User {username} blocked!")
        else:
            print("Incorrect password. Try again.")


# =========================
# EXERCICE 6 — Strong Number
# =========================
def exo6():
    n = input()

    fact = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}
    result = sum(fact[int(d)] for d in n)

    print("yes" if result == int(n) else "no")


# =========================
# EXERCICE 7 — Vending Machine
# =========================
def exo7():
    money = 0.0
    valid_coins = {0.1, 0.2, 0.5, 1.0, 2.0}
    prices = {
        "Nuts": 2.0,
        "Water": 0.7,
        "Crisps": 1.5,
        "Soda": 0.8,
        "Coke": 1.0,
    }

    while True:
        command = input()
        if command == "Start":
            break
        coin = float(command)
        if coin in valid_coins:
            money += coin
        else:
            print(f"Cannot accept {coin}")

    while True:
        product = input()
        if product == "End":
            break
        if product not in prices:
            print("Invalid product")
            continue
        if money >= prices[product]:
            money -= prices[product]
            print(f"Purchased {product.lower()}")
        else:
            print("Sorry, not enough money")

    print(f"Change: {money:.2f}")


# =========================
# EXERCICE 8 — Triangle of Numbers
# =========================
def exo8():
    n = int(input())
    for i in range(1, n + 1):
        print((str(i) + " ") * i)


# =========================
# EXERCICE 9 — Padawan Equipment
# =========================
def exo9():
    import math

    money = float(input())
    students = int(input())
    lightsaber_price = float(input())
    robe_price = float(input())
    belt_price = float(input())

    lightsabers = math.ceil(students * 1.1)
    free_belts = students // 6
    paid_belts = students - free_belts

    total = lightsabers * lightsaber_price + students * robe_price + paid_belts * belt_price

    if money >= total:
        print(f"The money is enough - it would cost {total:.2f}lv.")
    else:
        print(f"John will need {total - money:.2f}lv more.")


# =========================
# EXERCICE 10 — Rage Expenses
# =========================
def exo10():
    lost_games = int(input())
    headset_price = float(input())
    mouse_price = float(input())
    keyboard_price = float(input())
    display_price = float(input())

    headsets = lost_games // 2
    mice = lost_games // 3
    keyboards = lost_games // 6
    displays = keyboards // 2

    expenses = headsets * headset_price + mice * mouse_price + keyboards * keyboard_price + displays * display_price
    print(f"Rage expenses: {expenses:.2f} lv.")


# =========================
# EXERCICE 11 — Orders
# =========================
def exo11():
    n = int(input())
    total = 0

    for _ in range(n):
        price_per_capsule = float(input())
        days = int(input())
        capsules = int(input())
        order_price = price_per_capsule * days * capsules
        total += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")

    print(f"Total: ${total:.2f}")


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
