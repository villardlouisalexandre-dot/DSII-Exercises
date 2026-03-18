# =========================
# EXERCICE 1 — Train
# =========================
def exo1():
    n = int(input())
    wagons = []
    total = 0

    for _ in range(n):
        people = int(input())
        wagons.append(people)
        total += people

    print(*wagons)
    print(total)


# =========================
# EXERCICE 2 — Common Elements
# =========================
def exo2():
    first = input().split()
    second = input().split()

    common = [x for x in second if x in first]
    print(*common)


# =========================
# EXERCICE 3 — Zig-Zag Arrays
# =========================
def exo3():
    n = int(input())
    first = []
    second = []

    for i in range(n):
        a, b = input().split()
        if i % 2 == 0:
            first.append(a)
            second.append(b)
        else:
            first.append(b)
            second.append(a)

    print(*first)
    print(*second)


# =========================
# EXERCICE 4 — Array Rotation
# =========================
def exo4():
    arr = input().split()
    rotations = int(input())
    rotations %= len(arr)

    arr = arr[rotations:] + arr[:rotations]
    print(*arr)


# =========================
# EXERCICE 5 — Top Integers
# =========================
def exo5():
    nums = list(map(int, input().split()))
    result = []

    for i in range(len(nums)):
        if all(nums[i] > nums[j] for j in range(i + 1, len(nums))):
            result.append(nums[i])

    print(*result)


# =========================
# EXERCICE 6 — Equal Sums
# =========================
def exo6():
    nums = list(map(int, input().split()))

    for i in range(len(nums)):
        left = sum(nums[:i])
        right = sum(nums[i+1:])
        if left == right:
            print(i)
            return

    print("no")


# =========================
# EXERCICE 7 — Max Sequence of Equal Elements
# =========================
def exo7():
    nums = input().split()

    best_seq = []
    current_seq = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_seq.append(nums[i])
        else:
            if len(current_seq) > len(best_seq):
                best_seq = current_seq[:]
            current_seq = [nums[i]]

    if len(current_seq) > len(best_seq):
        best_seq = current_seq[:]

    print(*best_seq)


# =========================
# EXERCICE 8 — Magic Sum
# =========================
def exo8():
    nums = list(map(int, input().split()))
    target = int(input())

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(nums[i], nums[j])


# =========================
# EXERCICE 9 — Kamino Factory
# =========================
def exo9():
    n = int(input())

    best_dna = []
    best_length = -1
    best_index = n
    best_sum = -1
    best_sample = 0
    sample_count = 0

    while True:
        line = input()
        if line == "Clone them!":
            break

        dna = [int(x) for x in line.split("!") if x != ""]
        sample_count += 1

        current_best_len = 0
        current_best_start = n
        current_len = 0
        current_start = 0

        for i, val in enumerate(dna):
            if val == 1:
                if current_len == 0:
                    current_start = i
                current_len += 1
                if current_len > current_best_len:
                    current_best_len = current_len
                    current_best_start = current_start
            else:
                current_len = 0

        dna_sum = sum(dna)

        better = False
        if current_best_len > best_length:
            better = True
        elif current_best_len == best_length:
            if current_best_start < best_index:
                better = True
            elif current_best_start == best_index and dna_sum > best_sum:
                better = True

        if better:
            best_dna = dna
            best_length = current_best_len
            best_index = current_best_start
            best_sum = dna_sum
            best_sample = sample_count

    print(f"Best DNA sample {best_sample} with sum: {best_sum}.")
    print(*best_dna)


# =========================
# EXERCICE 10 — LadyBugs
# =========================
def exo10():
    size = int(input())
    field = [0] * size
    initial_indexes = list(map(int, input().split()))

    for idx in initial_indexes:
        if 0 <= idx < size:
            field[idx] = 1

    while True:
        command = input()
        if command == "end":
            break

        idx, direction, fly_length = command.split()
        idx = int(idx)
        fly_length = int(fly_length)

        if not (0 <= idx < size) or field[idx] == 0:
            continue

        field[idx] = 0

        if fly_length < 0:
            fly_length = abs(fly_length)
            direction = "left" if direction == "right" else "right"

        position = idx
        while True:
            if direction == "right":
                position += fly_length
            else:
                position -= fly_length

            if position < 0 or position >= size:
                break

            if field[position] == 0:
                field[position] = 1
                break

    print(*field)


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
