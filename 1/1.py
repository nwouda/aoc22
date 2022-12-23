#!/usr/bin/env python

input = open('1.txt', 'r')

elves = []
elf = 0

for line in input.readlines():
    try:
        type(elves[elf])
    except IndexError:
        elves.append([])

    if line != '\n':
        elves[elf].append(int(line))

    if line == '\n':
        elf += 1

print(f'Elves: {len(elves)}')
print(f'Sample: {elves[0][2]}')
print(f'Example: {sum(elves[0])}')

calories = []
for elf in elves:
    calories.append(sum(elf))

print(f'From list: {calories[0]}')

print(f'Answer: {max(calories)}')

print(f'Top three: {sorted(calories, reverse=True)[0:3]}')
print(f'Answer: {sum(sorted(calories, reverse=True)[0:3])}')