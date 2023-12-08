a = int(input("Необходимо ввести число: "))
b = int(input('Необходимо ввести степень: '))

fin_x = 1

for i in range(b):
    fin_x *= a
print(fin_x)
