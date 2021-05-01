a = input('Введите предложение: ')

print(a[:int(len(a)/2)].lower()+a[int(len(a)/2):].upper())