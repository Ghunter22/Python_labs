M = 64.063
Pc = 77.8
Tc = 430.8 # критическая
T = int(input()) + 273.5 # текущая температура



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
print(N)
print(""
      "")





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

#T = int(input()) + 273.5 # текущая температура
i = 0
temp = []
while(i < 101):
    temp.append(40+i+273.5)
    i+=1

ress = list(map(all_result,temp))
