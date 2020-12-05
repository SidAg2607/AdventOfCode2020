num = open("day1text.txt", 'r+')
numb_string = num.readlines()
numbers = [int(x[:-1]) for x in numb_string]

for i, i1 in enumerate(numbers):
    for j, j1 in enumerate(numbers[i+1:]):
        for k, k1 in enumerate(numbers[j+1:]):
            if i1 + j1 + k1 == 2020:
                answer = (i1 * j1 * k1)

print(answer)
