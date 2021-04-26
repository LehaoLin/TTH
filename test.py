abc_dict = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

def TTH(aaa):
    print('-----------------------------------')
    print('Before TTH:', aaa)
    result = ''
    aaa = aaa.replace(' ', '')
    input_list = []
    for i in aaa:
        input_list.append(abc_dict[i])

    trans_temp = [0,0,0,0]

    step = 16
    result = []
    uu = 0
    while uu < len(input_list):
        temp = input_list[uu:(uu+step)]
        
        temp_1 = []
        step_1 = 4
        ii = 0
        while ii < len(temp):
            sht = temp[ii] + temp[ii+1] + temp[ii+2] + temp[ii+3] + trans_temp[ii//4]
            sht = sht % 26
            temp_1.append(sht)
            ii += step_1
            
        new_matrix = []
        new_matrix.append(temp[4])
        new_matrix.append(temp[9])
        new_matrix.append(temp[14])
        new_matrix.append(temp[15])
        new_matrix.append(temp[8])
        new_matrix.append(temp[13])
        new_matrix.append(temp[2])
        new_matrix.append(temp[11])
        new_matrix.append(temp[12])
        new_matrix.append(temp[1])
        new_matrix.append(temp[6])
        new_matrix.append(temp[7])
        new_matrix.append(temp[0])
        new_matrix.append(temp[5])
        new_matrix.append(temp[10])
        new_matrix.append(temp[3])

        temp_2 = []
        ii = 0
        while ii < len(new_matrix):
            sht = new_matrix[ii] + new_matrix[ii+1] + new_matrix[ii+2] + new_matrix[ii+3] + temp_1[ii//4]
            sht = sht % 26
            temp_2.append(sht)
            ii += step_1

        trans_temp = temp_2
        uu += step

    result_abc = ''
    for i in temp_2:
        xx = list(filter(lambda k: abc_dict[k] == i, abc_dict))
        result_abc += xx[0]

    print('After TTH:', result_abc)
    return result_abc


TTH('ABCDEFGHIJKLMNOP')
TTH('ALICE THINKS THE ASSIGNMENT IS VERY EASY FOR OUR STUDENTS')