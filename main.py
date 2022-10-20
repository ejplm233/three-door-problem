import random


def three_doors_no_switch():
    choice = [0, 1, 2]
    all_choices = [True, False, False]
    picked_position = random.choices(choice)[0]
    result = all_choices[picked_position]
    return result


def three_doors_switch():
    choice = [0, 1, 2]
    all_choices = [True, False, False]
    picked_position = random.choices(choice)[0]
    result = all_choices[picked_position]
    all_choices.remove(result)
    all_choices.remove(False)
    if all_choices[0] is True:
        return True
    else:
        return False


def main():
    no_switch = 0
    switch = 0
    n = 100000
    for i in range(n):
        if three_doors_switch() is True:
            switch += 1
    print("Number of switch is", switch)

    for i in range(n):
        if three_doors_no_switch() is True:
            no_switch += 1
    print("Number of no_switch is", no_switch)


if __name__ == "__main__":
    main()
