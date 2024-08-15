def print_spaces(n):
    if n > 0:
        print(" ", end=" ")
        print_spaces(n - 1)

def print_stars(n):
    if n > 0:
        print("*", end=" ")
        print_stars(n - 1)

def print_stars2(n):
    if n > 0:
        print("*  ", end=" ")
        print_stars2(n - 1)

def numpat(n, i=1):
    if i <= n:
        print_stars(i)
        print("")
        numpat(n, i + 1)

def numpatR(n):
    if n > 0:
        print_stars(n)
        print("")
        numpatR(n - 1)

def pyramid(n, i=1):
    if i <= n:
        print_spaces(n - i)
        print_stars2(i)
        print("")
        pyramid(n, i + 1)

def pyramidR(n, i=1):
    if i <= n:
        print_spaces(i - 1)
        print_stars2(n - i + 1)
        print("")
        pyramidR(n, i + 1)

def numpatright(n, i=1):
    if i <= n:
        print_spaces(n - i)
        print_stars(i)
        print("")
        numpatright(n, i + 1)

def numpatandpyramid(number):
    print("Pattern 1:")
    numpat_ = numpat(number)
    print("\n" + "-"*30 + "\n")
    
    numpat_rotate = numpatR(number)
    print("\n" + "-"*30 + "\n")
    
    pyramid_ = pyramid(number)
    print("\n" + "-"*30 + "\n")
    
    pyramid_rotate = pyramidR(number)
    print("\n" + "-"*30 + "\n")
    
    numpatright_ = numpatright(number)
    print("\n" + "-"*30 + "\n")
    
    return numpat_, numpat_rotate, pyramid_, pyramid_rotate, numpatright_

number = int(input('Enter your number: '))
numpat_, numpat_rotate, pyramid_, pyramid_rotate, numpatright_ = numpatandpyramid(number)