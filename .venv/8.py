N_k = int(input())
N_s = N_k // 29
N_k_ost = N_k - N_s * 29
N_g = N_s // 17
N_s_ost = N_s - N_g * 17
if N_g != 0:
    print(N_g, "галлеонов")
if N_s_ost != 0:
    print(N_s_ost, "сиклей")
if N_k_ost != 0:
    print(N_k_ost, "кнатов")