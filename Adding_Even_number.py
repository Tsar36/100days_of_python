# Loop with Range:

total = 0
for number in range(2, 101, 2):
  total += number
print(total)

total2 = 0
for n in range(1, 101):
  if n % 2 == 0:
    total2 += n
print(total2)