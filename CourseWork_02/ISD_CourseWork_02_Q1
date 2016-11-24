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
