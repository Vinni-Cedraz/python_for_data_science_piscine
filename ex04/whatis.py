import sys
"""Create a script that takes a number as argument, checks whether it is odd or
 even and prints the result. If more than one argument is provided or if the
 argument is not an integer, print an AssertionError"""
assert len(sys.argv) == 2, "more than one argument is provided"
i = sys.argv[1]
if not i.isdigit():
    raise AssertionError("argument is not an integer")
else:
    i = int(i)
    print("I'm Odd" if i % 2 else "I'm Even")
