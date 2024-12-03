from itertools import count

import numpy

def exerciseone(line):
    goodcounter = 0
    # line = ['69', '72', '75', '78', '80', '79']
    inputs = [int(x) for x in line]
    # print('pass 1')
    # print(inputs)
    inputsforwards = inputs.copy()
    # print('pass 2')
    # print(inputsforwards)
    inputsreveresed = inputs.copy()
    # inputsforwards.sort()
    # print('passs 2')
    # print(inputs)
    # print(sorted(inputsforwards,key=int, reverse=False))
    # print('pass 3')
    # inputsreveresed.reverse()
    # print(inputs)
    # print(sorted(inputsreveresed,key=int, reverse=True))

    badcounter = 0
    badforwards = sorted(inputsforwards,key=int, reverse=False) == inputs
    # print(badforwards)
    badreverse = sorted(inputsreveresed,key=int, reverse=True) == inputs
    # print(badreverse)
    if badreverse == True or badforwards == True:
        diffinelements = numpy.diff(inputs)
        # print(diffinelements)
        outofrange = 0
        for i in diffinelements:
            goodvalues = [-3,-2,-1,1,2,3]
            # print(i)
            if i not in goodvalues:
                # print('here')
                outofrange += 1
            # print(f'outofrange counter {outofrange}')
            if outofrange > 0:
                badcounter += 1
            # print(f'badcounter1 {badcounter}')
    else:
        badcounter += 1
    # print(f'badcounter2 {badcounter}')
    if badcounter == 0:
        goodcounter += 1
    # print(f'The answer is {goodcounter}')
    return goodcounter

# line = ['69', '72', '75', '78', '80', '82','90','95']
# line = ['28', '31', '34', '31', '35']
# line = ['28', '31', '34', '35']
line = ['69', '72', '75', '78', '80', '79']
goodcounter = 0
result = exerciseone(line)
# print(exerciseone(line))
goodcounter += result
# if result == 1:
    # print('success')
#     attempt to fix
fixablerows = 0
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
        result = exerciseone(myline)
        counter += 1
        # print(result)
        # print(f'end of run {counter + 1} ')
        # print(f'counter: {counter}')
        if result == 1:
            # print('this line can be fixed by removing one element')
            fixablerows += 1
        else:
            # print('This line cant be fixed')
            pass
