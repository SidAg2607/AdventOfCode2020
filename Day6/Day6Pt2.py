# I didn't knew set() and intersection() when I wrote this

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

ff = [x[1:] for x in data_string_f]
gg = [y.split() for y in ff]

count = []

for g in gg:
    if len(g) > 1:
        counter1 = 0
        for t, o in enumerate(g[0]):
            counter2 = 0
            if o not in g[0][:t]:
                for h in g[1:]:
                    if o in h:
                        counter2 += 1
                if counter2 == (len(g) - 1):
                    counter1 += 1
        count.append(counter1)
    else:
        counter = 0
        for k, l in enumerate(g[0]):
            if l not in g[0][:k]:
                counter += 1
        count.append(counter)

total_count = 0
for c in count:
    total_count += c

print(total_count)
