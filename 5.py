N = int(input('Необходимо ввести число: '))

number = 1
prev_number = 1

for _ in range(N):
    print(number)
    number, prev_number = number + prev_number, number
    
