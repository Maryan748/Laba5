def create_table(N, M):
    table = []
    count = 1
    for i in range(N):
        row = []
        for j in range(M):
            row.append(count)
            count += 1
        table.append(row)
    return table

N = 3
M = 4
table = create_table(N, M)
for row in table:
    print(row)
