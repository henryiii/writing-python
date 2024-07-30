Modify `choose.py` to choose one of a list that the user provides on the command line.

Optionally try to mimic this new `python3.13 -m random` interface:

```
usage: random.py [-h] [-c CHOICE [CHOICE ...] | -i N | -f N] [input ...]

positional arguments:
  input                 if no options given, output depends on the input
                            string or multiple: same as --choice
                            integer: same as --integer
                            float: same as --float

options:
  -h, --help            show this help message and exit
  -c, --choice CHOICE [CHOICE ...]
                        print a random choice
  -i, --integer N       print a random integer between 1 and N inclusive
  -f, --float N         print a random floating point number between 1 and N inclusive
```
