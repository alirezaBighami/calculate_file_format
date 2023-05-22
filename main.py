import os


def explore(ttype, address):
    all_flies = list(os.walk(address))
    ans_dict = {}
    for i in range(all_flies.__len__()):
        for j in range(all_flies[i][2].__len__()):
            if ('.' + ttype.lower()) in all_flies[i][2][j].lower():
                if not ans_dict.get(all_flies[i][0]):
                    ans_dict[all_flies[i][0]] = 1
                else:
                    ans_dict[all_flies[i][0]] += 1
    return ans_dict
