"""
For all numbers between 100 and 100,000
check if prime, print Foo
check if Perfect Square, Print Bar
if Neither, Print FooBarr
"""
is_perfect = False
is_prime = True
for num in range(100, 100001):
    for n in range(2, num-1):
        if num % n == 0:
            is_prime = False
            if num == n ** 2:
                print("Bar", num)
                is_perfect = True

    if is_prime and num != 1:
        print("Foo", num)
    elif not is_perfect and not is_prime:
        print("FooBar", num)
    is_prime = True
    is_perfect = False
