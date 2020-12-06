data = open("day6text.txt", "+r")
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

count = []

for group in data_string_f:
    counter = 0
    for k, l in enumerate(group):
        if 'a' <= l <= 'z':
            if l not in group[:k]:
                counter += 1
    count.append(counter)

print(count)

total_count = 0
for c in count:
    total_count += c

print(total_count)