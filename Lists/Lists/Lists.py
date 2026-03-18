# =========================
# EXERCICE 1 — Train
# =========================
def exo1():
    train = list(map(int, input().split()))
    capacity = int(input())

    while True:
        command = input()
        if command == "end":
            break

        parts = command.split()
        if parts[0] == "Add":
            train.append(int(parts[1]))
        else:
            passengers = int(parts[0])
            for i in range(len(train)):
                if train[i] + passengers <= capacity:
                    train[i] += passengers
                    break

    print(*train)


# =========================
# EXERCICE 2 — Change List
# =========================
def exo2():
    nums = list(map(int, input().split()))

    while True:
        command = input()
        if command == "end":
            break

        parts = command.split()
        if parts[0] == "Delete":
            element = int(parts[1])
            nums = [x for x in nums if x != element]
        elif parts[0] == "Insert":
            element = int(parts[1])
            position = int(parts[2])
            nums.insert(position, element)

    print(*nums)


# =========================
# EXERCICE 3 — House Party
# =========================
def exo3():
    n = int(input())
    guests = []

    for _ in range(n):
        parts = input().split()
        name = parts[0]

        if parts[2] == "going!":
            if name in guests:
                print(f"{name} is already in the list!")
            else:
                guests.append(name)
        else:
            if name in guests:
                guests.remove(name)
            else:
                print(f"{name} is not in the list!")

    print(*guests, sep="\n")


# =========================
# EXERCICE 4 — List Operations
# =========================
def exo4():
    nums = list(map(int, input().split()))

    while True:
        command = input().split()
        if command[0] == "End":
            break

        if command[0] == "Add":
            nums.append(int(command[1]))
        elif command[0] == "Insert":
            number = int(command[1])
            index = int(command[2])
            if 0 <= index < len(nums):
                nums.insert(index, number)
            else:
                print("Invalid index")
        elif command[0] == "Remove":
            index = int(command[1])
            if 0 <= index < len(nums):
                nums.pop(index)
            else:
                print("Invalid index")
        elif command[0] == "Shift":
            direction = command[1]
            count = int(command[2]) % len(nums)

            if direction == "left":
                nums = nums[count:] + nums[:count]
            else:
                nums = nums[-count:] + nums[:-count]

    print(*nums)


# =========================
# EXERCICE 5 — Bomb Numbers
# =========================
def exo5():
    nums = list(map(int, input().split()))
    bomb, power = map(int, input().split())

    while bomb in nums:
        idx = nums.index(bomb)
        left = max(0, idx - power)
        right = min(len(nums), idx + power + 1)
        del nums[left:right]

    print(sum(nums))


# =========================
# EXERCICE 6 — Cards Game
# =========================
def exo6():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    while first and second:
        c1 = first.pop(0)
        c2 = second.pop(0)

        if c1 > c2:
            first.extend([c1, c2])
        elif c2 > c1:
            second.extend([c2, c1])

    if first:
        print(f"First player wins! Sum: {sum(first)}")
    else:
        print(f"Second player wins! Sum: {sum(second)}")


# =========================
# EXERCICE 7 — Append Arrays
# =========================
def exo7():
    parts = input().split("|")
    result = []

    for part in reversed(parts):
        result.extend(part.split())

    print(*result)


# =========================
# EXERCICE 8 — Anonymous Threat
# =========================
def exo8():
    data = input().split()

    while True:
        command = input()
        if command == "3:1":
            break

        parts = command.split()
        action = parts[0]

        if action == "merge":
            start = int(parts[1])
            end = int(parts[2])

            start = max(0, start)
            end = min(len(data) - 1, end)

            if start <= end:
                merged = "".join(data[start:end + 1])
                data[start:end + 1] = [merged]

        elif action == "divide":
            index = int(parts[1])
            partitions = int(parts[2])
            element = data[index]

            part_size = len(element) // partitions
            result = []
            start = 0

            for i in range(partitions):
                if i == partitions - 1:
                    result.append(element[start:])
                else:
                    result.append(element[start:start + part_size])
                    start += part_size

            data[index:index + 1] = result

    print(" ".join(data))


# =========================
# EXERCICE 9 — Pokemon Don't Go
# =========================
def exo9():
    nums = list(map(int, input().split()))
    removed_sum = 0

    while nums:
        index = int(input())

        if index < 0:
            removed = nums[0]
            removed_sum += removed
            nums[0] = nums[-1]
        elif index >= len(nums):
            removed = nums[-1]
            removed_sum += removed
            nums[-1] = nums[0]
        else:
            removed = nums.pop(index)
            removed_sum += removed

        for i in range(len(nums)):
            if nums[i] <= removed:
                nums[i] += removed
            else:
                nums[i] -= removed

    print(removed_sum)


# =========================
# EXERCICE 10 — SoftUni Course Planning
# =========================
def exo10():
    schedule = input().split(", ")

    while True:
        command = input()
        if command == "course start":
            break

        parts = command.split(":")
        action = parts[0]
        lesson = parts[1]
        exercise = f"{lesson}-Exercise"

        if action == "Add":
            if lesson not in schedule:
                schedule.append(lesson)

        elif action == "Insert":
            index = int(parts[2])
            if lesson not in schedule:
                schedule.insert(index, lesson)

        elif action == "Remove":
            if lesson in schedule:
                schedule.remove(lesson)
            if exercise in schedule:
                schedule.remove(exercise)

        elif action == "Swap":
            lesson2 = parts[2]
            exercise2 = f"{lesson2}-Exercise"

            if lesson in schedule and lesson2 in schedule:
                i1, i2 = schedule.index(lesson), schedule.index(lesson2)
                schedule[i1], schedule[i2] = schedule[i2], schedule[i1]

                if exercise in schedule:
                    schedule.remove(exercise)
                    schedule.insert(schedule.index(lesson) + 1, exercise)

                if exercise2 in schedule:
                    schedule.remove(exercise2)
                    schedule.insert(schedule.index(lesson2) + 1, exercise2)

        elif action == "Exercise":
            if lesson in schedule:
                if exercise not in schedule:
                    schedule.insert(schedule.index(lesson) + 1, exercise)
            else:
                schedule.append(lesson)
                schedule.append(exercise)

    for i, lesson in enumerate(schedule, start=1):
        print(f"{i}.{lesson}")


# =========================
# MENU
# =========================
while True:
    choix = input("Choisis un exo (1-10) ou 'exit' : ")

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
    elif choix == "exit":
        break
    else:
        print("Choix invalide")
