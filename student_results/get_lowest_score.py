def get_lowest_score(list):
    val = list[0]

    for i in list:
        if  i < val :
            val = i

    return val

if __name__ =="__main__" :
    print(get_lowest_score([55, 90, 73, 88]))