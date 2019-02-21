"""
This function will output the prime factors of the input, num
"""
def generate_prime_number(num):
    """Function takes an input, and has an output of the prime factors"""
    prime_factor_list = [] #initializing list
    div = 2 # number for dividing and to append to list
    if isinstance(num, int): #ifinstance checks data type is an int
        while num % div == 0: # to get prime, divide by two until a number with decimal is returned
            prime_factor_list.append(div) # appending prime factor to list'
            break
        return prime_factor_list
    raise ValueError
