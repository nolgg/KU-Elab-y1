order = [int(input("M: ")), int(input("N: "))]

M_Mat = [0, 0]

N_Mat = [0, 0]


M_num = order[0]

M_mat_0 = (M_Mat[0] + 2)*M_num

M_mat_1 = (M_Mat[1] + 6)*M_num

M_mat = [M_mat_0, M_mat_1]



N_num = order[1]

N_mat_0 = (N_Mat[0] + 1)*N_num

N_mat_1 = (N_Mat[1] + 4)*N_num

N_mat = [N_mat_0, N_mat_1]

sum_mat = M_mat + N_mat

print(f"{sum_mat[0]} {sum_mat[1]}")

