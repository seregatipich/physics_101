import math


def calculate_deflection_angle(b):
    G = 6.67430 * 10**-11  # м^3 кг^-1 с^-2
    M = 5.972 * 10**24  # кг
    c = 3.0 * 10**8  # м/с
    Δθ = 4 * G * M / (c**2 * b)
    return Δθ  # радианы


b = float(input("Введите расстояние от светового луча до Земли в метрах: "))
angle = calculate_deflection_angle(b)

# радианы в градусы
angle_degrees = math.degrees(angle)

print(f'Угол отклонения: {angle_degrees} градусов')
