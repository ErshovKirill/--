def change(A,x,y):
    A[x-1],A[y-1] = A[x-1],A[y-1]
    return A
M =[[4,7,2,9],
    [2,5,8,4],
    [0,1,7,3]]
print('Матрица:')
for k in M:
    print(k)
i = int(input('Введите номер строки:'))
j = int(input('С какой строкой поменять:'))
M = change(M,i,j)
print('Результат:')
for k in M:
    print(k)