def my_func_01(aList, bList):
    for i in range(0,len(aList)):
        for j in range(0, len(bList)):
            if(bList[j] >= aList[i] + 20):
                print('YES')
                # print(bList[j], aList[i])
            else:
                print('NO')
                # print(bList[j], aList[i])
