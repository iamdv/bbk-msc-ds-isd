def max_iter_counter(aList):
    my_output_list = []
    my_dist_list = list(set(aList))
    for aNum in my_dist_list:
        my_output_list.append(aList.count(aNum))
    return max(my_output_list)
