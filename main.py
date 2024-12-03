import numpy
import test
from PIL.ImageChops import difference
import os
goodcounter = 0
fixablerows = 0
with open('input.txt') as input1:
    for line in input1:
        # os.system('cls' if os.name == 'nt' else 'clear')
        line = line.split()
        # print('start')
        # print(line)
        result = test.exerciseone(line)
        goodcounter += result
        isrowfixable = 0
        if result != 1:
            counter = 0
            # print('here')
            for i in line:
                # print(f'start of run {counter + 1} ')
                # print(line)
                myline = line.copy()
                myline.pop(counter)
                # print(line)
                # print(myline)
                result = test.exerciseone(myline)
                counter += 1
                # print(result)
                # print(f'end of run {counter + 1} ')
                # print(f'counter: {counter}')
                if result == 1:
                    # print('this line can be fixed by removing one element')
                    isrowfixable += 1
                else:
                    # print('This line cant be fixed')
                    # input()
                    pass
        if isrowfixable > 0:
            fixablerows += 1

print(f'The answer is {goodcounter}')
print(f'{fixablerows} rows can be fixed by removing one element')
print(f'{fixablerows + goodcounter}')
