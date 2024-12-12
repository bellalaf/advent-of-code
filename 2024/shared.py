import requests
import os

COOKIE = os.getenv("COOKIE_AOC")

def get_input(day: int):
    response = requests.get(
        f"https://adventofcode.com/2024/day/{day}/input",
        headers={
            "cookie":COOKIE
        })
    input = response.content.decode('utf-8')
    return input.splitlines()

