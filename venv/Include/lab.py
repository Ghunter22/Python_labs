list1 = ['world', 'programmer', 'she', 'I', 'he', 'is', 'am', 'watching', 'python', 'c++', 'java', 'popular', 'most', 'group', 'university', 'my', 'like', 'studying']
str1 = list1[3]+" "+list1[6]+" " + list1[1]
print(str1)

str1 = list1[1]+" "+list1[9]+" " + list1[2]
print(str1)

str1 = list1[4]+" "+list1[3]+" " + list1[5]
print(str1)

str1 = list1[0]+" "+list1[5]+" " + list1[9]
print(str1)

str1 = list1[6]+" "+list1[0]+" " + list1[1]
print(str1)
#//////////////////////////////////////////////////
i = 0
stroka = ""
while i < len(list1):
    stroka = list1[i][0].upper() + list1[i][1:len(list1[i])]
    print(stroka)
    i = i+1


    #/////////////////////////////////////////
    i=0
    list2 =list1
    while i < len(list1):
         list2[i] = list1[i][0:len(list1[i])-1]+"!"
         print(list2[i])
         i= i+1