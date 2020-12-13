f = open("day11text.txt", "r+")

r = [x[:-1] if x[-1] == "\n" else x for x in f.readlines()]

seats_changed = r.copy()


def Dir8s(direc, ro, col):
    try:
        if direc == 1:
            if ro - 1 >= 0:
                if seats_changed[ro - 1][col] != '.':
                    return seats_changed[ro - 1][col]
                else:
                    return Dir8s(1, ro - 1, col)
            else:
                return '.'
        elif direc == 2:
            if ro - 1 >= 0:
                if seats_changed[ro - 1][col + 1] != '.':
                    return seats_changed[ro - 1][col + 1]
                else:
                    return Dir8s(2, ro - 1, col + 1)
            else:
                return '.'
        elif direc == 3:
            if seats_changed[ro][col + 1] != '.':
                return seats_changed[ro][col + 1]
            else:
                return Dir8s(3, ro, col + 1)
        elif direc == 4:
            if seats_changed[ro + 1][col + 1] != '.':
                return seats_changed[ro + 1][col + 1]
            else:
                return Dir8s(4, ro + 1, col + 1)
        elif direc == 5:
            if seats_changed[ro + 1][col] != '.':
                return seats_changed[ro + 1][col]
            else:
                return Dir8s(5, ro + 1, col)
        elif direc == 6:
            if col - 1 >= 0:
                if seats_changed[ro + 1][col - 1] != '.':
                    return seats_changed[ro + 1][col - 1]
                else:
                    return Dir8s(6, ro + 1, col - 1)
            else:
                return '.'
        elif direc == 7:
            if col - 1 >= 0:
                if seats_changed[ro][col - 1] != '.':
                    return seats_changed[ro][col - 1]
                else:
                    return Dir8s(7, ro, col - 1)
            else:
                return '.'
        else:
            if (ro - 1 >= 0) & (col - 1 >= 0):
                if seats_changed[ro - 1][col - 1] != '.':
                    return seats_changed[ro - 1][col - 1]
                else:
                    return Dir8s(8, ro - 1, col - 1)
            else:
                return '.'
    except IndexError:
        return '.'


def adjacent(row, column):
    if row == 0:
        if column == 0:
            return Dir8s(3, row, column) + Dir8s(4, row, column) + Dir8s(5, row, column)
        elif column == len(seats_changed[0]) - 1:
            return Dir8s(5, row, column) + Dir8s(6, row, column) + Dir8s(7, row, column)
        else:
            return Dir8s(3, row, column) + Dir8s(4, row, column) + Dir8s(5, row, column) + Dir8s(6, row, column) + Dir8s(7, row, column)
    elif row == len(seats_changed) - 1:
        if column == 0:
            return Dir8s(1, row, column) + Dir8s(2, row, column) + Dir8s(3, row, column)
        elif column == len(seats_changed[0]) - 1:
            return Dir8s(1, row, column) + Dir8s(7, row, column) + Dir8s(8, row, column)
        else:
            return Dir8s(1, row, column) + Dir8s(2, row, column) + Dir8s(3, row, column) + Dir8s(7, row, column) + Dir8s(8, row, column)
    else:
        if column == 0:
            return Dir8s(1, row, column) + Dir8s(2, row, column) + Dir8s(3, row, column) + Dir8s(4, row, column) + Dir8s(5, row, column)
        elif column == len(seats_changed[0]) - 1:
            return Dir8s(1, row, column) + Dir8s(5, row, column) + Dir8s(6, row, column) + Dir8s(7, row, column) + Dir8s(8, row, column)
        else:
            return Dir8s(1, row, column) + Dir8s(2, row, column) + Dir8s(3, row, column) + Dir8s(4, row, column) + Dir8s(5, row, column) + Dir8s(6, row, column) + Dir8s(7, row, column) + Dir8s(8, row, column)


NumOfAdjSeats = []

for i, j in enumerate(r.copy()):
    NumOfAdjSeats.append([])
    for k, l in enumerate(j):
        NumOfAdjSeats[i].append(len(adjacent(i, k)) - adjacent(i, k).count("."))


def change_seats():
    global seats_changed
    change = []
    for i1, j1 in enumerate(seats_changed):
        seats = ''
        for m, n in enumerate(j1):
            if n == 'L':
                if adjacent(i1, m).count("L") == NumOfAdjSeats[i1][m]:
                    seats += '#'
                else:
                    seats += n
            elif n == '#':
                if adjacent(i1, m).count("#") >= 5:
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
        for i1 in change:
            Occupied += i1.count('#')
        return Occupied
    else:
        seats_changed = change
        return change_seats()


print(change_seats())

f.close()
