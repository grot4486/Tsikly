a = int(input('Необходимо ввести число: '))

factorial = 1

for i in range(1, a + 1):
    factorial *= i
print(factorial)
