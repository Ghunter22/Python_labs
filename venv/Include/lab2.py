import copy

A = ['world', 1, 'she', 6, 'he', 2, 'am', 'watching', 'python', 3, 'java'] # задание №7
B = copy.copy(A)

B[1] = 20; #A
B[3] = 20;
B[7] = 20;
i = 0
while i < len(B): #A
    if i % 2 == 0 :
          B[i] = "University"
  #  print(B[i])
    i = i+1

B[3] = (1.0, 2.0 , 3.0) #B


while i < len(B): #A
    del B[i]
  #  print(B[i])
    i = i+1

D = A[len(A)-3:len(A):1]
print(D)