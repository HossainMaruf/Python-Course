for i in range(10):
    n = int(input('Enter a positive integer number: '))

    # flag for prime or not
    isPrime = True

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            isPrime = False
            break

    if (isPrime == True):
        print("{} is prime".format(n))
    else:
        print("{} is not prime".format(n))