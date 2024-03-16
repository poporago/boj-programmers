sum_answer = 0
answer = 0
grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

for _ in range(20):
    subject_name , score, grade = input().split()
    score = float(score)  # 3학점
    if grade != 'P':
        answer += score
        sum_answer += score * score_list[grade_list.index(grade)]

final_answer = sum_answer / answer
print('{:.6f}'.format(final_answer))
