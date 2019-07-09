 #!/usr/bin/python3
import argparse
import itertools

parser = argparse.ArgumentParser()
parser.add_argument("max_length", help="Maximum length of password you want", type=int)
parser.add_argument("init_str", help="initial string of each password", type=str)
parser.add_argument("--vervose", help="specify if want details of passwords")
parser.add_argument("--interval", help="interval between passwords, need in vervose mode", type=int)
args = parser.parse_args()

name = args.init_str  # This should have minimum value 3
if len(name) < 3:
    print("file created is so big, Try again with big string.")
    exit(code=7)
password_file = name + "_password.txt"
number_of_passwords = 0
f = open(password_file, "w")
max_digit_length = args.max_length - len(name)
digit_length = 1
digit_string = ""
while digit_length <= max_digit_length:
    per_obj = itertools.product(range(10), repeat=digit_length)
    for i in per_obj:
        for digit in i:
            digit_string = digit_string + str(digit)
        s = name + digit_string + "\n"
        f.write(s)
        number_of_passwords += 1
        if number_of_passwords % args.interval == 0:
            if args.vervose:
                print(s, end="")
        digit_string = ""
    digit_length += 1

print("Password file of name ", password_file, " is created.")
print("It contains", number_of_passwords, " passwords")
f.close()
