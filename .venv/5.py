def ft_to_kg(ft):
    return ft/2.205
def dm_to_m(dm):
    return dm*2.54/100
weight_ft = float(input())
height_dm = float(input())
IMT = ft_to_kg(weight_ft)/dm_to_m(height_dm)**2
IMT_final = round(IMT, 2)
if IMT < 16:
    print("выраженный дефицит массы тела")
elif 16 <= IMT < 18.5:
    print("недостаточная масса тела")
elif 18.5 <= IMT < 25:
    print("норма")
elif 25 <= IMT < 30:
    print("избыточная масса тела")
elif 30 <= IMT < 35:
    print("ожирение первой степени")
elif 35 <= IMT < 40:
    print("ожирение второй степени")
elif 40 <= IMT:
    print("ожирение третьей степени")