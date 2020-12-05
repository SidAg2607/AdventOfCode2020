data = open("day4text.txt", "+r")
sep_data = data.readlines()
data2 = ""

for i in range(len(sep_data)):
    if i < len(sep_data)-1:
        if (sep_data[i][-1] == "\n") & (sep_data[i+1][0] != "\n"):
            data2 += ' ' + sep_data[i][:-1]
        else:
            data2 += ' ' + sep_data[i]
    else:
        data2 += sep_data[i]

data2_final = data2.split("\n")
data_final = []
for i in data2_final:
    j = i + " "
    data_final.append(j)

valid = len(data_final)

for i in data_final:
    if i.find('byr:') == -1:
        valid -= 1
    elif i.find('iyr:') == -1:
        valid -= 1
    elif i.find('eyr:') == -1:
        valid -= 1
    elif i.find('hgt:') == -1:
        valid -= 1
    elif i.find('hcl:') == -1:
        valid -= 1
    elif i.find('ecl:') == -1:
        valid -= 1
    elif i.find('pid:') == -1:
        valid -= 1

print(valid)
