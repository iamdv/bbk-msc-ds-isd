# Please run/execute this file. All relevant print() commands are already in place.

A = []
def my_func_list_creator(my_input_total_elements):
    my_input_value = ''
    for x in range(0, my_input_total_elements):
        my_input_value = int(input('Enter a integer value:'))
        A.append(my_input_value)
    return A

my_input_value_count = int(input('Enter number of values as input: '))
print('Your input list is: ', my_func_list_creator(my_input_value_count))


def my_func_coursework_1_1():
    my_list = list(set(A))
    my_list = sorted(i for i in my_list if i >= 1)
    if(my_list[0:3] == [1,2,3]):
        return 'YES'
    else:
        return 'NO'


def my_func_coursework_1_2():
    my_output_list = []
    for x in A:
        if(x == 1 and my_output_list == []):
            my_output_list.append(1)
        if(x == 2 and my_output_list == [1]):
            my_output_list.append(2)
        if(x == 3 and my_output_list == [1, 2]):
            my_output_list.append(3)

    if(my_output_list == [1, 2, 3]):
        return 'YES'
    else:
        return 'NO'


def my_func_coursework_1_3():
    my_output_list = []
    my_list_len = len(A)
    for x in range(0, my_list_len):
        try:
            if([A[x], A[x+1], A[x+2]] == [1,2,3]):
                return 'YES'
        except IndexError:
            return 'NO'
    return 'NO'


print('1.1 exercise answer is: ', my_func_coursework_1_1())
print('1.2 exercise answer is: ', my_func_coursework_1_2())
print('1.3 exercise answer is: ', my_func_coursework_1_3())
