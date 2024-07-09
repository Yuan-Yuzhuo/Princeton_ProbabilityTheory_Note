from secrets import choice

list = [1,2,3]
times = 10000000
counterKeep = 0
counterChange = 0
count = 1

while(True):
    rightAnswer = choice(list)
    myChoice = choice(list)
    if myChoice == rightAnswer:
        newList = list.copy()
        newList.remove(myChoice)
        openDoor = choice(newList)
    else:
        newList = list.copy()
        newList.remove(myChoice)
        newList.remove(rightAnswer)
        openDoor = newList[0]
    # newList2 is the purified list given by the holder
    newList2 = list.copy()
    newList2.remove(openDoor)
    # case: Keep original choice
    myFinal = myChoice
    if myFinal == rightAnswer:
        counterKeep = counterKeep + 1
    # case: Change original choice
    else:
        counterChange = counterChange + 1
    count += 1
    if count > times:
        break

print(f"Keeping your choice means your winning probability is: {counterKeep/times: .4f}")
print(f"Changing your choice means your winning probability is: {counterChange/times: .4f}")

