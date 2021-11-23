def check_prime(number):
    if number == 1:
        print("It is not a prime number")
        return
    
    for i in range (2, number//2):
        if(number % i == 0):
            print('Not a prime number')
            return

    print("It is a Prime Number")
        


number = 17

check_prime(number)