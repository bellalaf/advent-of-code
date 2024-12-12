import requests
import os

DAY = os.getenv("DAY_AOC")
COOKIE = os.getenv("COOKIE_AOC")

def get_input():
    response = requests.get(
        f"https://adventofcode.com/2024/day/{DAY}/input",
        headers={
            "cookie":COOKIE
        })
    input = response.content.decode('utf-8')
    return input.splitlines()

# used on day one
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