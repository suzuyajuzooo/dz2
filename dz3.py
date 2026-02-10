def golden_ratio(i):
    a, b = 1, 1
    
    for _ in range(1, i):
        a, b = b, a + b
    
    result = b / a
    print(result)

i_value = int(input("Введите номер приближения (i): "))
golden_ratio(i_value)