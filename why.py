def trichotomy(n):
    '''
    Descripition:States whether an integer is positive negative or zero.

    Parameters:
    n - int, float; the number to be checked

    Return values: None
    '''
    if n > 0:
        print(n, "is positive")
    elif n < 0:
        print(n, "is negative")
    else:
        print(n, "is zero")

def checkSingleDigit(n):
    '''
    Description: check to see if n is a single digit integer.

    Parameter n - int; the integer to be checked

    Return Values: None
    '''
if n < 10 and n > -10:
    print(n, "is a single digit number")
if __name__ == '__main__':
    string = input ("Enter a number: ")
    string = int(string)
    checkSingleDigit(int(string))
