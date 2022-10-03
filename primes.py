"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    list.append(2)
    check = True
    counter = list[0]+1
    if number_of_primes <= 0:
        raise ValueError()
    elif number_of_primes == 1:
        return list

    else:
        while len(list) < number_of_primes:
            for x in list:
                if counter % x:
                    check = True
                    continue
                else:
                    check = False
                    break
            if check:
                list.append(counter)
            counter += 2
    print(list)
    return list

primes(10)