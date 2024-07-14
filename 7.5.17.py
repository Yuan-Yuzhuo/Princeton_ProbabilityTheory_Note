from secrets import choice


def generateMaxNum(lst, times):
    max_num = -10
    for i in range(times):
        selected = choice(lst)
        if selected > max_num:
            max_num = selected
    return max_num


list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4, 5, 6]

count = 0
iterations = 10000000

for i in range(iterations):
    num1 = generateMaxNum(list1, 3)
    num2 = generateMaxNum(list2, 1)
    if num1 >= num2:
        count += 1

print(f"The probability that A >= B is {count / iterations} times")
