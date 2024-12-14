import sys
import re
import shared

DO = "do()"
DONT = "don't()"

def handler():
    # datas = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    datas = shared.get_input()
    pattern = re.compile('do\(\)|don\'t\(\)|mul\([0-9]+,[0-9]+\)')
    lil_pattern = re.compile("[0-9]*")
    
    data_string = ""
    for data in datas:
        data_string += data
    
    uncorrupted_cmds_iter = pattern.finditer(data_string)
    total = 0
    
    allowed = True
    
    for cmd in uncorrupted_cmds_iter:
        if cmd.group() == DO:
            allowed = True
        elif cmd.group() == DONT:
            allowed = False
        elif allowed:
            nums = lil_pattern.findall(cmd.group())
            nums.sort()
            total += int(nums[-1]) * int(nums[-2])
        else:
            # skipped one
            print(f"skipped {cmd.group()}")
    
    print(total)
    # part one - 184511516
    # part two - 90044227


if __name__ == '__main__':
    globals()[sys.argv[1]]()