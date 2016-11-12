my_input_value_count = int(input('Enter number of values as input:'))
S = ''

for x in range(0, my_input_value_count):
    my_input_value = str(input('Enter a left or right brackets:'))
    S = S + my_input_value

print('Your input string is: ', S)

def my_func_coursework_2_1():
    return 'Total Left Brackets: ' + str(S.count('(')) +  ' and Right Brackets: ' + str(S.count(')'))

def my_func_coursework_2_2():
    my_bracket_counter = 0
    for my_input_string_value in S:
        if(my_input_string_value == '('):
            my_bracket_counter = my_bracket_counter + 1
        elif(my_input_string_value == ')'):
            my_bracket_counter = my_bracket_counter - 1
            if(my_bracket_counter < 0):
                return 'NO, it is not math-like string'
    if(my_bracket_counter == 0):
        return 'YES, it is math-like string'
    else:
        return 'NO, it is not math-like string'

print('2.1 exercise answer is: ', my_func_coursework_2_1())
print('2.2 exercise answer is: ', my_func_coursework_2_2())
