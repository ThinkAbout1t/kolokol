'''Дано натуральне n, m. Отримати суму m останніх цифр числа n
(використовувати рядковий тип даних і методи по роботі з рядками забороняється).
Pakhomov Olexandr 122Б
'''
while True:
    try:
        n=int(input('n='))
        m=int(input('m='))
        summa=0
        while m!=0:
            n_last=n%10
            n//=10
            m-=1
            summa+=n_last
        print(summa)
        break
    except ValueError:
        print('input int')
