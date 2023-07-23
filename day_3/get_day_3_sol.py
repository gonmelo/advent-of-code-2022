
# Create priority dictionary
priority = {}
for ascii in range(65, 91):
    priority[chr(ascii)] = ascii - 38
for ascii in range(97, 123):
    priority[chr(ascii)] = ascii - 96

# open input file and read its lines into a list
with open("day_3_input.txt", "r") as f:
    rucksacks = f.readlines()

def get_sol_1(rucksacks, priority):
    result = 0

    # Iterate over rucksacks,break them into compartments and check for co-occuring item
    for rucksack in rucksacks:
        comp_1 = rucksack[:len(rucksack)//2]
        comp_2 = rucksack[len(rucksack)//2:]
    
        for char in comp_1:
            if char in comp_2:
                result += priority[char]
                break   # Needed to avoid counting the same item type more than once
    print('Solution 1: ', result)


def get_sol_2(rucksacks, priority):
    result = 0
    grouped_rucksacks = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]

    for group in grouped_rucksacks:
        for char in group[0]:
            if char in group[1] and char in group[2]:
                result += priority[char]
                break
    print('Solution 2: ', result)



def main():
    get_sol_1(rucksacks, priority)
    get_sol_2(rucksacks, priority)


if __name__ == '__main__':
    main()
