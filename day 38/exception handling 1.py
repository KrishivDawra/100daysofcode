#Write a Python Program to Print the Contents of File in Reverse Order
with open('test.txt', 'r') as file:
    content = file.read()
lines = content.splitlines()
for line in reversed(lines):
    print(line)
