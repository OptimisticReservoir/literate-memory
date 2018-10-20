# Python module for my Project Euler functions

def findMaxPalindrome(digits):
    from classes import ProductPalindrome
    """
    Finds largest product that is a palindrome

    digits - max digits allowed in each factor (integer)
    Uses the idea of indecies to search for the largest
    palindrome first. It stops after the first one found.
    Not guaranteed to be the largest, but likely to be.
    """
    # TODO: Write a function to find all palindromes.
    digits = int(castNumber(digits))
    if not digits:
        digits = 3 # use 3 as default if invalid digit given.
    maxNum = int("9"*digits) # all 9s is max value
    maxIndex = 2 * maxNum # index = sum of the two numbers to be multipled.
    i = maxIndex
    x = maxNum
    y = maxNum
    solved = False
    # I'm postulating that this will find the maximum palindrome first
    # if not, I'll need to add all palindromes found to a list and then
    # find max later.
    # There could exist a situation where a particular index will give
    # two palindromes.
    # There could also exist a situation where a lower index would give
    # a larger palindrome.
    # TODO: add a more rigorous search.
    while(i > 0):
        x = maxNum
        y = i - x
        # x + y = i
        while(y <= maxNum):
            if isPalindrome(x*y):
                solved = True
                break
            x -= 1
            y += 1
        if solved:
            break
        i -= 1
    return ProductPalindrome(x,y)
def isPalindrome(s):
    """ Checks to see if passed string/number is a palindrome """
    s = str(s)
    # Old method - more memory efficient?
    #i = 0
    #while(i < len(s)/2):
    #    if s[i] != s[-(i+1)]: # 0 is first, -1 is last.
    #        return False
    #    i += 1
    #return True
    return s == s[::-1]
def generatePrimes(maxPrime):
    """
    Generates a list of primes up to a maximum value

    maxPrime -- Largest acceptable value (integer)
    returns the list of primes < maxPrime
    """
    maxPrime = int(maxPrime)
    primeList = []
    primeCandidates = []
    if 2 < maxPrime:
        primeList.append(2)
    else:
        return primeList

    if 3 < maxPrime:
        primeList.append(3)
    else:
        return primeList

    primeCandidates = list({*range(6,maxPrime+1,6)})
    primeCandidates.sort()

    for x in primeCandidates:
        if checkPrime(x-1,primeList):
            primeList.append(x-1)
        if checkPrime(x+1,primeList):
            primeList.append(x+1)
    # might have generated 1 extra prime above maxPrime

    if primeList[len(primeList)-1] > maxPrime:
        primeList.pop(-1)
    return primeList
def checkPrime(num, primes=None):
    """
    Checks number to see if it is prime

    num -- number to check (integer)
    primes -- (option) list of prime numbers ([integer])

    Accepts a number and an optional list of primes
    checks to see if number is divisible by a prime
    This will generate it's own pseudo-prime list if none provided.
    returns True if indivisible by Primes
    returns False if divisibile.
    """
    num = int(num)
    sqrtNum = int(num ** 0.5)
    if(primes is not None):
        for x in primes:
            if x > sqrtNum:
                break;
            if num % x == 0:
                return False
    else: # make our own list
        if num % 2 == 0:
            return False
        if num % 3 == 0:
            return False
        for x in {*range(6,sqrtNum+1,6)}:
            # primes besides 2 and 3 are 1 above or below multiples of 6
            # these aren't all primes, but close enough.
            if num % (x-1) == 0:
                return False
            if num % (x+1) == 0:
                return False
    return True
def LPF(num):
    """
    Gets largest prime factor

    num -- number to factor (integer)
    """
    num = int(num)
    sqrtNum = int(num ** 0.5)
    primes = generatePrimes(sqrtNum)
    largest = -1
    for x in primes:
        if num % x == 0 and x > largest:
            largest = x
    return largest
def testArgs(args):
    """ Tests an argument list and prints results. """
    print(str(len(args)) + " arguments.")
    i = 0
    x = 0
    output = 0
    while(i < len(args)):
        x = castNumber(args[i])
        output = str(x if is_floatstring(args[i]) else args[i])
        output += " " + str(type(x if is_floatstring(args[i]) else args[i]))
        print(output)
        i += 1
def castNumber(n):
    """ Casts given string as a number - int or float as required. """
    if type(n) == type(""):
        if is_intstring(n): # "5.4" gives False
            return int(n)
        elif is_floatstring(n):
            return float(n)
    elif type(n) == type(5.0) or type(n) == type(5):
        return n # no casting needed
    return None
def is_floatstring(s):
    """ Tests if string is a float. """
    try:
        float(s)
        return True
    except ValueError:
        return False
def is_intstring(s):
    """ Tests if string is an int. """
    try:
        int(s) # exception for float strings.
        return True
    except ValueError:
        return False
