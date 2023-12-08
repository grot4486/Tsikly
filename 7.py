x = int(input('Необходимо ввести число: '))

sum = 0

while x > 0:
    if (x % 10) % 2 == 0:
        sum += x % 10
    x = x // 10

print(sum)
