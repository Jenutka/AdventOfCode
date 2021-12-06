import collections

def main():
    list_of_bingos=[85,84,30,15,46,71,64,45,13,90,63,89,62,25,87,68,73,47,65,78,2,27,67,95,88,99,96,17,42,31,91,98,57,28,38,93,43,0,55,49,22,24,82,54,59,52,3,26,9,32,4,48,39,50,80,21,5,1,23,10,58,34,12,35,74,8,6,79,40,76,86,69,81,61,14,92,97,19,7,51,33,11,77,75,20,70,29,36,60,18,56,37,72,41,94,44,83,66,16,53]
    rows = get_rows()
    matrixes = get_matrixes(rows)
    r_dict = test_matrixes_rows(matrixes)
    c_dict = test_matrixes_columns(matrixes)
    sum_dict = sum_matrixes(matrixes)
    win_dict = collections.defaultdict(int)
    for number in list_of_bingos:
        m=0
        for mat in matrixes:
            mat_name = "matice_"+str(m)
            r_key = "r_"+str(m)
            c_key = "c_"+str(m)
            sum_key = "s_"+str(m)
            process_mat(matrixes, mat, number, mat_name, r_dict, r_key, c_dict, c_key, sum_dict, sum_key, win_dict)
            m+=1
    print("konec_programu")

def process_mat(matrixes, mat, number, mat_name, r_dict, r_key, c_dict, c_key, sum_dict, sum_key, win_dict):
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            value=mat[i][j]
            if number == value:
                r_dict[r_key][i]+=1
                c_dict[c_key][j]+=1
                sum_dict[sum_key]-=value
                if r_dict[r_key][i]==5:
                    win_dict[mat_name]+=1
                    if len(win_dict)==len(matrixes):
                        print(f"poslední výhra: matice: {mat_name},  s hodnotou {value}, součet zb. čísel {sum_dict[sum_key]}, final score = {sum_dict[sum_key]*value}")
                    print(f"nalezena rada v matici {mat_name}, na rade {i}, s hodnotou {value}, součet zb. čísel {sum_dict[sum_key]}, final score = {sum_dict[sum_key]*value}")
                if c_dict[c_key][j]==5:
                    win_dict[mat_name]+=1
                    if len(win_dict)==len(matrixes):
                        print(f"poslední výhra: matice: {mat_name},  s hodnotou {value}, součet zb. čísel {sum_dict[sum_key]}, final score = {sum_dict[sum_key]*value}")
                    print(f"nalezen sloupec v matici {mat_name}, ve sloupci {j}, s hodnotou {value}, součet zb. čísel {sum_dict[sum_key]}, final score = {sum_dict[sum_key]*value}")

def get_rows():
    rows=[]
    for line in open('input_matrixes').readlines():
        if len(line) > 4:
            row = [int(x) for x in line.split()]
            rows.append(row)
        else: continue
    return rows

def get_matrixes(rows):
    matrixes=[]
    for i in range(0, len(rows), 5):
        matrixes.append(rows[i:i + 5])
    return matrixes

def test_matrixes_rows(matrixes):
    r_list = []
    for mat_num in range(len(matrixes)):
        r_list.append("r_" + str(int(mat_num)))
    r_dict = {}.fromkeys(r_list)
    for key in r_dict.keys():
        r_dict[key] = [0, 0, 0, 0, 0]
    return r_dict

def test_matrixes_columns(matrixes):
    c_list = []
    for mat_num in range(len(matrixes)):
        c_list.append("c_" + str(int(mat_num)))
    c_dict = {}.fromkeys(c_list)
    for key in c_dict.keys():
        c_dict[key] = [0, 0, 0, 0, 0]
    return c_dict

def sum_matrixes(matrixes):
    sum_list = []
    for mat_num in range(len(matrixes)):
        sum_list.append("s_" + str(int(mat_num)))
    sum_dict = {}.fromkeys(sum_list, int())
    s=0
    for mat_val in matrixes:
        sum_key = "s_" + str(s)
        s+=1
        for k in range(len(mat_val[0])):
            for l in range(len(mat_val)):
                value = mat_val[k][l]
                sum_dict[sum_key]+=value
    return sum_dict

main()