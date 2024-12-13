import shared
import sys

# ffs, i should definitely be using pandas... anyways

def handler():
    # data = shared.get_input()
    # data = ['7 6 4 2 1','1 2 7 8 9','9 7 6 2 1','1 3 2 4 5','8 6 4 4 1','1 3 6 7 9']
    data = ['48 46 47 49 51 54 56']
        # '1 1 2 3 4 5',
        # '1 2 3 4 5 5',
        # '5 1 2 3 4 5',
        # '1 4 3 2 1',
        # '1 6 7 8 9',
        # '1 2 3 4 3',
        # '9 8 7 6 7',
        # '7 10 8 10 11',
        # '29 28 27 25 26 25 22 20']
    safe_reports = 0

    for line in data:
        report = [int(num) for num in line.split()]
        if is_report_safe(report, True):
            print("SAFE")
            safe_reports += 1
        print("----")

    print(safe_reports)


def is_report_safe(report: list[int], problem_dampner_available: bool) -> bool:
    for i in range(len(report) - 2):
        if i==0:
            initial_direction = get_direction(report[1] - report[0])

        if not is_num_diff_safe(report[i+1], report[i], initial_direction):
            if problem_dampner_available:
                # try without this element
                if is_report_safe(report[:i] + report[i+1:], False):
                    problem_dampner_available = False
                    report = report[:i] + report[i+1:]
                    continue
                # try without the first element (change direction)
                if is_report_safe(report[1:], False):
                    print("This worked")
                    problem_dampner_available = False
                    report = report[1:]
                    continue
                # try without the last element
                if is_report_safe(report[:-1], False):
                    problem_dampner_available = False
                    report = report[:-1]
                    continue
            else:
                print(f"Actually failing. nums (in order): {report[i+1]}, {report[i]}. Dir = {initial_direction}")
            # defs something wrong
            print("UNSAFE:")
            print(report)
            return False
    return True

def is_num_diff_safe(next_num, num, initial_direction) -> bool:
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