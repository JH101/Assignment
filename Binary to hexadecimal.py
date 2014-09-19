#Jamie Hilton
#18/09/14
# Denary-Hexadecimal converter

denary = int(input("Please enter a denary number"))

binary_string = ""

while denary > 0:
             binary_string = str(denary%2)+binary_string
             denary = denary//2

print("The binary equivalent is {0}".format(binary_string))

binary_string_a = binary_string[0:4]

print(binary_string_a)

if denary > 15:

    binary_string_b = binary_string[3:8]

    print(binary_string_b)

    if binary_string_b == "1111":
    hex_string_b="F"

    if binary_string_b == "0111":
    hex_string_b="E"

    if binary_string_b == "1011":
    hex_string_b="D"

    if binary_string_b == "0011":
    hex_string_b="C"

    if binary_string_b == "1101":
    hex_string_b="B"

    if binary_string_b == "0101":
    hex_string_b="A"

    if binary_string_b == "1001":
    hex_string_b="9"

    if binary_string_b == "0001":
    hex_string_b="8"

    if binary_string_b == "1110":
    hex_string_b="7"

    if binary_string_b == "0110":
    hex_string_b="6"

    if binary_string_b == "1010":
    hex_string_b="5"

    if binary_string_b == "0010":
    hex_string_b="4"

    if binary_string_b == "1100":
    hex_string_b="3"

    if binary_string_b == "0100":
    hex_string_b="2"

    if binary_string_b == "1000":
    hex_string_b="1"

    if binary_string_b == "0000":
    hex_string_b ="0"

print(hex_string_a+hex_string_b)


if binary_string_a == "1111":
    hex_string_a="F"

if binary_string_a == "0111":
    hex_string_a="E"

if binary_string_a == "1011":
    hex_string_a="D"

if binary_string_a == "0011":
    hex_string_a="C"

if binary_string_a == "1101":
    hex_string_a="B"

if binary_string_a == "0101":
    hex_string_a="A"

if binary_string_a == "1001":
    hex_string_a="9"

if binary_string_a == "0001":
    hex_string_a="8"

if binary_string_a == "1110":
    hex_string_a="7"

if binary_string_a == "0110":
    hex_string_a="6"

if binary_string_a == "1010":
    hex_string_a="5"

if binary_string_a == "0010":
    hex_string_a="4"

if binary_string_a == "1100":
    hex_string_a="3"

if binary_string_a == "0100":
    hex_string_a="2"

if binary_string_a == "1000":
    hex_string_a="1"

if binary_string_a == "0000":
    hex_string_a="0"

print(hex_string_a)


