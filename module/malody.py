note = [
    [492, 529, 595, 681], #0dan
    [695, 621, 718, 1279],
    [1397, 1090, 805, 1212],
    [1055, 1489, 1288, 1788],
    [1865, 1434, 1284, 1839],
    [1282, 1706, 1473, 1939],
    [1694, 1636, 1803, 2115],
    [1701, 1799, 2132, 1899],
    [2237, 2081, 2280, 2000],
    [2374, 1889, 2142, 1814],
    [2034, 1740, 2270, 2166]
]

def get_acc(acc_raw, dan): # acc_list: "xxxx-xxxx-xxxx-xxxx", dan: int
    note_dan = note[dan]
    acc = []
    acc_list = acc_raw.split("-")
    for i in range(0, 4):
        acc.append(float(acc_list[i]))
    acc_1 = note_dan[0] * acc[0]
    acc_2 = (note_dan[0] + note_dan[1]) * acc[1] - acc_1
    acc_3 = (note_dan[0] + note_dan[1] + note_dan[2]) * acc[2] - (acc_1 + acc_2)
    acc_4 = (note_dan[0] + note_dan[1] + note_dan[2] + note_dan[3]) * acc[3] - (acc_1 + acc_2 + acc_3)
    return [round(acc_1 / note_dan[0], 4), round(acc_2 / note_dan[1], 4), round(acc_3 / note_dan[2], 4), round(acc_4 / note_dan[3], 4)], acc[3]

