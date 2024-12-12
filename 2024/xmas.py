import shared
import sys

def handler():
    data = shared.get_input()

    (left, right) = split_input_into_two_sorted_lists(data)
    
    similarity_score = 0
    for num in left:
        similarity_score += num * right.count(num)
    
    print(similarity_score)
    # PART ONE distances = [abs(x-y) for x, y in zip(list1, list2)] ANS. 2086478


def split_input_into_two_sorted_lists(data: list[str]) -> tuple[list[int], list[int]]:
    list1 = []
    list2 = []
    
    for line in data:
        split = line.split()
        list1.append(int(split[0]))
        list2.append(int(split[1]))
        
    list1.sort()
    list2.sort()
        
    return (list1, list2)


if __name__ == '__main__':
    globals()[sys.argv[1]]()