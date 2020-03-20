M = 64.063
Pc = 77.8
Tc = 430.8 # критическая                                 # 5-ая лабораторная

print("Введите значение температуры")
def is_digit(string): # проверка, что ввел пользователь
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
str_t = input()
if is_digit(str_t):
    T = float(str_t) + 273.5 # текущая температура
else:
    print("Введите числовое значение")
    raise SystemExit


def TZC(M, Pc, Tc):
    Teta_zv_c = (3.5 * (M**(1/2))*(Pc**(2/3)))/(Tc**(1/6))
    return Teta_zv_c


def Tr(T, Tc):
    tr = T/Tc
    return tr

def Nf(tzc, tr):
    if(tr > 1):
      a = tzc*(tr**(0.71+(0.29/tr)))
      return a
    if (tr < 1):
     b = tzc*(tr**(0.965))
     return b

tr = Tr(T,Tc) # безразмерная температура
tzc = TZC(M,Pc,Tc) # вязкость  при крит температуре
N = Nf(tzc,tr)# финальная фязкость
print(N) # результат расчета на основе введеных данных пользователя
print('\n')





TZC_1 = lambda M, Pc,Tc:(3.5 * (M**(1/2))*(Pc**(2/3)))/(Tc**(1/6))
Tr_1 = lambda T,Tc: T/Tc
Nf_1 =  lambda tzc, tr: tzc*(tr**(0.71+(0.29/tr)))
Nf_2 =  lambda tzc, tr: tzc*(tr**(0.965))


def all_result(T):
    tr = Tr_1(T, Tc)
    tzc = TZC_1(M, Pc, Tc)  # вязкость  при крит температуре
    if (tr > 1):
        N = Nf_1(tzc, tr)  # финальная фязкость
    if (tr <= 1):
        N = Nf_2(tzc, tr)  # финальная фязкость
    print(N)
    f.write(str(T) + '\n') # записываю в файл данные температуры
    res.write(str(N)+ '\n')  # записываю в файл результаты

#T = int(input()) + 273.5 # текущая температура
f = open('temp.txt','w')
res = open('res.txt','w')
i = 0
temp = []
while(i < 101):
    temp.append(40+i+273.5)
    i+=1

ress = list(map(all_result,temp))
f.close()


print('НОВЫЙ РАСЧЕТ ' + '\n'+ '\n'+ '\n')
#                                                      ЛАБОРАТОРНАЯ 6
#берем данные из файла
all_temp = []
f = open('temp.txt')
for line in f:
    all_temp.append(float(line))
f.close()
f = open('temp.txt','w') # тут хранится исходная температура
res = open('res.txt','w') # тут хранятся результаты
# передаю данные считанные из файла
ress2 = list(map(all_result,all_temp))
print("DONE")