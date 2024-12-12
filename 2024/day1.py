import shared

data = shared.get_input(1)

list1 = []
list2 = []

for line in data:
    split = line.split()
    list1.append(int(split[0]))
    list2.append(int(split[1]))

list1.sort()
list2.sort()

distances = [abs(x-y) for x, y in zip(list1, list2)]
print(sum(distances))
# 2086478 - correct yay
