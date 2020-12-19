#####################
def NumSpoken(iterate):
    data = [9, 6, 0, 10, 18, 2, 1]
    data_dic = {}
    for m, n in enumerate(data):
        data_dic[n] = m + 1
    i = len(data) + 1
    spoken = 0
    while i < iterate:
        data.append(spoken)
        if spoken in data_dic.keys():
            num = i - data_dic[spoken]
            data_dic[spoken] = i
            spoken = num
        else:
            data_dic[spoken] = i
            spoken = 0
        i += 1
    return spoken


print(NumSpoken(2020))
print(NumSpoken(30000000))
