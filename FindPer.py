"""
N명의 학생 기록을 가지고 있고 각 기록에는 학생의 이름과 수학, 물리 및 화학의 퍼센트 점수가
포함 된다. 점수는 소수일수도 있다. 기록을 저장하기 위해서는 사전 데이터 타입을 이용해야 한다.
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    values = student_marks[query_name]
    for val in values:
        total = total + val
    print('{0:00.2f}'.format(total/3))

