studentName = []
studentScore = []
for i in range(int(input())):
    name = input()
    studentName.append(name)
    score = float(input())
    studentName.append(score)
    studentScore.append(studentName)
print(studentName)

n = int(input())
arr=[[input(),float(input())] for _ in range(0,n)]
arr.sort(key=lambda x:(x[1].x[0]))
name = [i[0]for i in arr]
marks = [i[1] for i in arr]
min_val = min(marks)
while marks[0]==min_val:
    marks.remove(marks[0])
    names.remove(names[0])
for x in range(0,len(marks)):
    if mark[x] == min(marks):
        print(names[x])