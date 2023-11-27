standard_input = ["3 2", 
                  "1 2", 
                  '2 3']

main_list = list(map(int, input().split()))

one_students = []
two_students = []

for _ in range(main_list[1]):
    temp_list = list(map(int, input().split()))
    one_students.append(temp_list[0])
    two_students.append(temp_list[1])

state = "YES"

for one_student, two_student in zip(one_students, two_students):
    if one_students.count(one_student) > 1:
        state = "NO"
    if two_students.count(two_student) > 1:
        state = "NO"

print(state)