import Imports.grade_average_service as grade_service

homework_assignment_grades = {
    'homework_1': 85,
    'homework_2': 100,
    'homework_3': 81
}

# def calculate_homework(homework_assignment_arg):
#     sum_of_grade = 0
#     for homework in homework_assignment_arg.values():
#         sum_of_grade += homework
#     final_grade = round(sum_of_grade / len(homework_assignment_arg), 2)
#     print(final_grade)

# calculate_homework(homework_assignment_grades)

grade_service.calculate_homework(homework_assignment_grades)


















