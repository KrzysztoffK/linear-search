#linear search
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return "Target not in the list"
print(linear_search(["A", "B", "C", "D", "E", "F", "G"], "E"))

#sentinel linear search
def sentinel_linear_search(list, target):
    list[-1] = target
    i = 0
    while(list[i] != target):
        i = i + 1
    else:
        return i
print(sentinel_linear_search(["A", "B", "C", "D", "E", "F", "G"], "E"))