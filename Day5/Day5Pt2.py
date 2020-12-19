f = open("day5text.txt", "r+")
r = f.readlines()
data = []
for i in r[:-1]:
    data.append(i[:-1])
data.append(r[-1])

seat_id = []

for seat in data:
    row1 = 0
    row2 = 128
    column1 = 0
    column2 = 8
    for direc in seat:
        if direc == 'F':
            row2 = row1 + (row2 - row1) / 2
        if direc == 'B':
            row1 = row2 - (row2 - row1) / 2
        if direc == 'R':
            column1 = column2 - (column2 - column1) / 2
        if direc == 'L':
            column2 = column1 + (column2 - column1) / 2
    seat_id.append(int(row1*8+column1))

seat_id_missing = []

for row in range(128):
    for column in range(8):
        if row*8+column not in seat_id:
            seat_id_missing.append(row*8+column)

for s in seat_id_missing:
    if (s+1 in seat_id) and (s-1 in seat_id):
        my_seat = s

print(my_seat)
