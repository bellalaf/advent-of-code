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

