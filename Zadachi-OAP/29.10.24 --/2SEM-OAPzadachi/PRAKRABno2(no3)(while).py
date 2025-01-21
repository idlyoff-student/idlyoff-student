A = int(input("Введите A (A > B): "))
B = int(input("Введите B: "))

if A <= B:
    print("Ошибка: A должно быть больше B.")
else:
    occupied = 0
    while occupied + B <= A:
        occupied += B        
        free = A - occupied
        print("Длина незанятой части A:", free)
