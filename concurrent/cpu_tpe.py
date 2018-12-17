#!/usr/bin/env python3
import concurrent.futures                                                                                                                                  
import math                                                                                                                                                

def is_prime(n):                                                                                                                                           
    if n % 2 == 0:                                                                                                                                         
        return False                                                                                                                                       

    sqrt_n = int(math.floor(math.sqrt(n)))                                                                                                                 
    for i in range(3, sqrt_n + 1, 2):                                                                                                                      
        if n % i == 0:                                                                                                                                     
            return False                                                                                                                                   
    return True                                                                                                                                            

PRIMES = [112272535095293, 1099726899285419, 112582705942171] * 10

# computations will be done in separate threads
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:                                                                                                 
    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
        print('{:d} is prime: {}'.format(number, prime))
