with open("day_4_input.txt", "r") as f:
    elf_pairs = f.readlines()


def get_sols(elf_pairs):
    contained_assignments = 0   # Solution for problem 1
    overlapping_assignments = 0  # Solution for problem 2

    for elf_pair in elf_pairs:
        # Format input and cast to ints for easier processing
        assign_1, assign_2 = elf_pair.split(',')
        assign_1 = [int(x) for x in assign_1.split('-')]
        assign_2 = [int(x) for x in assign_2.split('-')]

        # Check if the an assignment is contained in the other
        if assign_1[0] >= assign_2[0] and assign_1[1] <= assign_2[1] or assign_2[0] >= assign_1[0] and assign_2[1] <= assign_1[1]:
            contained_assignments += 1
            overlapping_assignments += 1
        # Check if the assignments overlap
        elif assign_1[0] <= assign_2[0] <= assign_1[1] or assign_1[0] <= assign_2[1] <= assign_1[1]:
            overlapping_assignments += 1

    print('Solution 1: ', contained_assignments)
    print('Solution 2: ', overlapping_assignments)


def main():
    get_sols(elf_pairs)


if __name__ == '__main__':
    main()
