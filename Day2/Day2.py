text = open("day2text.txt", "r+")
lines = text.readlines()
length = []
letter = []
string = []

for i in lines:
    j = i.split(" ")
    length.append(j[0])
    letter.append(j[1][0])
    string.append(j[2])

part1 = 0
part2 = 0

for num in range(len(letter)):
    lent = length[num].split("-")
    lent1 = int(lent[0])
    lent2 = int(lent[1])

    if lent1 <= string[num].count(letter[num]) <= lent2:
        part1 += 1

    string1 = string[num]
    if (str(string1[lent1 - 1]) == str(letter[num])) + (str(string1[lent2 - 1]) == str(letter[num])) == 1:
        part2 += 1

print(part1)
print(part2)
