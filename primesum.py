myrange = list(range(2,2001))
divisorrange = list(range(1,2001))
factor_count = 0
is_prime= []

for i in myrange:
    for j in divisorrange:
        if i%j == 0:
            factor_count += 1
    if factor_count <= 2:
        is_prime.append(i)
    factor_count = 0

print(is_prime)
print(sum(is_prime))