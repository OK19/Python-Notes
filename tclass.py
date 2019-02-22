fin = open("words.txt")

'''
for i in range(10):
    line = fin.readline()
    line = line.strip()
    print(line)
'''

'''
for line in fin:
    if "e" not in line:
        print(line.strip())
'''

'''
def avoid(string, undesireables):
    for letter in undesireables:
        if letter in string:
            return True
    return Flase

b = avoid("yellow", "abcdef")
print(b)
'''

'''
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

b = is_abecedarian("abcdea")
print(b)
'''
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

for line in fin:
    print(line.strip()[::-1])
