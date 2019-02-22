myList = ("apples", "oranges", "Pears", "Bears", "Oh My")

def printLength(list):
    print(len(list))

def table():
    print("number", "square", "cube", sep='\t')
    print(3, 3**2, 3**3, sep='\t')
    print(9, 9**2, 9**3, sep='\t')
    print(18, 18**2, 18**3, sep='\t')


if __name__ == '__main__':
    table()
