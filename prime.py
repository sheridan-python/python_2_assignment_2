"""
This function will output the prime factors of the input, num
"""
def generate_prime_number(num):
    """Function takes an input, and has an output of the prime factors"""
    prime_factor_list = [] #initializing list
    div = 2 # number for dividing and to append to list
    if isinstance(num, int): #ifinstance checks data type is an int
        while num > 1:
            if num % div == 0:
                prime_factor_list.append(div) #if num can be divided by div (2) then append
                num //= div # you need to actually divide the num by div (2)
            else:
                div += 1
                """ at this point we know we have to divide by greater than 2, so we add 1.
                Unsure how to add by only odd numbers though so I brute force it. Involves sq rt?"""
        return prime_factor_list
    raise ValueError
