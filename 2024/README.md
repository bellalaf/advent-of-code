## Cookies for Santa

Each day, grab your cookie from the dev tools in Chrome and (actually when does it expire?) and set as an env var using: `export COOKIE_AOC="<input cookie here>"`

Set `DAY_AOC=<day>`

The code uses these to interactively grab the required input from aoc.com

`poetry run python xmas.py handler` to run the code


## Set up/handy commands

```
poetry env use python3.12

virtualenv venv

source venv/bin/activate

poetry install
```


Then just `poetry run` to ya heart's content.