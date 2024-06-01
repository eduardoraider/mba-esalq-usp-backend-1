euro_rate = 5.70
yen_rate = 29.98
real_value = float(input('Enter the value in R$: '))
print(f'Euro: {real_value / euro_rate:.2f} | Yen: { yen_rate * real_value:.2f}')
