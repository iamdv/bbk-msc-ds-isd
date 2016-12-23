#Please run the program directly. There is a print statement for each function.
# Notes: Followed modular approach where one function is passed into other functions

student=['adam','john','james','alice','sarah']
module=['cs','maths','geography','english']
mark=[[90,-1,70,85],[-1,90,50,60],[40,70,-1,60],[75,80,60,70],[80,60,50,-1]]


def my_registered_marks(element):
    return element >= 0 and element <= 100


def my_func_avg_table_row_2_1(my_table, my_row_num):
    my_student_marks = my_table[my_row_num]
    my_registered_student_scores = list(filter(my_registered_marks, my_student_marks))
    return round(sum(my_registered_student_scores)/len(my_registered_student_scores),2)


def my_func_avg_table_column_2_2(my_table, my_column_num):
    my_subject_marks = []
    for my_row in my_table:
        if(my_row[my_column_num] >= 0 and my_row[my_column_num] <= 100):
            my_subject_marks.append(my_row[my_column_num])
    return round(sum(my_subject_marks)/len(my_subject_marks),2)


def my_func_avg_student_marks_2_3(my_table, my_student_name):
    try:
        my_student_index_num = student.index(my_student_name)
        return my_func_avg_table_row_2_1(my_table,my_student_index_num)
    except ValueError:
        return 'There is no such student'


def my_func_avg_module_marks_2_4(my_table, my_module_name):
    try:
        my_module_index_num = module.index(my_module_name)
        return my_func_avg_table_column_2_2(my_table,my_module_index_num)
    except ValueError:
        return 'There is no such module'


def my_func_student_report_2_5(my_table):
    student_average = []
    for each_student_name in student:
        student_average.append([each_student_name, my_func_avg_student_marks_2_3(my_table, each_student_name)])
    student_average = sorted(student_average, key=lambda x: x[1], reverse=True)
    print('\n', '2.5: Printing Student Report')
    print('\t', 'Student Name', '\t', 'Average Marks')
    for my_row in student_average:
        print('\t', my_row[0], '\t', '\t', '\t', my_row[1])
    print('\n')
    return student_average


def my_func_module_report_2_6(my_table):
    module_average = []
    for each_module_name in module:
        module_average.append([each_module_name, my_func_avg_module_marks_2_4(my_table, each_module_name)])
        module_average = sorted(module_average, key=lambda x: x[1], reverse=True)
    print('\n', '2.6: Printing Module Report')
    print('\t', 'Module Name', '\t', '\t','Average Marks')
    for my_row in module_average:
        print('\t', my_row[0], '\t', '\t', '\t', '\t', my_row[1])
    print('\n')
    return module_average


####################################################################################
print('2.1: Row Average: ', my_func_avg_table_row_2_1(mark, 4))
# First parameter table name and second parameter row number

print('2.2: Column Average: ', my_func_avg_table_column_2_2(mark, 3))
# First parameter table name and second parameter column number

print('2.3: Student Search: ', my_func_avg_student_marks_2_3(mark, 'test'))
# Correct student names: ['adam','john','james','alice','sarah']

print('2.4: Module Search: ', my_func_avg_module_marks_2_4(mark, 'accounting'))
# Correct module names: ['cs','maths','geography','english']

print('2.5: Student Report: ', my_func_student_report_2_5(mark))
# Displays student report as table (list of list) in descending order

print('2.6: Module Report: ', my_func_module_report_2_6(mark))
# Displays module report as table (list of list) in descending order
####################################################################################
