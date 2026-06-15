# SORT DICTIONARY BY VALUES
student_marks = {
    'john': 85,
    'alice':76,
    'ayush': 98
}

sorted_dict = dict(sorted(student_marks.items(), key=lambda x: x[1]))
print(sorted_dict)

