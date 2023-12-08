x = int(input('Необходимо ввести число: '))

sum = 0
multi = 1

while x > 0:
    sum += x % 10
    multi *= x % 10
    x = x // 10
print(f'Сумма - {sum}')
print(f'Произведение - {multi}')
