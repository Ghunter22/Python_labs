

i = 0
count_now = 1
count_alf = 0                                   #1
alf = 'abcdefghijklmnopqrstuvwxyz'
A = []
for i in range(20):
    if(i%2==0):
        A.append(alf[count_alf])
        count_alf+=1
    else:

        A.append(count_now)
        count_now += 3

print(A)


for i in range(2, 59, 3):                       #9
    if(i%5 ==0):
        print(i)



mas = [0]
i = 0
while(mas[i] >= 0):              #12
    mas.append(int(input()))
    if mas[len(mas)-1] < 0:
      print("Число меньше нуля, заверщение цикла")
    i+=1