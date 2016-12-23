student=['adam','john','james','alice','sarah']
module=['accounting','maths','geography','english','computers']
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
    return student_average



print('2.1: Row Average: ', my_func_avg_table_row_2_1(mark, 4))
print('2.2: Column Average: ', my_func_avg_table_column_2_2(mark, 3))
print('2.3: Student Search: ', my_func_avg_student_marks_2_3(mark, 'test'))
print('2.4: Module Search: ', my_func_avg_module_marks_2_4(mark, 'accounting'))
print('2.4: Student Report: ', my_func_student_report_2_5(mark))



