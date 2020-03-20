
A = ("слон", "жираф", "медведь", "тигр", "лев")               # задание №4
B = ("верблюд", "аист", A)
#print(len(A)+len(B)) #A
slon,zir,medv,tirg,lion = A; #b
#print(medv)
i = 0
AS = list(A)
while i < len(AS): #A
    if (i % 2 == 0 and i !=0): # так как ноль ни четный, ни нечетный
             count = AS[i]
             AS[i] = AS[i-1]
             AS[i-1] = count

    i = i+1

j = 200
min = 0
k = 0



while k < len(AS):
    i = k
    j = 200
    min = len(AS)
    while i < len(AS):  # находим минимальный элемент и ставим его в начало массива
        if (len(AS[i]) < j):
            j = len(AS[i])
            min = i # запомнил индекс минимального элемента
        i = i + 1
   # print(min)

    count = AS[k]
    AS[k] = AS[min]
    AS[min] = count

    k+=1


print(AS)
