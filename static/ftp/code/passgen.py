from random import choice
from colorama import init
import sys

init()

crypto_type = 10000
data = []
password = ""
data.extend(list("abcdefghijklmnopqrstuvwxyz"))
data.extend(list("abcdefghijklmnopqrstuvwxyz".upper()))
data.extend(list('~!@#$%^&*()_+-=`[]\\{}|;\':"<>,./?'))
data.extend(list("0123456789"))

for num in range(0, crypto_type):
    index = range(0, crypto_type).index(num) + 1
    sys.stdout.write(f"\033[32m{round(index / crypto_type * 100, 1)}%\033[0m {index}/{crypto_type}\r")
    password += choice(data)

with open("pass.txt", "w") as file:
    file.write(password)
    sys.stdout.write("Done.                                      \r")