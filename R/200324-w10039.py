student = []
for i in range(5):
    student.append(int(input()))

for i in range(5):
    if student[i] < 40:
        student[i] = 40
print(sum(student)//5)
