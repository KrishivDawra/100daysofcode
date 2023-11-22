#Write a Python Program to Capitalize First Letter of Each Word in a File. 
with open('test.txt', 'r') as file:
    content = file.read()
capitalized_content = ' '.join(word.capitalize() for word in content.split())
with open('test.txt', 'w') as file:
    file.write(capitalized_content)
