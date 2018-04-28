#define a list of all numbers 2-1999
myrange = list(range(2,2000))
factor_count = 0
is_prime= []

#divide every number by every other number below it; if remainder = 0, it is a factor of the first
#If a number only has 2 factors (itself and 1), add it to the 'prime' list for summing
for i in myrange:
    for j in range(1,i+1):
        if i%j == 0:
            factor_count += 1
    if factor_count <= 2:
        is_prime.append(i)
    factor_count = 0

print('Sum=', sum(is_prime))
