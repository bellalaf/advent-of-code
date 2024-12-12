import shared
import sys

def handler():
    data = shared.get_input()
    # data = ['7 6 4 2 1','1 2 7 8 9','9 7 6 2 1','1 3 2 4 5','8 6 4 4 1','1 3 6 7 9']

    safe_reports = 0
    for line in data:
        
        # prep
        report = [int(num) for num in line.split()]
        safe = True
        
        for i in range(len(report) - 1):
            if i==0:
                initial_direction = get_direction(report[1] - report[0])
    
            if not is_safe(report[i+1], report[i], initial_direction):
                safe = False
                break

        if safe:
            safe_reports += 1
            

    print(safe_reports)
    # PART ONE distances = [abs(x-y) for x, y in zip(list1, list2)] ANS. 2086478
    # PART TWO similarity_score_list = [num * right.count(num) for num in left] ANS. 24941624


def is_safe(next_num, num, initial_direction) -> bool:
    level_diff = next_num - num
    if abs(level_diff) == 0 or abs(level_diff) > 3 or get_direction(level_diff) != initial_direction:
        return False
    return True
    

def get_direction(level_diff) -> int:
    if level_diff > 0:
        return 1
    elif level_diff == 0:
        return 0
    return -1

if __name__ == '__main__':
    globals()[sys.argv[1]]()