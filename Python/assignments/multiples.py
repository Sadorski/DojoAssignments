for i in range(1000):
  if i % 2 == 1:
    print(i)

for i in range(10000001):
    if i % 5 == 0:
        print(i)

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(len(a)):
    sum += a[i]
print sum

average = 0
for i in range(len(a)):
    average += a[i]
average = average / len(a)
print(average)
