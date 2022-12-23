#!/usr/bin/env python
from pandas import read_fwf, DataFrame, Series
from io import StringIO


input = open('5.txt', 'r')
data = []
build_frame = True
data_prepped = ''
print('starting')
for line in input.readlines():
    if build_frame and line != '\n':

        data.append(line)
    elif build_frame and line == '\n':
        build_frame = False
        data.reverse()
        for l in data:
            data_prepped += l
        file = StringIO(data_prepped)
        df = read_fwf(file, infer_nrows=2)
        print(df)
        stacks = df.to_dict(orient='list')
        for k,v in stacks.items():
            stacks[k] = list(filter(lambda val: isinstance(val, str), v))
        print('\nStart processing\n')
    elif not build_frame:
        splitline = line.split(' ')
        amount = splitline[1]
        source = splitline[3]
        destination = splitline[5].strip('\n')
        print(f'Move {amount} from {source} to {destination}')        
        print(f'Source: {stacks[source]}')
        print(f'Destination: {stacks[destination]}')
        on_crane = []
        for i in range(0, int(amount)):
            on_crane.append(stacks[source].pop())
        print(on_crane)
        for i in range(0, int(amount)):
            stacks[destination].append(on_crane.pop())
        print(f'Source: {stacks[source]}')
        print(f'Destination: {stacks[destination]}')

answer = ''
for stack in stacks.items():
    answer += stack[-1][-1]
print(answer)
print(DataFrame({ key:Series(value) for key, value in stacks.items() }))
