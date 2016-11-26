def my_func_list_creator(my_input_total_elements):
	my_output_list = []
	my_input_value = 0
	for x in range(0, my_input_total_elements):
		my_input_value = int(input('Enter a integer value:'))
		my_output_list.append(my_input_value)
	return my_output_list

A = my_func_list_creator(5)
B = my_func_list_creator(6)

# A = [7, 3, 2, 6, 4]
# B = [4, 6, 7, 3, 2, 1]
# B = [3, 2, 9, 1, 11, 5]
print(A, B)

# print(set(A).intersection(B))


def my_func_set_like_containment_1_1():
	if sorted(set(A).intersection(B)) == sorted(B):
		print('YES')
	else:
		print('NO')
	return sorted(set(A).intersection(B)), sorted(B)


print(my_func_set_like_containment_1_1())


def my_func_set_like_containment_1_2():
    my_output_list = []
    my_search_list = A
    for my_b_elem in B:
        if my_b_elem in my_search_list:
            my_output_list.append(my_b_elem)
            # print(A.index(my_b_elem))
            my_search_list = my_search_list[A.index(my_b_elem):]
            # print(my_search_list)
    if my_output_list == B:
        return 'YES', my_output_list
    else:
        return 'NO', my_output_list


def my_func_consecutive_containment_1_3():
    my_aList_len = len(A)
    my_bList_len = len(B)
    for x in range(0, my_aList_len):
        try:
            if(A[x: x + my_bList_len] == B):
                return 'YES'
        except IndexError:
            return 'NO'
    return 'NO'

print(my_func_consecutive_containment_1_3())
