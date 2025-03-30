#Part1
#XMAS, horizontal, vertical, diagonal, cros_diag
with open('Day4_input.txt', 'r') as file:
    table = [ list(i) for i in file.readlines()]#140*140 with \n 

for i in table:
    if i[-1] == '\n':
        i.pop(-1)

def get_diagonals(mat):
    diagonals = []
    n = len(table)
    for offset in range(-n + 1, n):
        diagonal = []
        for i in range(n):
            j = i + offset 
            if 0 <= j < n:
                diagonal.append(mat[i][j])
        diagonals.append(diagonal)
    return diagonals

def get_cros_diagonals(mat):
    cr_diagonals = []
    n = len(table)
    for offset in range(-n + 1, n):
        cr_diagonal = []
        for i in range(n):
            j = n - 1 - i + offset 
            if 0 <= j < n:
                cr_diagonal.append(mat[i][j])
        cr_diagonals.append(cr_diagonal)
    return cr_diagonals


def count_xmas(s:str): 
    return s.count("XMAS")+s[::-1].count("XMAS")

Hrzs = ["".join(i) for i in table]
Vrts = ["".join([ j[i] for j in table  ]) for i in range(0,len(table[0]))]
dgns = ["".join(i) for i in get_diagonals(table)]
crds = ["".join(i) for i in get_cros_diagonals(table)]

count_all = sum([count_xmas(i)for i in Hrzs]) + \
            sum([count_xmas(i)for i in Vrts]) + \
            sum([count_xmas(i)for i in dgns]) + \
            sum([count_xmas(i)for i in crds]) 
print(count_all) #2557

#Part2
##lu-ru-ld-rd:SSMM,SMSM,SMMS,MMSS,MSMS,MSSM
X_MASs = ["SSMM","SMSM"]
def is_X_MAS(l:list):
    corns = "".join([l[0][0],l[2][0],l[0][2],l[2][2]])
    return any(case in corns for case in X_MASs) or any(case in corns[::-1] for case in X_MASs)

cand_MASs = []
for i in range(1,len(table)-1):
    for j in range(1,len(table[0])-1):
        if table[i][j] == "A":
            cand_MASs.append([ table[row][j-1:j+2]for row in range(i-1,i+2)])

print(sum([ is_X_MAS(i) for i in cand_MASs]))
