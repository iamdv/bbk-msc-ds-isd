def my_func_02(aList):
    my_counter = 0
    for i in range(0, len(aList)):
        for j in range(0, len(aList)):
            if(aList[i] - aList[j] >= 20):
                my_counter = my_counter + 1
    if(my_counter >= 2):
        print('YES ', my_counter)
    else:
        print('NO', my_counter)
