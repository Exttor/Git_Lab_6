def rut2(num):
    n = str(num)
    for i in range(len(n)):
        if n[i] != '9' and n[i] != '6':
            return print("Введено неверное число, пожалуйста введите число состоящее только из чисел 6 и 9")
    n_2 = n.replace('6', '9', 1)
    return int(n_2)
