f = open("day11text.txt", "r+")

r = [x[:-1] if x[-1] == "\n" else x for x in f.readlines()]

seats_changed = r.copy()


def adjacent(row, column):
    if row == 0:
        if column == 0:
            return seats_changed[0][1] + seats_changed[1][:2]
        elif column == len(seats_changed[0]) - 1:
            return seats_changed[0][-2] + seats_changed[1][-2:]
        else:
            return seats_changed[0][column - 1] + seats_changed[0][column + 1] + seats_changed[1][column - 1:column + 2]
    elif row == len(seats_changed) - 1:
        if column == 0:
            return seats_changed[row][1] + seats_changed[row - 1][:2]
        elif column == len(seats_changed[0]) - 1:
            return seats_changed[row][-2] + seats_changed[row - 1][-2:]
        else:
            return seats_changed[row][column - 1] + seats_changed[row][column + 1] + seats_changed[row - 1][
                                                                                     column - 1:column + 2]
    else:
        if column == 0:
            return seats_changed[row][1] + seats_changed[row - 1][:2] + seats_changed[row + 1][:2]
        elif column == len(seats_changed[0]) - 1:
            return seats_changed[row][-2] + seats_changed[row - 1][-2:] + seats_changed[row + 1][-2:]
        else:
            return seats_changed[row][column - 1] + seats_changed[row][column + 1] + seats_changed[row - 1][column - 1:column + 2] + seats_changed[row + 1][column - 1:column + 2]


NumOfAdjSeats = []

for i, j in enumerate(r.copy()):
    NumOfAdjSeats.append([])
    for k, l in enumerate(j):
        NumOfAdjSeats[i].append(len(adjacent(i, k)) - adjacent(i, k).count("."))

def change_seats():
    global seats_changed
    change = []
    for i, j in enumerate(seats_changed):
        seats = ''
        for m, n in enumerate(j):
            if n == 'L':
                if adjacent(i, m).count("L") == NumOfAdjSeats[i][m]:
                    seats += '#'
                else:
                    seats += n
            elif n == '#':
                if adjacent(i, m).count("#") >= 4:
                    seats += 'L'
                else:
                    seats += n
            else:
                seats += n
        change.append(seats)
    Same = 0
    for num, line in enumerate(change):
        if line == seats_changed[num]:
            Same += 1
    Occupied = 0
    if Same == len(change):
        for i in change:
            Occupied += i.count('#')
        return Occupied
    else:
        seats_changed = change
        return change_seats()

print(change_seats())

f.close()
