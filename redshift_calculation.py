def calculate_redshift(λ_emitted, λ_observed):
    z = λ_observed / λ_emitted - 1
    return z

λ_emitted = float(input("Введите излученную длину волны в метрах: "))
λ_observed = float(input("Введите наблюдаемую длину волны в метрах: "))

z = calculate_redshift(λ_emitted, λ_observed)

print(f'Красное смещение: {z}')
