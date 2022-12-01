# AoC 2022 Day1
# Charles Twardy
# Done with nano and commandline

# Get list of calories
with open("input.txt") as f:
    lines = f.readlines()

# Break up our calorie list by elf
i, elves, elf = 1, [], []
for line in lines:
    line = line.strip()
    if line:
        elf.append(int(line))
        continue
    elves.append(elf)
    print(f"Elf {i}: {elf}")
    i += 1
    elf = []

sums = [sum(elf) for elf in elves]
print()

# Part 1
print(f"Max: {max(sums):,} calories")

# Part 2
top3 = sorted(sums)[-3:]
print(f"Top3: {sum(top3):,} calories from {top3}")

