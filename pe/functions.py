# Python module for my Project Euler functions

def ordinal(i):
    """ Returns the ordinal ending, e.g. 'st' for 1"""
    ending = { 1:"st",
               2:"nd",
               3:"rd"}
    if castNumber(i):
        i = int(float(i))
        if i%100>3 and i%100<14:
            return "th"
        return ending.get(i%10,"th")
    else:
        return ""
def sum_square_difference(numList):
    """
    Sum square difference of a list

    Calculates the difference between the square of the sum and
    the sum of the squares.
    e.g. (a+b+c)**2 - (a**2 + b**2 + c**2)
    """
    square_sum_all = sum(numList)**2
    sum_squares = 0
    for x in numList:
        sum_squares += x**2
    return square_sum_all - sum_squares
def lcm(numList):
    """
    Find lowest common multiple of number list

    numList - list of integers to use

    Will factor each number in the list,
    then find LCM using dictionaryProduct.
    """
    primeList = generatePrimes(max(numList))
    # Initialize the factor dictionary to 0:
    primeDict = dict.fromkeys(primeList,0)
    for x in numList: # will stop at maxNum
        primeDict = primeFactor(x,primeDict)
        #print(primeDict)
    return dictionaryProduct(primeDict)
def dictionaryProduct(numDict):
    """
    Find the product of dictionary: key**value

    numDict -- dictionary: {int: int, int: int ...}

    Calculates the product of all keys multiplied together.
    Each key counts value times.
    So, key1**value1 * key2**value2 * etc.
    """
    product = 1
    for x in numDict:
        product *= x ** numDict[x]
    return product
def primeFactor(num, prime_dict_original):
    """
    Factors given number using prime dictionary

    num -- number to factor (integer)
    prime_dict_original -- dictionary of prime numbers as keys.
                         The values are how many of each prime.
                         This allows comparison across mulitple runs.

    The dictionary is used because it keeps track of the factors.
    This implementation is used for function Lowest Common Multiple.
    To factor just a single number, send values as 0s.
    If num can already be made by the existing prime_dict values,
    then no changes are made.
    """
    q = num # q for quotient
    prime_dict = prime_dict_original
    # prime_dict = prime_dict_original.copy() #uncomment to preserve original
    for x in prime_dict:
        i = 0
        while q % x == 0:
            q /= x
            i += 1
        if i > prime_dict[x]:
            prime_dict[x] = i
    if q != 1:
        prime_dict[q] = 1 # add the remaining quotient to the end
                          # this is like a remainder in the event
                          # primeList was incomplete
    return prime_dict
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
def generateNPrimes(nthPrime):
    """
    Generates a list of n primes

    nthPrime -- How many primes to getnerate (integer)
    returns the list of n primes
    """
    nthPrime = int(nthPrime)
    primeList = []
    primeCandidate = 0
    if 1 <= nthPrime:
        primeList.append(2)
    else:
        return primeList
    if 2 <= nthPrime:
        primeList.append(3)
    else:
        return primeList

    while(len(primeList)<nthPrime):
        primeCandidate += 6
        if checkPrime(primeCandidate-1,primeList):
            primeList.append(primeCandidate-1)
        if checkPrime(primeCandidate+1,primeList):
            primeList.append(primeCandidate+1)

    # might have generated 1 extra prime above nthPrime
    if len(primeList) > nthPrime:
        primeList.pop(-1)
    return primeList
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
