import math

def solve():
    q, r = map(int, input().split())
    product = q * (r - 1)
    
    divisors = set()
    i = 1
    while i <= int(math.sqrt(product)):
      if product % i == 0:
        divisors.add(i)
        divisors.add(product//i)
      i += 1
    
    print(len(divisors))

solve()