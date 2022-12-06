from bisect import bisect


def get_solution_1():
    """Solution to the 1st problem"""
    max_calories = 0
    current_calories = 0
    with open("day_1_input.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip():
            current_calories += int(line)
        else:
            if current_calories > max_calories:
                max_calories = current_calories  # We can do it here since the last line of the input is empty
            current_calories = 0
    print(f"The elf carrying the most calories has: {max_calories} cals.")


def get_solution_2():
    """Solution for the 2nd problem"""
    current_calories = 0
    calories_by_elf = []
    with open("day_1_input.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip():
            current_calories += int(line)
        else:
            calories_by_elf.append(current_calories)
            current_calories = 0
    solution = sum(sorted(calories_by_elf, reverse=True)[:3])
    print(f"The top 3 elfs are carrying {solution} cals in total.")


def main():
    get_solution_1()
    get_solution_2()


if __name__ == "__main__":
    main()
