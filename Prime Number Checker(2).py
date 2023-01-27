def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")




    #
    # if number == 2 or number == 3 or number == 5 or number == 7:
    #     print("It's a prime number.")
    # elif number == 1 or number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
    #     print("It's not a prime number.")
    # else:
    #     print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
