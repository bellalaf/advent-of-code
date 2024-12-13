import sys
import re

def handler():
    # data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    with open("./input/day3.txt", "r") as data_file:
        data = data_file.read()
        
        pattern = re.compile('mul\([0-9]*,[0-9]*\)')
        uncorrupted_cmds_iter = pattern.finditer(data)
        total = 0
        for cmd in uncorrupted_cmds_iter:
            lil_pattern = re.compile("[0-9]*")
            nums = lil_pattern.findall(cmd.group())
            nums.sort()
            total += int(nums[-1]) * int(nums[-2])
            
        print(total)
        # seems to be 184511516


if __name__ == '__main__':
    globals()[sys.argv[1]]()