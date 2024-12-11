inputList = [
    [-3, 12],
    [4, 1],
    [6, 0],
    [4, 1],
    [1, -7]
]
sortedList = []
print(f"unsorted list :  {inputList}")
lowList = inputList[0][0]
lowNum = 0

def filter():
    global lowList, lowNum

    state = 0
    for i in inputList:
        if i[1] < lowList:
            lowNum = state
        lowList = i[1]

        state+=1
    sortedList.append(inputList[lowNum])
    inputList.pop(lowNum)
    lowNum = 0

for i in range(5):
    filter()


print(f"sorted list :    {sortedList}")