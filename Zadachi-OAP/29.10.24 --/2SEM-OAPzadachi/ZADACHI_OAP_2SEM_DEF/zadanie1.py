def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return (a * b) // euclidean_gcd(a, b)

# Ввод чисел
A = int(input("Введите первое натуральное число A: "))
B = int(input("Введите второе натуральное число B: "))

# Вычисление НОД и НОК
nod = euclidean_gcd(A, B)
nok = calculate_lcm(A, B)

print(f"Наибольший общий делитель (НОД) чисел {A} и {B} равен: {nod}")
print(f"Наименьшее общее кратное (НОК) чисел {A} и {B} равно: {nok}")
