data = open("day4text.txt", "+r")
lines = data.readlines()
data_string = ""

for i in lines:
    if i != "\n":
        if i[-1] == "\n":
            data_string += " " + i[:-1]
        else:
            data_string += " " + i
    else:
        data_string += i

data_string_f = data_string.split('\n')
data_final = []
for i in data_string_f:
    j = i + " "
    data_final.append(j)

valid_counter = 0
valid = 0

for i in data_final:
    byr = i.find("byr:")
    iyr = i.find("iyr:")
    eyr = i.find("eyr:")
    hgt = i.find("hgt:")
    hcl = i.find("hcl:")
    ecl = i.find("ecl:")
    pid = i.find("pid:")

    if byr != -1:
        if (1920 <= int(i[byr + 4:byr + 8]) <= 2002) & (i[byr + 8] == ' '):
            valid_counter += 1

    if iyr != -1:
        if (2010 <= int(i[iyr + 4:iyr + 8]) <= 2020) & (i[iyr + 8] == ' '):
            valid_counter += 1

    if eyr != -1:
        if (2020 <= int(i[eyr + 4:eyr + 8]) <= 2030) & (i[eyr + 8] == ' '):
            valid_counter += 1

    if hgt != -1:
        if i[hgt + 7:hgt + 9] == "cm":
            if (150 <= int(i[hgt + 4:hgt + 7]) <= 193) & (i[hgt + 9] == ' '):
                valid_counter += 1
        if i[hgt + 6:hgt + 8] == "in":
            if (59 <= int(i[hgt + 4:hgt + 6]) <= 76) & (i[hgt + 8] == ' '):
                valid_counter += 1

    if hcl != -1:
        if i[hcl + 4] == "#":
            hcl_data = i[hcl + 5:hcl + 11]
            hcl_num = 0
            for ch in hcl_data:
                try:
                    if 'a' <= ch <= 'f':
                        hcl_num += 1
                    elif 0 <= int(ch) <= 9:
                        hcl_num += 1
                except ValueError:
                    pass
            if (hcl_num == 6) & (i[hcl + 11] == ' '):
                valid_counter += 1

    if ecl != -1:
        if (i[ecl + 4:ecl + 7] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) & (i[ecl + 7] == ' '):
            valid_counter += 1

    if pid != -1:
        try:
            if (0 <= int(i[pid + 4:pid + 13]) <= 999999999) & (i[pid + 13] == ' '):
                valid_counter += 1
        except (ValueError, IndexError) as error:
            pass

    if valid_counter == 7:
        valid += 1
    valid_counter = 0

print(valid)
